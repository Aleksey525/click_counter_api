# Счетчик кликов по ссылкам
Приложение для сокращения ссылок и получения количества кликов по ним. Работает с API ресурса [bitly.com](https://app.bitly.com/Bo1gdG8iCoh/home)

### Как установить

* Зарегистрироваться на [bitly.com](https://app.bitly.com/Bo1gdG8iCoh/home)

* Получить токен [app.bitly.com/settings/api](https://app.bitly.com/settings/api)
  
```
GENERIC ACCESS TOKEN - нужный тип токена
```
* После получения токена создать .env файл в корневом каталоге проекта

* Прописать переменную окружения BITLY_TOKEN = 'Ваш токен'

* Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
* Ссылка на документацию ресурса - [dev.bitly.com](https://dev.bitly.com)

### Примеры запуска приложения в терминале

* Создание сокращенной ссылки

  ```
  python main.py https://python-scripts.com/requests
  Битлинк: bit.ly/3O62ifV
  ```

* Получение количества кликов

  ```
  python main.py http://bit.ly/3O62ifV
  По вашей ссылке прошли 7 раз(а)
  ```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
