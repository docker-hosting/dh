# Docker-Hosting cli tool
Cli tool to manage your docker-hosting websites.

## Building and running the docker-hosting cli as docker image
```bash
docker build -t dh .

# Now run dh, mount ./webserver to containers /var/www directory
docker run --rm -ti --volume $PWD/webserver:/var/www dh create wordpress test.de
```