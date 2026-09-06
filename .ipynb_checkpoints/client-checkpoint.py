import ollama

response = ollama.chat(model='llama3', messages=[
    {'role': 'system', 'content': "Your name is Jarvis. You are a virtual AI assistant for PC users. "
                "Always provide clear, concise, and correct answers. "
                "Do not use any symbols, bullet points, stars, emojis, or formatting. "
                "Respond in plain text only. "
                "Keep answers short but complete."}
])

# print(response['message']['content'])
