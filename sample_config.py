import os

from dotenv import load_dotenv

load_dotenv("config.env" if os.path.isfile("config.env") else "sample_config.env")

BOT_TOKEN = os.environ.get('BOT_TOKEN', '6132329564:AAEJBoyXwP9eipKIQAxT7yQHf39HzyhV_5A')
API_ID = int(os.environ.get('API_ID', '9774346'))
SESSION_STRING = os.environ.get('SESSION_STRING', 'BQCVJQoAhx4TNSp8fTizIJa9TQ_7P8pDk2hR1CWTxSu7RW22MxMz201iQ_MMHN1x4yXK3lJROmA3ctmr3mED_i956YFqY0qzv-mTns2yvow8gM8QBYsC4J6Du1WLyHDNOANGU19uk8TxPwmNaTLa2MNKLJu-zaOEpLbeXHUEkQCRGt7EiWIaNesBuMgxKTl6lz8bKDznVy13l1O5wtimx08rSNnChcz5-fUX76L8HeDUFS6xzW7QKamnH3CI21tSL6H6dv9GlvrfZm50_1Gzr0tKRrT72M3B3aMSa5uNyfsrEbXrQ1G08eiqHrQewWafEEw7hS0nd9GC0UWpKQQF9ZUosqPeMAAAAAA2GAb2AA')
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
