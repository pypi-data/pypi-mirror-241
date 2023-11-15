from tketool.JConfig import get_config_instance
from tketool.lmc.models import *
from tketool.ServiceShelve import Service_Shelve
# from langchain.chat_models import ChatOpenAI
import os


def get_init_llm():
    service_shelve = Service_Shelve("")
    llm_type = service_shelve.get_config().get_config("llm_type", "chatgpt")

    if llm_type == "gpt4":
        return service_shelve.get_llm_GPT4()
        # return OpenAI(temperature=float(temperature), model_name=model_name)

    if llm_type == "glm":
        return service_shelve.get_llm_GLM6B()

    raise Exception("Notset")
