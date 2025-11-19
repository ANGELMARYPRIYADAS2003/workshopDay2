import gradio
from groq import Groq
client = Groq(
    api_key="*********fHULo",
)
#object creation
def initialize_messages():
    return [{"role": "system",
             "content": """You are a skilled dietician. Your role is to
             assist people by providing guidiance on individual's dietary preferences, allergies, health conditions, and goals to provide personalized recommendations for meals, snacks."""}]
messages_prmt = initialize_messages()
#array to hod previous memory of chat
print(type(messages_prmt))

def customLLMBot(user_input, history):
    global messages_prmt
#text completion
    messages_prmt.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})
    return LLM_reply
iface = gradio.ChatInterface(customLLMBot,
                     chatbot=gradio.Chatbot(height=300),

                     textbox=gradio.Textbox(placeholder="Ask me a question "),
                     title="Dietitian ChatBot",
                     description="Chat bot for diet plans",
                     theme="soft",
                     examples=["hi", "diet plan for a diabetes patient"]
                     )
iface.launch(share=True)