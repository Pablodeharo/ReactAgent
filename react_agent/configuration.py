from dataclasses import dataclass, field
from typing import Annotated, Optional
from langchain_core.runnables import RunnableConfig, ensure_config
from react_agent.prompts import SYSTEM_PROMPT

@dataclass(kw_only=True) # kw true significa que todos los campos deben pasarse como argumentos nombrados
class Configuration:
    system_prompt: str = field(default=SYSTEM_PROMPT)
    model_path: str = field(default="C:\\Users\\Lucas\\Desktop\\Socrates\\llm_proyect\\src\\modelo_dialogos")
    max_search_results: int = field(default=5) # Número maximo de resultados que devuelven herramientas como wikipedia o la base de datos

    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig] = None) -> "Configuration":
        config = ensure_config(config)
        cfg = config.get("configurable") or {}
        return cls(**{k: v for k, v in cfg.items() if k in cls.__annotations__})
