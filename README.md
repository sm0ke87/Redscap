# Redscap

## Как работать с openscap(общая теория) 
Документация: <https://redos.red-soft.ru/base/redos-7_3/7_3-security/7_3-openscap/?nocache=1728044764963>

1. На сервере должны стоять 2 утилиты: openscap-scanner openscap-utils

`dnf install openscap-scanner openscap-utils`
2. Загруженный xml файл

`wget https://redos.red-soft.ru/support/secure/redos.xml`
3. На проверяемой машине должен стоять только openscap-scanner

`dnf install openscap-scanner`

4. На сервере запускается команда 

`oscap-ssh user@10.81.186.86 22 oval eval --results results.xml --report report.html redos.xml`

## Как работает докер контейнер

Докер контейнер основан debian:trixie-slim.

1. Сборка контейнера

`sudo docker build . --tag redscap:1`
2. Запуск контенера

`docker run -ti --rm -v /opt/result:/tmp:rw redscap:1 192.168.31.156`

где:

`/opt/result` - папка с будущими результатами в формате html

`192.168.31.156` - проверяемый хост, вроде можно через пробел, но не проверял

`-ti ` - для интерактивного режима, что бы ввести пароль к сертификату
# Особенности

В Dockerfile переопределена переменная, что бы подхватывался сертификат

`SSH_ADDITIONAL_OPTIONS='-i /opt/id_rsa -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null'`

При пересборке контейнера нужно подкладывать действующий сертифика, так что --no-cache не используется, лучше делать на 
основе предыдущего контейнера из п.1(docker save\docker load)

