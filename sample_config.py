import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('BOT_TOKEN', '6132329564:AAEJBoyXwP9eipKIQAxT7yQHf39HzyhV_5A')
API_ID = int(os.environ.get('API_ID', '9774346'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQCVJQoAU7DnsHMNCIYRXTid4KfseZitP3zjMiHyZ0S4Hwl3UBDvu76NL1akk6zmTlphpz_RHLO3YYqpVyOJ6HhTHH-r5JbTQ4yULJKUa9xttehEKtfUtmXk1YLf0B4FyYOSZkwxAZfJTJOVhrNKKtpWeX9wDp6VXhROapyxSg5mattQvifb4une2gi4DH4OXMpMlpaT0ijWszG0lwaV6W1tn4TSuvoqR4X1kIS02CphOdTef8EZV1td8c0vaGduYExae5ncqmBnaleDrRqF73Ps2k2MZWremjtZ6bNZ9MYfeyO1Usjy9nNxb_GsVXc2F0sSwhNauez4iCGlgJoJ6kqK3b6phAAAAAA2GAb2AA')
API_HASH = os.environ.get('API_HASH', 'a92aed7d74654a563af4b07efbcd88e9')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '907544310').split()))
LOG_GROUP_ID = int(os.environ.get('LOG_GROUP_ID', '-1001844573348'))
GBAN_LOG_GROUP_ID = int(os.environ.get('GBAN_LOG_GROUP_ID', '-1001844573348'))
MESSAGE_DUMP_CHAT = int(os.environ.get('MESSAGE_DUMP_CHAT'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL', 'mongodb+srv://ZoMusic:Rextor99@zomusic.iabfu0l.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY', 'QUIHTR-JTXPCQ-XZSLAV-RNJXML-ARQ')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'False').lower() in ['false', '1']
