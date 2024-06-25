# Deploy with Docker Compose

```sh
cp .env.default .env
docker compose build && docker compose up -d
```


# Some useful commands

```sh
# look for last 20 log lines and follow the stdout until Ctrl-C
docker compose logs --tail 20 -f api

# execute the command inside the container
docker compose exec api <command>
```