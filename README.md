Инстукция:

1. Установить Python 3.6 или выше
2. Создать venv (python3 -m venv venv)
3. Скачаь и разархивировать репозиторий в катоалог виртуальной среды (venv)
4. Установить зависимости (pip install -r requirements.txt)
5. Запуск  тестов 
* REST: >python3 test_controller_api.py
* SOAP: >python3 test_soap.py

# csssr_test

REST API

Документация: [superhero.qa-test.csssr.com](https://superhero.qa-test.csssr.com/swagger-ui.html#/superhero-controller)

Тестовое покрытие:

* swagger.py
* test_controller_api.py

Обнаруженые баги:

* [№1](https://github.com/alex-pancho/csssr_test/issues/1)
* [№2](https://github.com/alex-pancho/csssr_test/issues/2)
* [№3](https://github.com/alex-pancho/csssr_test/issues/3)
* [№4](https://github.com/alex-pancho/csssr_test/issues/4)

SOAP API

Источник: [superhero.qa-test.csssr.com/ws/](https://soap.qa-test.csssr.com/ws/soap.wsdl)

Тестовое покрытие:

* soapwsdl.py
* test_soap.py

Только позитивное тестирование, 5 тест-кейсов, багов не обнаружено.
