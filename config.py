import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6841893746:AAEw6rjO14pLOI12h1YY4DzqER39WtY-gd0")

    APP_ID = int(os.environ.get("APP_ID", 25829176))

    API_HASH = os.environ.get("API_HASH", "160b2bf653ee7dd974bd6d09a7968cd1")

    