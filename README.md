# FastAPI получения сведений с kinopoisk через открытое API
 ## установка и запуск в docker
 - Создать окружение "python -m venv venv" для windows
 - Скачать с git репозитория
 - Установить все зависимости из файла "requirements.txt" 
    командой "pip install -r requirements.txt"
 - создать файл ".env"
 - перенести переменные из файла ".env.example"
 - Задать не заданные значения для переменных базы данных и KINOPOISK_API_KEY
 - Запустить Docker desctop
 - Создать docker щбраз командой: "docker build -t kinopoisk_api ."
 - Запустить командой "docker-compose up --build"
 - Открыть в браузере "http://localhost:8000/docs#/"
 - Зарегистрировать пользователя
 - Залогиниться
 - Использовать все остальные Endpoint-ы

 ## Реализованый функционал
  - все кроме тестов, времени не хватает