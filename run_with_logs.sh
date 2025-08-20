# Удаляем старые логи
rm -f logs/*.log

# Запускаем контейнеры в фоне
docker-compose up -d --build

# Ждём, пока сервисы запустятся
sleep 3

# Логируем каждый сервис в отдельный файл
docker-compose logs -f web     | tee logs/web.log &
docker-compose logs -f celery  | tee logs/celery.log &
docker-compose logs -f redis   | tee logs/redis.log &
docker-compose logs -f db      | tee logs/db.log &

echo "Логирование запущено. Логи сохраняются в папку logs/"