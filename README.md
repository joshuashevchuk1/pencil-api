# pencil-api
An API around pencil-code, a high order hydro solver

http://pencil-code.nordita.org/

### Installation

The pencil-api runs a flask server via docker

To build the flask server run the following command

```commandline
docker build -t pencil-api .
```

```commandline
docker run -it pencil-api
```