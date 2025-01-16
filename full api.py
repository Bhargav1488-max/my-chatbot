import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)