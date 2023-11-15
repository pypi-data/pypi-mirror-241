from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Optional, List, Dict, Mapping, Any
from tketool.lmc.models import LLM_Plus
import requests, openai, os


class ChatGLM(LLM_Plus):
    gurl: str = ""

    def __init__(self, _url, **kwargs: Any):
        model_name = "GLM6B"
        super().__init__(model_name, **kwargs)
        self.gurl = _url

    def _post(self, url: str,
              query: Dict) -> Any:
        """POST请求
        """

        _headers = {"Content_Type": "application/json"}
        with requests.session() as sess:
            resp = sess.post(url,
                             json=query,
                             headers=_headers,
                             timeout=60)

        return resp

    def call_model(self, prompt, *args, **kwargs) -> Any:
        query = {
            "prompt": prompt,
            "history": []
        }
        # post
        resp = self._post(url=self.gurl,
                          query=query)

        if resp.status_code == 200:
            resp_json = resp.json()
            predictions = resp_json["response"]

            return predictions
        else:
            return "请求模型Error"


class ChatGPT4(LLM_Plus):
    api_token: Optional[str] = None

    def __init__(self, apitoken, **kwargs: Any):
        super().__init__("gpt-4", price=(0.03, 0.06), **kwargs)

        self.api_token = apitoken
        openai.api_key = self.api_token

        if self.proxy is not None:
            # os.environ['OPENAI_API_PROXY'] = ""
            openai.proxy = self.proxy  # "192.168.2.1:9999"

    def _construct_query(self, prompt: str) -> List:
        """
        构造请求体
        """
        query = [
            {"role": "user", "content": prompt}
        ]
        return query

    def _invoke_model(self, prompt):
        """
        _call
        """

        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=prompt,
            **self.call_dictionary_config
        )

        return response

    def _parse_invoke_result(self, response):
        answer = response.choices[0]['message']['content']

        prompt_token_count = response['usage']['prompt_tokens']
        completion_token_count = response['usage']['completion_tokens']

        self.add_token_use((prompt_token_count, completion_token_count))

        return answer

    def call_model(self, prompt, *args, **kwargs) -> Any:
        query = self._construct_query(prompt)
        invoke_result = self._invoke_model(query)
        result = self._parse_invoke_result(invoke_result)

        return result


class ChatGPT3(LLM_Plus):
    api_token: Optional[str] = None

    def _construct_query(self, prompt: str) -> List:
        """构造请求体
        """
        query = [
            {"role": "user", "content": prompt}
        ]
        return query

    def _invoke_model(self, prompt):
        """
        _call
        """
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=prompt,
            **self.call_dictionary_config
        )

        return response

    def _parse_invoke_result(self, response):
        answer = response.choices[0]['message']['content']

        prompt_token_count = response['usage']['prompt_tokens']
        completion_token_count = response['usage']['completion_tokens']

        self.add_token_use((prompt_token_count, completion_token_count))
        return answer

    def __init__(self, apitoken, **kwargs: Any):
        super().__init__("gpt-3.5-turbo-0613", price=(0.0015, 0.002), **kwargs)
        self.api_token = apitoken
        openai.api_key = self.api_token

        if self.proxy is not None:
            # os.environ['OPENAI_API_PROXY'] = ""
            openai.proxy = self.proxy  # "192.168.2.1:9999"

    def call_model(self, prompt, *args, **kwargs) -> Any:
        query = self._construct_query(prompt)
        invoke_result = self._invoke_model(query)
        result = self._parse_invoke_result(invoke_result)

        return result


class FineTuned_Completion_Model(LLM_Plus):
    api_token: Optional[str] = None

    def __init__(self, model_id, apitoken, **kwargs: Any):
        super().__init__(model_id, price=(0.03, 0.06), **kwargs)
        self.api_token = apitoken
        openai.api_key = self.api_token

        if self.proxy is not None:
            # os.environ['OPENAI_API_PROXY'] = ""
            openai.proxy = self.proxy  # "192.168.2.1:9999"

    def _construct_query(self, prompt: str) -> List:
        return prompt

    def _invoke_model(self, prompt):
        response = openai.Completion.create(
            model=self.model_name,
            prompt=prompt,
            **self.call_dictionary_config
        )

        return response

    def _parse_invoke_result(self, response):
        answer = response.choices[0]['text']

        prompt_token_count = response['usage']['prompt_tokens']
        completion_token_count = response['usage']['completion_tokens']

        self.add_token_use((prompt_token_count, completion_token_count))

        return answer

    def call_model(self, prompt, *args, **kwargs) -> Any:
        query = self._construct_query(prompt)
        invoke_result = self._invoke_model(query)
        result = self._parse_invoke_result(invoke_result)

        return result
