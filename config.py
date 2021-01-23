import ast
from os import environ
from pyrogram import filters


API_ID = environ.get('1331889') # Get these two from https://my.telegram.org eg:1234567
API_HASH = environ.get('b6f525900fd20d4282116c6fe13094ac') # Get these two from https://my.telegram.org.  eg:ab1c23def45fg67890h123i45678j9kl
TOKEN = environ.get('1539987153:AAHaJz_OCFJXTT-Oig_jNryHkwn9FjvUJ80')   ## Get this from @Botfather eg:1234567890:ABCdEFgHij1KlMNop_QrStuVWxyzuA-EmXI
SUDO_USERS = environ.get('879481389') # The IDs of the users which can stream, skip, pause and change volume. eg: 625145821
GROUP = environ.get('-1001474831419') # The ID of the group where your bot streams. eg:-1001402753006
MONGO_DB_URI = environ.get('mongodb+srv://edi123:edi123@cluster0.r463p.mongodb.net/dbtest?retryWrites=true&w=majority') # Your mongodb uri. eg:mongodb+srv://username:password@vcpb.opda3.mongodb.net/<dbname>?retryWrites=true&w=majority
USERS_MUST_JOIN = environ.get('USERS_MUST_JOIN', 'True') # Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
LANG = environ.get('LANG', 'id') # Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
DUR_LIMIT = environ.get('DUR_LIMIT', 20) # Max video duration allowed for user downloads in minutes




## No need to touch the following.
API_ID = int(API_ID)
SUDO_USERS = list(map(int, SUDO_USERS.split()))
if type(GROUP) is str:
  GROUP = int(GROUP)
DUR_LIMIT = int(DUR_LIMIT)
USERS_MUST_JOIN = ast.literal_eval(USERS_MUST_JOIN)
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
