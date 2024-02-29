template = """
**Respuesta:**

{answer}

**Explicación:**

El LLM utilizó los siguientes documentos para generar la respuesta:

{documents_list}
"""

ragprompt_string = template.format(
    answer=llm_response["answer"],
    documents_list="\n".join(document["title"] for document in documents),
)
