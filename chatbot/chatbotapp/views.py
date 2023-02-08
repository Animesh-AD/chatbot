from django.shortcuts import render
from chatterbot import ChatBot
chat_logs = []
def chatbot(request):
    chatbot = ChatBot(name='CBOT')

    if request.method == 'POST':
        input_text = request.POST.get('text')
        response = chatbot.get_response(input_text).text
        chat_logs.append({'user': 'You', 'text': input_text})
        chat_logs.append({'user': 'CBOT', 'text': response})

        return render(request, 'app/chatbot.html', {'response': response, 'chat_logs': chat_logs})

    return render(request, 'app/chatbot.html')
