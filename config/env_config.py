import os

from decouple import config
from pydantic_settings import BaseSettings

__all__ = ['env_config']


class MainConfig(BaseSettings):
    root_path: str = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))


class LoginConfig(BaseSettings):
    username: str = config('LOGIN_USERNAME')
    password: str = config('LOGIN_PASSWORD')

class TaskConfig(BaseSettings):
    reference_task: str = config('REFERENCE_TASK')

class EnvironmentConfig:
    @property
    def main(self) -> MainConfig:
        return MainConfig()

    @property
    def login(self) -> LoginConfig:
        return LoginConfig()

    @property
    def task(self) -> TaskConfig:
        return TaskConfig()


env_config = EnvironmentConfig()
