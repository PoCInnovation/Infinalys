version: "3"

services:
    emma:
        ports:
            - "4444:4444"
        volumes:
            - ./front/emma:/app
        stdin_open: true
        build:
            context: ./front/emma
            dockerfile: ./Dockerfile
        network_mode: "host"
    jean_pierre:
        ports:
            - "5000:5000"
        build:
            context: ./back/jean_pierre
            dockerfile: ./Dockerfile
        volumes:
            - ./back/jean_pierre:/app
        network_mode: "host"
    nicos:
        ports:
            - "4000:4000"
        build:
            context: ./back/nicos
            dockerfile: ./Dockerfile
        volumes:
            - ./back/nicos:/app
        network_mode: "host"
    irma:
        ports:
            - "3000:3000"
        build:
            context: ./back/irma/api
            dockerfile: ./Dockerfile
        volumes:
            - /tmp:/tmp
            - ./back/irma/api:/app
        network_mode: "host"
