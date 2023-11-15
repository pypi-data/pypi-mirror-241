from openai import OpenAI

from gpt_interface.completions import call_completion
from gpt_interface.log import Log
from gpt_interface.rate_limiter import RateLimiter


class GptInterface:
    def __init__(
        self,
        openai_api_key: str,
        model: str,
        json_mode: bool = False,
        temperature: float = 1.0,
        warnings: bool = True,
    ) -> None:
        self.set_model(model, warnings=warnings)
        self.set_json_mode(json_mode)
        self.temperature = temperature
        self.interface = OpenAI(api_key=openai_api_key)
        self.log = Log()
        self.rate_limiter = RateLimiter()
        self.system_message: str | None = None

    def set_model(self, model: str, warnings: bool = True) -> None:
        self.model = model
        recommended_models = [
            "gpt-3.5-turbo",
            "gpt-4",
            "gpt-4-32k",
        ]
        if warnings and (model not in recommended_models):
            print(f"WARNING: {self.model} is not recognized as a recommended model.")
            print(f"Recommended models: {recommended_models}")
            print(f"See https://platform.openai.com/docs/models for more information.")
            print(f"To deactivate this warning, set warnings=False during GptInterface initialization.")

    def set_rate_limiter(self, min_wait_time_in_sec: int) -> None:
        self.rate_limiter = RateLimiter(min_wait_time_in_sec)

    def set_json_mode(self, json_mode: bool) -> None:
        # TODO: json_mode is not used yet
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
        )
        self.rate_limiter.wait()
        self.log.append("assistant", assistant_message)
        return assistant_message
