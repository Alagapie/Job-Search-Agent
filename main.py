from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import  load_dotenv
from langchain_groq import ChatGroq
from tavily import TavilyClient
load_dotenv()
from langchain_tavily import TavilySearch 
# tavily = TavilyClient()



# @tool
# def search(query: str) -> str:
#     """
#     args:
#         query: the user question to search forn
        
#     returns:
#         the answer to the user question"""
#     print(f"searching for {query}")
#     result = tavily.search(query)
#     return result
llm = ChatGroq(model='openai/gpt-oss-120b')
tools= [TavilySearch()]
agent= create_agent(model=llm, tools=tools)

def main():
    response = agent.invoke({'messages':[
        HumanMessage(content="I need you to search for 3 different AI roles currently open in Nigeria, and UAE")]
        })
    print(response)

if __name__ == "__main__":
    main()



    