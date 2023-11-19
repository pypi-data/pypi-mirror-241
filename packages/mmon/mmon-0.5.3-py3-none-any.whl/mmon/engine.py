import openai
from langchain.agents import AgentType, Tool, initialize_agent

from mmon.tools import load_tools

# openai.log = "debug"


class Engine:
    def __init__(self, llm, verbose_level=0):
        self.agent = initialize_agent(
            load_tools(llm),
            llm,
            agent=AgentType.OPENAI_MULTI_FUNCTIONS,
            verbose=verbose_level > 1,
        )

    def run(self, prompt: str) -> str:
        response = self.agent.run(prompt)
        return response
