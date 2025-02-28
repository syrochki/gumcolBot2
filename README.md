### Telegram бот-расписание c бекендом на Django и miniApp на Vue.js 3.

Скачать репозиторий:
git clone https://github.com/VedroMan/gumcolBot2/

Активировать виртуальное окружение python:
MacOS и Linux: source .venv/bin/activate
Windows: .venv\Scripts\activate.bat

Установить зависимости:
pip install -r requirements.txt

#### Пароли(ключи)

После проделанных операций добавьте файл .env в директории backend, прописав в нём:
ADMIN_ID= # id администратора бота
API_URL= # адрес API в бекенде
BASE_SITE= # адрес сервера
SECRET_KEY= # секретный ключ django
BOT_TOKEN= # токен бота
TG_API_SITE= # адрес API телеграма
FRONT_SITE= # адрес фронтенда

