from django.shortcuts import render
import openai, os
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()

api_key = "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"
print(api_key)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    print(userMessage)
    if api_key is not None and request.method == 'GET':
        openai.api_key = api_key
        #user_input = request.POST.get('user_input')
        prompt = userMessage
        response = openai.Completion.create(
            #engine="davinci:ft-jresendis-2023-03-28-07-42-06",
            engine="text-davinci-003",
            prompt = prompt,
            max_tokens = 120,
            stop = ["YOU:", "RESP:"],
            # top_p is default :3
            presence_penalty = 0.6,
            temperature=0.9
        )
        print(response)
        #chatbot_response = response.choices[0].text.strip()
        chatbot_response = response.choices[0].text
    #return render(request, 'main3.html' ,{"response":chatbot_response,"respuesta":userMessage})
    return HttpResponse(chatbot_response)

def chatbot(request):
    chatbot_response = None
    print(request)
    print("Ña")
    a = request.POST.get('user_input')
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input
        response = openai.Completion.create(
            engine="davinci:ft-jresendis-2023-03-28-07-42-06",
            prompt = prompt,
            max_tokens = 120,
            stop = ["YOU:", "RESP:"],
            # top_p is default :3
            presence_penalty = 0.6,
            temperature=0.9
        )
        print(response)
        #chatbot_response = response.choices[0].text.strip()
        chatbot_response = response.choices[0].text
    return render(request, 'main3.html' ,{"response":chatbot_response,"respuesta":a})


