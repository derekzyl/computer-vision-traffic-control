
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    DB_URL:str ='postgres://zyhaxiam:EHNQbkPk_-lPNqo8dLb3hV40blIvU9sN@stampy.db.elephantsql.com/zyhaxiam'
    DB_PASSWORD:str=''
    DB_NAME:str=''
    PORT:int=0
    
    HOST:str=''
    model_config= SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    