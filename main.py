from react_agent import graph
from langchain_core.messages import HumanMessage

result = graph.invoke({
    "messages": [HumanMessage(content="¿Qué es la justicia?")]
})

print(result["messages"][-1].content)