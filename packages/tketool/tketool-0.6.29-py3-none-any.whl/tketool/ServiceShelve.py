from tketool.JConfig import get_config_instance
from tketool.mlsample.LocalSampleSource import LocalDisk_NLSampleSource
from tketool.lmc.llms import *
from tketool.lmc.embeddings import *


class Service_Shelve:
    def __init__(self, config_file_path):
        self.config_obj = get_config_instance(config_file_path)

    def get_config(self):
        return self.config_obj

    def get_datasource(self):
        data_folder_path = self.config_obj.get_config("sample_source_path")
        return LocalDisk_NLSampleSource(data_folder_path)

    def get_llm_GLM6B(self, buffer_version=-1):
        glm_url = self.config_obj.get_config("glm_url", "not_set")
        return ChatGLM(glm_url, version=buffer_version)

    def get_llm_GPT4(self, buffer_version=-1):
        proxys = self.config_obj.get_config("openai_proxy", "not_set")
        api_token = self.config_obj.get_config("openai_token", "not_set")
        temperature = self.config_obj.get_config("openai_temperature", "0.8")

        config_dict = {'temperature': float(temperature)}

        return ChatGPT4(api_token, proxy=proxys, call_dict=config_dict, version=buffer_version)

    def get_llm_GPT35(self, buffer_version=-1):
        proxys = self.config_obj.get_config("openai_proxy", "not_set")
        api_token = self.config_obj.get_config("openai_token", "not_set")
        temperature = self.config_obj.get_config("openai_temperature", "0.8")

        config_dict = {'temperature': float(temperature)}

        return ChatGPT3(api_token, proxy=proxys, call_dict=config_dict, version=buffer_version)

    def get_ft_model(self, model_id, buffer_version=-1, **kwargs):
        proxys = self.config_obj.get_config("openai_proxy", "not_set")
        api_token = self.config_obj.get_config("openai_token", "not_set")
        temperature = self.config_obj.get_config("openai_temperature", "0.8")

        config_dict = {'temperature': float(temperature), **kwargs}

        return FineTuned_Completion_Model(model_id, api_token, proxy=proxys, call_dict=config_dict,
                                          version=buffer_version)

    def get_emb(self, buffer_version=-1, **kwargs):
        api_token = self.config_obj.get_config("openai_token", "not_set")
        proxys = self.config_obj.get_config("openai_proxy", "not_set")
        return Openai_embedding(api_token, proxy=proxys, version=buffer_version)
