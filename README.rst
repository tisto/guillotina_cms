.. contents::

GUILLOTINA_CMS
==============

WIP: This package is a work in progress to provide CMS on guillotina

Bundle of cms functionality for guillotina

Prepare Docker env
------------------

MacOS::

    screen ~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
    sysctl -w vm.max_map_count=262144
    (to exit Ctrl + a + d)

Start Docker Background
-----------------------

Start it::

    docker-compose create
    docker-compose up cockroachdb cockroachdb2 elasticsearch
    docker exec -it guillotina_cms_cockroachdb_1 /cockroach/cockroach sql --insecure --execute="CREATE DATABASE guillotina;"

Run dev
-------

docker-compose run --service-ports guillotina


Add CMS container
-----------------

curl -X POST --user root:root http://localhost:8081/db -d '{"@type": "Container", "id": "web", "title": "Plone Site"}'

curl -X POST --user root:root http://localhost:8081/db/web/@addons -d '{"id": "cms"}'


Running Plone React
-------------------

Using yarn on a new terminal::

    cd plone-react
    yarn install
    ( edit src/config.py to point http://localhost:8081/db/web )
    yarn dev

    access http://localhost:4300