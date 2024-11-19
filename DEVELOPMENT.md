# Development

### Build docker image
```bash
docker build -t jtrfaker .
```

### Run docker container in interactive mode
```bash
docker compose up -d
```

```bash
docker exec -it jtrfaker bash
```

### Run tests
```bash
pytest
```

### Run linting
```bash
flake8
```
