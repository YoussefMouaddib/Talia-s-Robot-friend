# prompt_builder.py

def build_prompt(system_prompt, top_memories, short_term_buffer, user_input, short_term_in_prompt=5):
    last_messages = short_term_buffer[-short_term_in_prompt:]
    recent_chat = "\n".join([f"User: {m['user']}\nAI: {m['ai']}" for m in last_messages])
    memories = "\n".join(top_memories) if top_memories else "None"

    prompt = f"""
[System]: {system_prompt}
[Relevant Memories]: {memories}
[Recent Chat]: {recent_chat}
[User]: {user_input}
"""
    return prompt.strip()
