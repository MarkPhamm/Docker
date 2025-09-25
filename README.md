# 🐳 Docker
A hands-on repository documenting my journey learning Docker — from container basics to building and orchestrating real-world applications.

![image](https://github.com/user-attachments/assets/59c65354-b544-4189-9325-d636f2e29db1)

# TLDR:

- **Container**: An isolated process that includes everything it needs to run, providing self-containment and portability.
- **Docker**: A platform that allows you to build, run, and manage containers.
- **Image**: A standardized package that contains all the files, dependencies, and configurations needed to run a container.
- **Registry**: A centralized storage location for container images, like Docker Hub.
- **`docker-compose`**: A tool for defining and running multi-container Docker applications using a YAML file.
- **`Dockerfile`**: A text document that contains instructions to build a Docker image.
- `docker build`: Build an image from `Dockerfile`

# Docker command

## Images

- `docker pull <image>` → Download an image from Docker Hub
- `docker images` → List images available locally
- `docker rmi <image>` → Remove an image
- `docker build -t <name>:<tag> .` → Build an image from a Dockerfile

## Containers

- `docker run <image>` → Run a container
    - Common flags:
        - `it` → Interactive terminal
        - `d` → Detached (background mode)
        - `-name <container>` → Assign a name
        - `p <host:container>` → Port mapping
        - `v <host:container>` → Volume mapping
- `docker ps` → List running containers
- `docker ps -a` → List all containers (including stopped)
- `docker stop <container>` → Stop a container
- `docker start <container>` → Start a stopped container
- `docker restart <container>` → Restart a container
- `docker rm <container>` → Remove a container

## Inspect & Logs

- `docker inspect <container>` → Show detailed info about a container
- `docker logs <container>` → Show container logs
- `docker exec -it <container> <command>` → Run a command inside a container (e.g., bash)

## Docker Compose (multi-container apps)
<img width="1810" height="921" alt="image" src="https://github.com/user-attachments/assets/a794bbbd-04f6-4e38-8a76-508186372fbe" />


- `docker-compose up` → Start services
    - `d` → Run in detached mode (background)
    - `-build` → Build images before starting containers
    - `-force-recreate` → Recreate containers even if config/ image hasn’t changed
    - `-remove-orphans` → Remove containers for services not defined in the current Compose file
    - `f <file>` → Specify an alternate Compose file (default is `docker-compose.yml`)
- `docker-compose down` → Stop and remove services
- `docker-compose ps` → List services
- `docker-compose logs` → Show logs for services

## Cleanup

- `docker system prune` → Remove all unused data (containers, networks, images)
- `docker image prune` → Remove unused images
- `docker container prune` → Remove stopped containers

## Networks

- `docker network ls` → List networks
- `docker network create <name>` → Create a network
- `docker network connect <network> <container>` → Connect container to a network
- `docker network rm <network>` → Remove a network

# 1. Introduction

## 1.1 Container

What is a container? Simply put, containers are isolated processes for each of your app's components. 

- **Self-contained.** Each container has everything it needs to function with no reliance on any pre-installed dependencies on the host machine.
- **Isolated.** Since containers are run in isolation, they have minimal influence on the host and other containers, increasing the security of your applications.
- **Independent.** Each container is independently managed. Deleting one container won't affect any others.
- **Portable.** Containers can run anywhere! The container that runs on your development machine will work the same way in a data center or anywhere in the cloud!

### Container vs VM

- VM is an entire operating system with its own kernel, hardware drivers, programs, and applications. Spinning up a VM only to isolate a single application is a lot of overhead.
- A container is simply an isolated process with all of the files it needs to run. If you run multiple containers, they all share the same kernel, allowing you to run more applications on less infrastructure.

```docker
docker ps        # List running containers
docker ps -a     # List all containers
docker stop      # Stop a running container
```

## 1.2 Image

A container image is a standardized package that includes all of the files, binaries, libraries, and configurations to run a container.

1. Images are immutable. Once an image is created, it can't be modified. You can only make a new image or add changes on top of it.
2. Container images are composed of layers. Each layer represents a set of file system changes that add, remove, or modify files.

### [**Finding images](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/#finding-images)**

[Docker Hub](https://hub.docker.com/) is the default global marketplace for storing and distributing images. 

- [Docker Official Images](https://hub.docker.com/search?q=&type=image&image_filter=official) - a curated set of Docker repositories, serve as the starting point for the majority of users, and are some of the most secure on Docker Hub
- [Docker Verified Publishers](https://hub.docker.com/search?q=&image_filter=store) - high-quality images from commercial publishers verified by Docker
- [Docker-Sponsored Open Source](https://hub.docker.com/search?q=&image_filter=open_source) - images published and maintained by open-source projects sponsored by Docker through Docker's open source program

```docker
docker image ls       # List all images
docker search         # Search for an image on Docker Hub
docker pull           # Download an image from a registry
docker image history  # Show the history of an image
```

## 1.3 Registry

An image registry is a centralized location for storing and sharing your container images. It can be either public or private. [Docker Hub](https://hub.docker.com/) is a public registry that anyone can use and is the default registry.

### Registry vs Repository

A *registry* is a centralized location that stores and manages container images, whereas a *repository* is a collection of related container images within a registry. Think of it as a folder where you organize your images based on projects. Each repository contains one or more container images.

![image.png](attachment:152e82af-6371-484b-a024-095a2d49cf0e:image.png)

## **1.4 What is `docker-compose`?**

Docker Compose is basically a `yml` file for you to define configuration to run multiple container. You include this file in your code repository, anyone that clones your repository can get up and running with a single command.

You don't always need to recreate everything from scratch. If you make a change, run **`docker compose up`** again and Compose will reconcile the changes in your file and apply them intelligently.

docker compose up -d --build

docker compose down

# 2. Building Images

## 2.1 Understanding image layers

Each layer in an image contains a set of filesystem changes - additions, deletions, or modifications. Let’s look at a theoretical image:

1. The first layer adds basic commands and a package manager, such as apt.
2. The second layer installs a Python runtime and pip for dependency management.
3. The third layer copies in an application’s specific requirements.txt file.
4. The fourth layer installs that application’s specific dependencies.
5. The fifth layer copies in the actual source code of the application.

### [**Stacking the layers**](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/#stacking-the-layers)

Layering is made possible by content-addressable storage and union filesystems. While this will get technical, here’s how it works:

1. After each layer is downloaded, it is extracted into its own directory on the host filesystem.
2. When you run a container from an image, a union filesystem is created where layers are stacked on top of each other, creating a new and unified view.
3. When the container starts, its root directory is set to the location of this unified directory, using **`chroot`**.

## 2.2 **Writing a `Dockerfile`**

A `Dockerfile` is a text-based document that's used to create a container image. It provides instructions to the image builder on the commands to run, files to copy, startup command, and more.

```docker
FROM python:3.13  
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src ./src
EXPOSE 5000

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

Some of the most common instructions in a **`Dockerfile`** include:

- **`FROM <image>`** - this specifies the base image that the build will extend.
- **`WORKDIR <path>`** - this instruction specifies the "working directory" or the path in the image where files will be copied and commands will be executed.
- **`COPY <host-path> <image-path>`** - this instruction tells the builder to copy files from the host and put them into the container image.
- **`RUN <command>`** - this instruction tells the builder to run the specified command.
- **`ENV <name> <value>`** - this instruction sets an environment variable that a running container will use.
- **`EXPOSE <port-number>`** - this instruction sets configuration on the image that indicates a port the image would like to expose.
- **`USER <user-or-uid>`** - this instruction sets the default user for all subsequent instructions.
- **`CMD ["<command>", "<arg1>"]`** - this instruction sets the default command a container using this image will run.

## **2.3 Build, tag, and publish an image**

### 2.3.1 Build

`docker build .` When you run a build, the builder pulls the base image, if needed, and then runs the instructions specified in the Dockerfile. 

The final `.` in the command provides the path or URL to the [build context](https://docs.docker.com/build/concepts/context/#what-is-a-build-context). At this location, the builder will find the `Dockerfile` and other referenced files.

With the previous command, the image will have no name, but the output will provide the ID of the image. 

```docker
docker build .
[+] Building 3.5s (11/11) FINISHED                                              docker:desktop-linux
 => [internal] load build definition from Dockerfile                                            0.0s
 => => transferring dockerfile: 308B                                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.12                                  0.0s
 => [internal] load .dockerignore                                                               0.0s
 => => transferring context: 2B                                                                 0.0s
 => [1/6] FROM docker.io/library/python:3.12                                                    0.0s
 => [internal] load build context                                                               0.0s
 => => transferring context: 123B                                                               0.0s
 => [2/6] WORKDIR /usr/local/app                                                                0.0s
 => [3/6] RUN useradd app                                                                       0.1s
 => [4/6] COPY ./requirements.txt ./requirements.txt                                            0.0s
 => [5/6] RUN pip install --no-cache-dir --upgrade -r requirements.txt                          3.2s
 => [6/6] COPY ./app ./app                                                                      0.0s
 => exporting to image                                                                          0.1s
 => => exporting layers                                                                         0.1s
 => => writing image sha256:9924dfd9350407b3df01d1a0e1033b1e543523ce7d5d5e2c83a724480ebe8f00    0.0s
```

With the previous output, you could start a container by using the referenced image:

```docker
 docker run sha256:9924dfd9350407b3df01d1a0e1033b1e543523ce7d5d5e2c83a724480ebe8f00
```

That name certainly isn't memorable, which is where tagging becomes useful.

### 2.3.2 Tag

Tagging images is the method to provide an image with a memorable name. A full image name has the following structure:

```docker
[HOST[:PORT_NUMBER]/]PATH[:TAG]
```

- **`HOST`**: The optional registry hostname where the image is located. If no host is specified, Docker's public registry at **`docker.io`** is used by default.
- **`PORT_NUMBER`**: The registry port number if a hostname is provided
- **`PATH`**: The path of the image, consisting of slash-separated components. For Docker Hub, the format follows **`[NAMESPACE/]REPOSITORY`**, where namespace is either a user's or organization's name. If no namespace is specified, **`library`** is used, which is the namespace for Docker Official Images.
- **`TAG`**: A custom, human-readable identifier that's typically used to identify different versions or variants of an image. If no tag is specified, **`latest`** is used by default.

Examples: 

- **`nginx`**, equivalent to **`docker.io/library/nginx:latest`**: this pulls an image from the **`docker.io`** registry, the **`library`** namespace, the **`nginx`** image repository, and the **`latest`** tag.
- **`docker/welcome-to-docker`**, equivalent to **`docker.io/docker/welcome-to-docker:latest`**: this pulls an image from the **`docker.io`** registry, the **`docker`** namespace, the **`welcome-to-docker`** image repository, and the **`latest`** tag
- **`ghcr.io/dockersamples/example-voting-app-vote:pr-311`**: this pulls an image from the GitHub Container Registry, the **`dockersamples`** namespace, the **`example-voting-app-vote`** image repository, and the **`pr-311`** tag

To tag an image during a build, add the **`-t`** or **`--tag`** flag:

```docker
docker build -t my-username/my-image .
```

If you've already built an image, you can add another tag to the image by using the [`docker image tag`](https://docs.docker.com/engine/reference/commandline/image_tag/) command:

```docker
docker image tag my-username/my-image another-username/another-image:v1
```

### 2.3.3 Publish

Once you have an image built and tagged, you're ready to push it to a registry. To do so, use the [`docker push`](https://docs.docker.com/engine/reference/commandline/image_push/) command:

`docker push my-username/my-image`

## **2.4 Using the build cache**

When building Docker images:

- Each instruction creates a layer that can be cached for future builds
- Cache invalidation happens when:
    - A `RUN` command changes
    - Files copied with `COPY`/`ADD` change
    - Any previous layer is invalidated

**Best practice:** For Node.js apps, structure your Dockerfile like this:

```docker
FROM node:22-alpine
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --production
COPY . .
CMD ["node", "src/index.js"]
```

This way, dependencies only reinstall when package.json changes, not when code changes.

## **2.5 Multi-stage builds**

# 3. Running containers

## 3.1 **Publishing and exposing ports**

Port publishing exposes container services by mapping host:container ports. Use **`-p`** flag with **`docker run`** to create forwarding rules (e.g., **`-p 8080:80`** routes host:8080 → container:80).

 `docker run -d -p HOST_PORT:CONTAINER_PORT nginx`

- **`HOST_PORT`**: The port number on your host machine where you want to receive traffic
- **`CONTAINER_PORT`**: The port number within the container that's listening for connections

For example, to publish the container's port **`80`** to host port **`8080`**:

 `docker run -d -p 8080:80 nginx`

Now, any traffic sent to port **`8080`** on your host machine will be forwarded to port **`80`** within the container.
