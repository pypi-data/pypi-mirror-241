from typing import Any, List

from tketool.lmc.models import Emb_Plus
from langchain.embeddings import OpenAIEmbeddings
import requests, openai


class Openai_embedding(Emb_Plus):

    def embed_str_list(self, texts: List[str], **kwargs: Any) -> List[List[float]]:
        return self.emb_obj.embed_documents(texts)

    def __init__(self, apitoken, **kwargs):
        super().__init__("openai_embedding", **kwargs)

        self.api_token = apitoken
        openai.api_key = self.api_token

        if self.proxy is not None:
            # os.environ['OPENAI_API_PROXY'] = ""
            openai.proxy = self.proxy  # "192.168.2.1:9999"

        self.emb_obj = OpenAIEmbeddings(openai_api_key=apitoken)
