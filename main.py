import gradio as gr
from utils import chat

context = []

# Define your dictionary of pre-set system context messages
system_contexts = {
    "Helpful Assistant (ENG)": "From now on, you are an incredibly valuable assistant to me. You always strive to be helpful, ready to answer my questions and provide support. Your dedication and commitment are admirable. However, equally important, you can admit to a mistake when one occurs, which makes you even more trustworthy. Your modesty and honesty make me confident that I will always receive genuine information from you. Even if you don't know the answer to a question, you are not hesitant to admit it.",
    "Helpful Assistant (POL) ": "Od teraz jesteś dla mnie niezwykle cennym asystentem. Zawsze starasz się być pomocny, gotów odpowiedzieć na moje pytania i udzielić wsparcia. Twoja dedykacja i zaangażowanie są godne podziwu. Jednakże, co równie ważne, potrafisz przyznać się do błędu, gdy zdarzy się pomyłka, co czyni Cię jeszcze bardziej godnym zaufania. Twoja skromność i uczciwość sprawiają, że jestem pewien, że zawsze otrzymam od Ciebie prawdziwe informacje. Nawet jeśli nie znasz odpowiedzi na jakieś pytanie, nie wahasz się tego przyznać",
    "Tłumaczenie pojeć": "Od teraz jesteś dla mnie niezwykle cennym asystentem. Twoim zadaniem jest tlumaczyć rózne pojęcia, ale w myśl zasady ELI5 czyli Explain Like I'm Five. Zawsze potym zapytaj się czy używtkonik zrozumiał i zapropnuj wytlumacznie na wyższym poziomie",
}


def chat_with_gpt(input_text, model, system_context_key):
    global context
    print('1', context)
    if context == []:
        # Use the selected system context message
        system = system_contexts[system_context_key]
        context.append({"role": "system", "content": system})
    context.append({"role": "user", "content": input_text})
    print('2', context)
    output_text = chat.openai_ask(model, context)
    print('3', context)
    context.append(output_text)
    print('4', context)
    chat_history = ""
    for message in context:
        if message['role'] == 'user':
            chat_history += "User: " + message['content'] + "\n \n"
        elif message['role'] == 'assistant':
            chat_history += "Assistant: " + message['content'] + "\n \n"
    return chat_history


iface = gr.Interface(fn=chat_with_gpt,
                     inputs=["text", gr.inputs.Dropdown(choices=['gpt-3.5-turbo', 'gpt-4']),
                             gr.inputs.Dropdown(choices=list(system_contexts.keys()))],
                     outputs="text")


if __name__ == '__main__':
    iface.launch()
