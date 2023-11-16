from openai import OpenAI

from gpt_interface.log import Log
from gpt_interface.models import known_models


def call_completion(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message: str | None,
    json_mode: bool,
) -> str:
    if model in [m.name for m in known_models if not m.legacy_chat_api]:
        return call_modern_model(
            interface=interface,
            model=model,
            log=log,
            temperature=temperature,
            system_message=system_message,
            json_mode=json_mode,
        )
    elif model in [m.name for m in known_models]:
        return call_legacy_model(
            interface=interface,
            model=model,
            log=log,
            temperature=temperature,
            system_message=system_message,
        )
    else:
        raise ValueError(f"Unrecognized model: {model}")


def call_modern_model(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message: str | None,
    json_mode: bool,
) -> str:
    messages=[
        {
            "role": message.role,
            "content": message.content
        }
        for message in log.messages
    ]
    if system_message:
        messages.append({
            "role": "system",
            "content": system_message,
        })
    completion_args = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    if json_mode and model in ["gpt-3.5-turbo-1106", "gpt-4-1106-preview"]:
        completion_args["response_format"] = { "type": "json_object" }
    response = interface.chat.completions.create(**completion_args)
    return_message = response.choices[0].message.content
    return return_message if return_message else "[ERROR: NO RESPONSE]"


def call_legacy_model(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message: str | None,
) -> str:
    prompt = "\n".join([
        f"{message.role}: {message.content}"
        for message in log.messages
    ])
    if system_message:
        prompt += "\nsystem: " + system_message
    prompt += "\nassistant: "
    response = interface.completions.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text
