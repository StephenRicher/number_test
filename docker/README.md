# Using Number Test via Docker

This directory contains a `Dockerfile` to make it easy to build and run Number Test via [Docker](https://www.docker.com/).

## Installing Docker

Follow the general installation instructions [on the Docker site](https://docs.docker.com/install/):

* [macOS](https://docs.docker.com/docker-for-mac/install/)
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Windows](https://docs.docker.com/docker-for-windows/install/)

## Using the CLI of Number Test via Docker

```shell
mkdir number_test-docker
cd number_test-docker
wget https://raw.githubusercontent.com/StephenRicher/number_test/main/docker/Dockerfile
docker build -t number_test .
```

where `number_test` is the desired Docker image name.

Run the CLI from the container:

```shell
docker run --rm -it number_test
```

To run the container through a shell use the following command:

```shell
docker run --rm -it --entrypoint /bin/bash number_test
```

