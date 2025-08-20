Микросервис для асинхронной отправки уведомлений через **Telegram, Email и SMS** с поддержкой fallback-логики, Celery, Docker и автоматической документации.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![Celery](https://img.shields.io/badge/-Celery-464646?style=flat-square&logo=Celery)](https://docs.celeryq.dev/en/stable/django/index.html)
[![RabbitMQ](https://img.shields.io/badge/-RabbitMQ-464646?style=flat-square&logo=RabbitMQ)](https://www.rabbitmq.com/)
[![Redis](https://img.shields.io/badge/-Redis-464646?style=flat-square&logo=Redis)](https://master--redis-doc.netlify.app/docs//)

---

## 🚀 Функционал

- ✅ Отправка уведомлений через:
  - 📲 **Telegram** (бот)
  - 📧 **Email** (Gmail)
  - 📱 **SMS** (SmsAero)
- 🔁 **Fallback-логика**: если один канал недоступен — пробует следующий
- 🕐 **Асинхронная обработка** через Celery + Redis
- 🗄️ Хранение данных в **PostgreSQL**
- 🐳 Полная поддержка **Docker и Docker Compose**
- 📄 Автоматическая **документация API** (Swagger UI / ReDoc)
- 🧪 Покрытие **тестами**
- 📂 Логирование в файлы
- 🔐 Настройка через `.env`

---

## 🛠️ Технологии

| Категория       | Использовано |
|----------------|-------------|
| Backend        | Python 3.11, Django 5.1, DRF |
| Асинхронность  | Celery 5.4, Redis |
| База данных    | PostgreSQL |
| Документация   | drf-spectacular (OpenAPI 3) |
| Контейнеризация| Docker, Docker Compose |
| Уведомления    | Telegram Bot API, Gmail (SMTP), SmsAero |

---

## 📦 Установка и запуск

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/notification-service.git
cd notification-service

### 2. Создайте файл .env в корне проекта(ЗАПОЛНИТЕ ОБЯЗАТЕЛЬНЫЕ ПОЛЯ В .env.example ПЕРЕД КОПИРОВАНИЕМ!!!)
cp .env.example .env

### 3. Запуститесь через Docker(Первый запуск может занять 2–3 минуты (установка зависимостей).)
docker-compose up --build
### Либо запуститеь с сохранением всех логов в папку logs
bash run_with_logs.sh(если не запускается сделайте файл исполняемым -chmod +x run_with_logs.sh)

### 4. Примените миграции
docker-compose run web python manage.py migrate

### 5. Создайте суперпользователя
docker-compose run web python manage.py createsuperuser
### в Админке создайте пользователей кому нужно будет отправлять уведомления

🌐 API и документация
После запуска откройте:

Swagger UI (интерактивная):
👉 http://127.0.0.1:8000/api/schema/swagger-ui/
ReDoc (красивая документация):
👉 http://127.0.0.1:8000/api/schema/redoc/

📡 Отправка уведомления(через терминал) либо через Postman
curl -X POST http://127.0.0.1:8000/api/notify/ \
-H "Content-Type: application/json" \
-d '{
  "user_id": 1,
  "title": "Привет!",
  "message": "Это тестовое уведомление"
}'
Уведомление будет отправлено через Telegram → Email → SMS (в порядке приоритета). 

🧪 Тесты
docker-compose run web python manage.py test notifications/tests

📂 Логи
Все логи сохраняются в папку logs/:

Если у вас есть предложения по улучшению или какие то вопросы то не стесняйтесь со мной связываться

Мой telegram = @HovardLarson
Мой vk = https://vk.com/feniks1632
