import google.generativeai as genai
genai.configure(api_key="AIzaSyD-CVthktVp9DRBxm8YR3Ak5Wa_Q0PgdAI")
for n in genai.list_models():
    print(n.name)