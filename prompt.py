def ragprompt(question, documents): 
    return   f"""Utilice las siguientes pedazos de contexto para responder la pregunta al final.
             Si no sabe la respuesta, simplemente diga que no la sabe, no intente inventar una respuesta.
             Conteste siempre en español.
            {documents}
            Pregunta: {question}
            """