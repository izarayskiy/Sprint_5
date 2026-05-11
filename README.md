# Sprint_5

Проект для автоматизированных UI-тестов на Selenium с запуском в Google Chrome

Все тесты находятся в директории `tests`
Фикстуры находятся в файле `tests/conftest.py`
Локаторы находятся в файле `tests/locators.py`
Тесты на каждую функциональность вынесены в отдельный файл

## Подготовка

Создайте виртуальное окружение:

```
python3 -m venv .venv
```

Активируйте виртуальное окружение:

```
source .venv/bin/activate
```

Установите зависимости:

```
python3 -m pip install -r requirements.txt
```

## Запуск тестов

```
pytest tests
```
