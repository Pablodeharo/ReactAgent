from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap
from typing import TypedDict
from react_agent.configuration import Configuration
from react_agent.prompts import SYSTEM_PROMPT_SOCRATIC
from react_agent.tools import wiki_search
from react_agent.utils import load_local_chat_model

# Estado del agente
class AgentState(TypedDict):
    messages: list

# Cargar configuración
config = Configuration()

# Herramientas
TOOLS = [wiki_search]

# Modelo
llm = load_local_chat_model(config.model_path)

# Prompt socrático
prompt_socratic = PromptTemplate.from_template(config.system_prompt + "\n\n{input}")

from langchain_core.runnables import RunnableLambda

chain_socratic = (
    RunnableLambda(lambda state: {"input": state["messages"][-1]["content"]})
    | prompt_socratic
    | llm
    | StrOutputParser()
)

# Construir el grafo
builder = StateGraph(AgentState)
builder.add_node("socrates_reasoning", chain_socratic)
builder.add_node("tool_use", ToolNode(tools=TOOLS))

# Transiciones
builder.add_conditional_edges("socrates_reasoning", tools_condition, {"tool": "tool_use", "final": END})
builder.add_edge("tool_use", "socrates_reasoning")

# Configurar entrada
builder.set_entry_point("socrates_reasoning")

# Compilar
graph = builder.compile()

# Función para chat
def chat_with_agent(input_message: str):
    """
    Función para interactuar con el agente usando mensajes en formato de chat.
    """
    response = graph.invoke({
        "messages": [{"role": "user", "content": input_message}]
    })
    return response
