# OpenWeatherAPIRu

# Начало Работы

1. Установка зависимостей:
   Перед запуском скрипта убедитесь, что у вас установлены необходимые зависимости. Вы можете установить их с помощью следующих команд:
   `pip install requests`
   `pip install python-decouple`


2. Настройка API ключа:
Для использования API OpenWeatherMap вам понадобится API ключ. Вы можете получить бесплатный API ключ, зарегистрировавшись на сайте OpenWeatherMap.

3. Конфигурация:
- Создайте файл `.env` в той же директории, что и скрипт.
- Добавьте ваш API ключ в файл `.env`, используя формат: `API_KEY=ваш_реальный_api_ключ`.

# Использование

1. Запуск скрипта:
Откройте терминальное окно и перейдите в директорию с скриптом. Затем запустите скрипт с помощью команды:
`python main.py`


2. Ввод названия города:
После запуска скрипта вас попросят ввести название города, для которого вы хотите получить погодную информацию.

3. Отображение погодной информации:
Скрипт получит данные о погоде из API OpenWeatherMap и отобразит следующую информацию:
- Название города
- Описание погоды
- Текущая температура (в градусах Цельсия)
- Температура "ощущается как" (в градусах Цельсия)
- Влажность (в процентах)
- Скорость ветра (в метрах в секунду)
- Облачность (в процентах)

# Важные Замечания

- Скрипт использует функцию `config` из библиотеки `decouple` для безопасного хранения и извлечения API ключа

- В данный момент скрипт настроен на отображение информации о погоде на русском языке (`lang="ru"`). Вы можете изменить параметр `lang` в функции `get_weather`, чтобы изменить язык.

- Для выполнения запросов к API OpenWeatherMap используется библиотека `requests`.

- Скрипт содержит функцию `print_weather_info`, которая форматирует и выводит полученные данные о погоде.

- Ответ API обрабатывается как объект JSON, что позволяет легко извлекать информацию о погоде.

# Благодарности
Спасибо ChatGPT за README.md)


