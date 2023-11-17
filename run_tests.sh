#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

# Поднимаем виртуальное окружение
python3 -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate

echo -e "${GREEN}[Запуск контейнеров...]${NC}"
docker-compose up -d

# Проверка статуса контейнеров
while [[ "$(docker-compose ps -q | wc -l)" -lt 2 ]]; do
    echo -e "\n${GREEN}[Ожидание запуска контейнеров...]${NC}"
    sleep 2
done

echo -e "\n${GREEN}[Установка зависимостей...]${NC}"
pip install -r app/requirements.txt

# Запуск тестов
echo -e "\n${GREEN}[Запуск тестов...]${NC}"
python test_requests.py

# Деактивация виртуального окружения
deactivate

# Выключение контейнеров
echo -e "\n${GREEN}[Выключение контейнеров...]${NC}"
docker-compose down