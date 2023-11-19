import openai
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.memory import ConversationBufferMemory

from mmon.tools import load_tools


class Engine:
    def __init__(self, llm, verbose_level=0):
        tools = load_tools(llm)
        if verbose_level > 2:
            openai.log = "debug"

        self.executor = create_conversational_retrieval_agent(
            llm=llm,
            tools=tools,
            max_token_limit=2000,
            remember_intermediate_steps=False,
            verbose=verbose_level > 1,
        )

    def run(self, prompt: str) -> str:
        response = self.executor.run(prompt)
        return response
