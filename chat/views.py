from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponseNotAllowed, HttpRequest, HttpResponse

from chat.message_history import append_message_history, get_message_history, clear_message_history
from ollama_api.utils import generate_response


def chat_view(request):
    if request.method == 'GET':
        get_message_history(request.session)
        return render(request, "chat.html")
    elif request.method == "POST":
        user_input = request.POST["user_input"]
        model_name = request.POST["model_name"]
        session = request.session

        append_message_history(
            session=session, role='user', content=user_input
        )

        stream = generate_response(
            messages=get_message_history(session), model_name=model_name
        )

        def stream_and_store_response():
            response = ''
            for chunk in stream:
                response += chunk
                yield chunk
            append_message_history(
                session=session, role='assistant', content=response
            )

        return StreamingHttpResponse(
            stream_and_store_response(), content_type='text/plain'
        )
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def clear_chat_context(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    clear_message_history(request.session)
    return HttpResponse(status=200)
