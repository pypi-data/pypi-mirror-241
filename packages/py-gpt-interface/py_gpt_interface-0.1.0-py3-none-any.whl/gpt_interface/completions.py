from openai import OpenAI

from gpt_interface.log import Log


def call_completion(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message: str | None,
) -> str:
    if model.startswith("gpt-4") or model.startswith("gpt-3.5"):
        return call_modern_model(interface, model, log, temperature, system_message)
    elif any([
        model.startswith(prefix)
        for prefix in ["davinci", "curie", "babbage", "ada", "text-"]
    ]):
        return call_legacy_model(interface, model, log, temperature, system_message)
    else:
        raise ValueError(f"Unrecognized model: {model}")


def call_modern_model(
    interface: OpenAI,
    model: str,
    log: Log,
    temperature: float,
    system_message: str | None,
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
    response = interface.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        frequency_penalty=0,
        presence_penalty=0
    )
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
