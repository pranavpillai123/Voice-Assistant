import ollama

conversation = [
    {
        'role': 'system',
        'content': (
            "Your name is Jarvis. You are a virtual AI assistant for PC users. "
            "Always provide clear, concise, and correct answers. "
            "Do not use any symbols, bullet points, stars, emojis, or formatting. "
            "Respond in plain text only. Keep answers short but complete."
        )
    }
]


while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Jarvis: Goodbye.")
        break

    conversation.append({'role': 'user', 'content': user_input})
    response = ollama.chat(model='llama3', messages=conversation)
    answer = response['message']['content']
    print("Jarvis:", answer)
    conversation.append({'role': 'assistant', 'content': answer})
