import threading
from typing import Generator

import ollama

from ollama_api.config import DEFAULT_MODEL


def async_model_pull(model_name: str = DEFAULT_MODEL) -> None:
    model_name = model_name or DEFAULT_MODEL
    threading.Thread(
        target=ollama.pull, kwargs={'model': model_name}
    ).start()


def generate_response(
        messages: list[dict],
        model_name: str = DEFAULT_MODEL
) -> Generator[str, None, None]:
    model_name = model_name or DEFAULT_MODEL

    stream = ollama.chat(
        model=model_name,
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        yield chunk['message']['content']
