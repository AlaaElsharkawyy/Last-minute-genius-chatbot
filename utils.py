def build_prompt(context, question, system_prompt):
    return f"""
{system_prompt}

Context:
{context}

Question:
{question}

Answer:
"""