from dataclasses import dataclass, field
from typing import Sequence
from langgraph.graph import add_messages
from langgraph.managed import IsLastStep
from langchain_core.messages import AnyMessage

@dataclass
class InputState:
    messages: Sequence[AnyMessage] = field(default_factory=list, metadata={"annotations": [add_messages]})

@dataclass
class AgentState(InputState):
    is_last_step: IsLastStep = field(default=False)
