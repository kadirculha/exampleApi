docker rm -f exampleapi

docker run -d -ti --restart=always --name exampleapi -p 8010:8010 exampleapi
