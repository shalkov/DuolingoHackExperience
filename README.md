## Скрипт для накрутки опыта в Duolingo

<p align="center">
<img src="images/duo_3d.png" alt="image" width="300" height="auto">
</p>

### Инструкция:

**Подробная видеоинструкция:** https://youtu.be/HOubVyP9Wqg

1. Пропатчить APK файл Android приложения с помощью этого скрипта: https://github.com/ilya-kozyr/android-ssl-pinning-bypass, чтобы можно было перехватывать трафик.
2. Установить пропатченное приложение на устройство.
3. Начать слушать трафик с помощью программы **Proxyman**.
4. Пройти одно тренировочное задание, чтобы выполнились запросы **/sessions** и **/batch**. 
5. Склонировать этот репозиторий и открыть в каком-нибудь IDE (например **PyCharm**)
6. С помощью **Proxyman**, сгенерировать **Python** код для этих двух запросов(**/sessions** и **/batch**). 
7. Полученный код вставить в **duolingo_requests.py**, согласно инструкции, которая написана в самом файле. 
8. Запустить скрипт.