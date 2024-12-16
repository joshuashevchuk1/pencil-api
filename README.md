# pencil-api
An API around pencil-code, a high order hydro solver

http://pencil-code.nordita.org/

To view progress on the pencil-api, visit the trello board

https://trello.com/b/klPcOAFj/pencil-api

### Installation

The pencil-api runs a flask server via docker

To build the flask server run the following command

```commandline
sudo docker build -t pencil-api .
```

```commandline
docker run -it pencil-api
```