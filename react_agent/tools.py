from langchain.tools import tool
import wikipedia

wikipedia.set_lang("es")

@tool
def wiki_search(term: str) -> str:
    """Busca un resumen del término en Wikipedia en español."""
    try:
        summary = wikipedia.summary(term, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Término ambiguo. Intenta ser más específico. Opciones: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "No se encontró una página para ese término."
    except Exception as e:
        return f"Error al buscar en Wikipedia: {str(e)}"
