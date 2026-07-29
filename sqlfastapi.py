from fastapi import FastAPI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import  SQLDatabase

from langchain_ollama import ChatOllama
from pydantic import BaseModel


app = FastAPI()
db = SQLDatabase.from_uri("sqlite:///databaes.db")

llm = ChatOllama(model="llama3.2:3b", temperature=0)

agent = create_sql_agent(llm=llm, db=db, verbose=True)

class sql_input(BaseModel):
    mode : str
    question : str

@app.post("/sql_query")
def sql(data :sql_input ) :
    mode = data.mode.lower()
    question = data.question
    if mode=="sql":
        result = agent.invoke({"input": question})
        return {"response" : result["output"]}
    elif mode =="csv":
         result = agent.invoke({"input": question})
         return {"response" : result["output"]}

    else :
        result = llm.invoke(question)
        return {"response" : result.content}
