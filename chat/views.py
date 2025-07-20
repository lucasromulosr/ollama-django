from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponseNotAllowed
from ollama_api.utils import generate_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat_view(request):
    if request.method == 'GET':
        return render(request, "chat.html")
    elif request.method == "POST":
        user_input = request.POST["user_input"]
        model_name = request.POST["model_name"]
        prompt = f"User: {user_input}\nAI:"
        response = generate_response(prompt, model_name)
        #print(response['message']['content'])
        print(response)
        return StreamingHttpResponse(response, content_type='text/plain')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
