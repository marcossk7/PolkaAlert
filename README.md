docker rm polkaalert_container
docker rmi polkaalert
docker ps -a
docker run -d --env-file .env --name polkaalert_container polkaalert
docker build -t polkaalert .
docker image prune --filter "dangling=true"