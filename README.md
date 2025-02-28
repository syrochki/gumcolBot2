### Telegram бот-расписание c бекендом на Django и miniApp на Vue.js 3.

<b>Скачать репозиторий</b>:

<i>git clone https://github.com/VedroMan/gumcolBot2/</i>

<b>Активировать виртуальное окружение python</b>:

MacOS и Linux: <i>source .venv/bin/activate</i>

Windows: <i>.venv\Scripts\activate.bat</i>

<b>Установить зависимости</b>:

pip install -r requirements.txt

<b>Пароли(ключи)</b>

После проделанных операций добавьте файл .env в директории backend, прописав в нём:

ADMIN_ID= # id администратора бота<br>
API_URL= # адрес API в бекенде<br>
BASE_SITE= # адрес сервера<br>
SECRET_KEY= # секретный ключ django<br>
BOT_TOKEN= # токен бота<br>
TG_API_SITE= # адрес API телеграма<br>
FRONT_SITE= # адрес фронтенда<br>
