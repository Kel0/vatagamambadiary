from decouple import config

ACCOUNT_LAST_4_ID = config("ACCOUNT_LAST_4_ID", cast=str)
EMAIL = config("EMAIL", cast=str)
PASSWORD = config("PASSWORD", cast=str)
