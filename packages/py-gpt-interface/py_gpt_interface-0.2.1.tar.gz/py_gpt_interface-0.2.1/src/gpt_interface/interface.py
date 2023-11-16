from openai import OpenAI

from gpt_interface.completions import call_completion
from gpt_interface.log import Log
from gpt_interface.models import known_models
from gpt_interface.rate_limiter import RateLimiter


class GptInterface:
    def __init__(
        self,
        openai_api_key: str,
        model: str,
        json_mode: bool = False,
        temperature: float = 1.0,
    ) -> None:
        self.set_model(model)
        self.set_json_mode(json_mode)
        self.temperature = temperature
        self.interface = OpenAI(api_key=openai_api_key)
        self.log = Log()
        self.rate_limiter = RateLimiter()
        self.system_message: str | None = None

    def set_model(self, model: str) -> None:
        self.model = model
        if model not in [m.name for m in known_models]:
            print(f"Warning: unrecognized model {model}. Known models list may be out of date.")

    def set_rate_limiter(self, min_wait_time_in_sec: int) -> None:
        self.rate_limiter = RateLimiter(min_wait_time_in_sec)

    def set_json_mode(self, json_mode: bool) -> None:
        self.json_mode = json_mode

    def set_system_message(self, content: str | None) -> None:
        self.system_message = content

    def say(self, user_message: str) -> str:
        self.log.append("user", user_message)
        assistant_message = call_completion(
            interface=self.interface,
            model=self.model,
            log=self.log,
            system_message=self.system_message,
            temperature=self.temperature,
            json_mode=self.json_mode,
        )
        self.rate_limiter.wait()
        self.log.append("assistant", assistant_message)
        return assistant_message
