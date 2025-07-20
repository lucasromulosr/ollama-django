from typing import Union

import ollama
from django.http import HttpResponseNotAllowed, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ollama_api import config
from ollama_api.config import DEFAULT_MODEL
from ollama_api.utils import async_model_pull


@csrf_exempt
def select_model(request) -> Union[JsonResponse, HttpResponse]:
    if request.method != "GET":
        return HttpResponseNotAllowed(['GET'])

    model_name = request.GET.get("model_name") or DEFAULT_MODEL

    if ':' not in model_name:
        model_name = f'{model_name}:latest'

    # If the selected model differs from the last used one,
    # check if its already in cache or downloads it if necessary.
    # Respond with 503 while downloading; return 200 once model loaded to RAM.
    if model_name != config.LAST_MODEL:
        try:
            model_pulled = any(
                model.model == model_name for model in ollama.list()['models']
            )
            if not model_pulled:
                # downloads model in the background (isolated thread)
                async_model_pull(model_name)
                return HttpResponse(status=503)
        # TODO: identify and process possible exception classes
        except Exception:
            raise

    """
    Ollama API doesnt seems to provide any feature
        to check if a model is loaded in RAM.
    This code is a simple workaround.
    It "pings" the API, which forces it to load the model
        (if not yet available).
    """
    ollama.chat(model=model_name)

    config.LAST_MODEL = model_name

    return HttpResponse(status=200)
