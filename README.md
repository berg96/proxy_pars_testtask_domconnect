# ТЗ Proxy Parsing Domconnect

## Описание проекта 

Тестовое задание реализовано на фреймворке Selenium и включает в себя парсинг сайта [PROXY6.net](https://px6.me/) ([https://px6.me/](https://px6.me/)) с выводом результатов в консоль.

### Автор backend Артём Куликов

tg: [@Berg1005](https://t.me/berg1005)

[GitHub](https://github.com/berg96)

## Используемые технологии 

Проект реализован на языке python c использованием следующего технгологического стека:

* Selenium
* WebDriver

## Как запустить проект

Клонировать репозиторий:
```
git clone https://github.com/berg96/proxy_pars_testtask_domconnect.git
```
Перейти в него в командной строке:
```
cd proxy_pars_testtask_domconnect
```
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

Запустить файл:

```
python pars_proxy.py
```
