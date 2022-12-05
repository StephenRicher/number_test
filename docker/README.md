# Using Number Test via Docker

This directory contains a `Dockerfile` to make it easy to build and run Number Test via [Docker](https://www.docker.com/).

## Installing Docker

Follow the general installation instructions [on the Docker site](https://docs.docker.com/install/):

* [macOS](https://docs.docker.com/docker-for-mac/install/)
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Windows](https://docs.docker.com/docker-for-windows/install/)


## Using Number Test via Docker

```
mkdir number_test-docker
cd number_test-docker
wget https://github.com/StephenRicher/number_test/master/docker/Dockerfile
docker build -t number_test .
```

After the image is built, run the container:

```
docker run --rm -it number_test
```
