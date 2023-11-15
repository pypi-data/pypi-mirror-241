import abc
from pydantic import BaseModel
from datetime import datetime
from tketool.utils.LocalRedis import *
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.embeddings.base import Embeddings
from typing import Optional, List, Dict, Mapping, Any, Tuple
import requests, openai, os
from tketool.logs import log_debug
from tketool.buffer.bufferbase import *


# class remote_model():
#
#     def __call__(self, *args, **kwargs):
#         if self.use_buffer:
#             nkey = get_hash_key(self.model_name, args, kwargs)
#             if has_item_key(nkey):
#                 log_debug("use_buffer")
#                 buffer_value = get_buffer_item(nkey)
#                 if buffer_value['version'] == self.buffer_version:
#                     return buffer_value['value']
#
#         # rebuild kwargs
#         new_kwargs = {**kwargs, **self.call_dictionary_config}
#
#         call_result = self.call_model(*args, **new_kwargs)
#         if self.use_buffer:
#             buffer_item(nkey, {'version': self.buffer_version, 'value': call_result})
#             flush()
#
#         return call_result


class LLM_Plus(LLM):
    proxy: Optional[str] = ""
    model_name: Optional[str] = ""
    use_buffer: bool = False
    buffer_version: Optional[float] = -1.0
    call_dictionary_config: Dict = {}
    price: Optional[Tuple] = (0.0, 0.0)

    def __init__(self, model_name, version=-1, call_dict={}, price=(0.0, 0.0), proxy=None, **kwargs: Any):
        super().__init__(**kwargs)
        self.proxy = proxy
        self.model_name = model_name
        self.use_buffer = True if version > 0 else False
        self.buffer_version = version
        self.call_dictionary_config = call_dict
        self.price = price

    def add_token_use(self, use: (int, int)):
        now = datetime.now()
        date_time_str = now.strftime("%m_%d")
        keyname = f"lm_{date_time_str}_{self.model_name}"

        if not has_value(keyname):
            set_value(keyname, 0)
            set_value(keyname + "_use_in", 0)
            set_value(keyname + "_use_out", 0)
            set_value(keyname + "_use_in_price", self.price[0])
            set_value(keyname + "_use_out_price", self.price[1])

        value_add(keyname + "_use_in", use[0])
        value_add(keyname + "_use_out", use[1])

        current_cost = get_value(keyname + '_use_in') / 1000 * self.price[0] + self.price[1] / 1000 * get_value(
            keyname + '_use_out')

        log_debug(f"{self.model_name} add token:{use[0]}/{use[1]}"
                  f" totle {get_value(keyname + '_use_in')}/{get_value(keyname + '_use_out')} "
                  f" cost {round(current_cost, 2)}"
                  f"")

    @abc.abstractmethod
    def call_model(self, prompt, *args, **kwargs) -> Any:
        pass

    def _call(self, *args: Any, **kwargs: Any) -> str:
        if self.use_buffer:
            nkey = get_hash_key(self.model_name, args, kwargs)
            if has_item_key(nkey):
                #log_debug("use_buffer")
                buffer_value = get_buffer_item(nkey)
                if buffer_value['version'] == self.buffer_version:
                    return buffer_value['value']

        # rebuild kwargs
        new_kwargs = {**kwargs, **self.call_dictionary_config}

        call_result = self.call_model(*args, **new_kwargs)
        if self.use_buffer:
            buffer_item(nkey, {'version': self.buffer_version, 'value': call_result})
            flush()

        return call_result

    @property
    def _llm_type(self) -> str:
        return self.model_name


class Emb_Plus(Embeddings):
    proxy: Optional[str] = ""
    model_name: Optional[str] = ""
    use_buffer: bool = False
    buffer_version: Optional[float] = -1.0
    call_dictionary_config: Dict = {}
    price: Optional[Tuple] = (0.0, 0.0)

    def __init__(self, model_name, version=-1, call_dict={}, price=(0.0, 0.0), proxy=None, **kwargs: Any):
        super().__init__(**kwargs)
        self.proxy = proxy
        self.model_name = model_name
        self.use_buffer = True if version > 0 else False
        self.buffer_version = version
        self.call_dictionary_config = call_dict
        self.price = price

    def add_token_use(self, use: (int, int)):
        now = datetime.now()
        date_time_str = now.strftime("%m_%d")
        keyname = f"lm_{date_time_str}_{self.model_name}"

        if not has_value(keyname):
            set_value(keyname, 0)
            set_value(keyname + "_use_in", 0)
            set_value(keyname + "_use_out", 0)
            set_value(keyname + "_use_in_price", self.price[0])
            set_value(keyname + "_use_out_price", self.price[1])

        value_add(keyname + "_use_in", use[0])
        value_add(keyname + "_use_out", use[1])

        current_cost = get_value(keyname + '_use_in') / 1000 * self.price[0] + self.price[1] / 1000 * get_value(
            keyname + '_use_out')

        log_debug(f"{self.model_name} add token:{use[0]}/{use[1]}"
                  f" totle {get_value(keyname + '_use_in')}/{get_value(keyname + '_use_out')} "
                  f" cost {round(current_cost, 2)}"
                  f"")

    @abc.abstractmethod
    def embed_str_list(self, texts: List[str], **kwargs: Any) -> List[List[float]]:
        pass

    def embed_documents(self, texts: List[str], **kwargs: Any) -> List[List[float]]:
        if self.use_buffer:
            nkey = get_hash_key(self.model_name, texts)
            if has_item_key(nkey):
                #log_debug("use_buffer")
                buffer_value = get_buffer_item(nkey)
                if buffer_value['version'] == self.buffer_version:
                    return buffer_value['value']

        # rebuild kwargs
        new_kwargs = {**kwargs, **self.call_dictionary_config}

        call_result = self.embed_str_list(texts, **new_kwargs)
        if self.use_buffer:
            buffer_item(nkey, {'version': self.buffer_version, 'value': call_result})
            flush()

        return call_result

    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]
