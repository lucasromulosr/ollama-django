import threading

import ollama

from ollama_api.config import DEFAULT_MODEL


def async_model_pull(model_name: str = DEFAULT_MODEL) -> None:
    model_name = model_name or DEFAULT_MODEL
    threading.Thread(
        target=ollama.pull, kwargs={'model': model_name}
    ).start()


def generate_response(prompt: str, model_name: str = DEFAULT_MODEL) -> str:
    model_name = model_name or DEFAULT_MODEL

    stream = ollama.chat(
        model=model_name,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    for chunk in stream:
        yield chunk['message']['content']
