# Используем официальный образ PostgreSQL 15.10
FROM postgres:15.10

# Устанавливаем переменные окружения для PostgreSQL
ENV POSTGRES_USER=to_do_backend \
    POSTGRES_PASSWORD=159753 \
    POSTGRES_DB=to_do_db

# Открываем стандартный порт PostgreSQL
EXPOSE 5432

# Указываем команду по умолчанию
CMD ["postgres"]
