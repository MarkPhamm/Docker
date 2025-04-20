# 🐳 Exploring Docker Commands
A hands-on repository documenting my journey learning Docker — from container basics to building and orchestrating real-world applications.

Here’s a cleanly formatted and GitHub-friendly version:


Understanding Docker Concepts

1. **Container:** A lightweight, standalone, and executable package that includes everything needed to run a piece of software.

2. **Image:** Think of this as a template or blueprint for containers. It contains all the instructions needed to create a container.

3. **Docker Hub:** Like GitHub but for Docker images — it's where you can find and share container images.

4. **Docker Engine:** The core technology that runs and manages containers on your machine.

---

<img src="https://github.com/user-attachments/assets/175211f9-cfdd-42f6-8dde-cf283f1950db" width="100%"/>

- The **Docker Engine** runs containers  
- **Images** are used to create containers  
- **Docker Hub** stores images  
- The Docker Engine can **pull** images from and **push** images to Docker Hub

---

Sure! Here's the revised Markdown version with a clearer hierarchy and only the Docker command section featuring an icon:

---

# Docker Command

## `docker run hello-world`

```bash
docker run hello-world
```

- **`docker`** – CLI to interact with Docker Engine  
- **`run`** – Instructs Docker to create and start a container  
- **`hello-world`** – The name of the image to run

---

**What Happens When You Run This**

1. Docker checks if the `hello-world` image exists locally  
2. If not, it pulls the image from Docker Hub  
3. A new container is created from the image  
4. The container runs, prints a message, then exits

---

**Behind the Scenes**

- The **Docker client** sends the command to the **Docker daemon**  
- The daemon pulls the image from Docker Hub if needed  
- It creates and starts a container from that image  
- The container’s output is printed in your terminal

---

## `docker images`

```bash
docker images
```

Example Output

```
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    feb5d9fea6a5   2 weeks ago     13.3kB
```
**Column Breakdown**

- **REPOSITORY** – Name of the image (e.g., `hello-world`)  
- **TAG** – Version label (default is `latest`)  
- **IMAGE ID** – Unique identifier for the image  
- **CREATED** – When the image was built  
- **SIZE** – Disk space used by the image  

## `docker ps`

Lists all **running containers** on your system.

```bash
docker ps
```

- Shows container ID, image, status, ports, and more  
- Add `-a` to see **all containers**, including stopped ones:

```bash
docker ps -a
```
---
# Docker Hub

🔗 [https://hub.docker.com/](https://hub.docker.com/)

On an image's page, you can typically find:

- A description of the image  
- Usage instructions  
- The number of pulls (downloads) the image has  
- Available tags (versions)  

Docker Hub is where Docker looks for images when you run a `docker run` command and the image isn’t available locally. This is why you were able to run the `hello-world` container even if you hadn't downloaded it beforehand.

---

## Key Points About Docker Hub

- **Official Images**  
  Curated by Docker, these images are typically well-maintained and documented. Great for beginners and production use.

- **Tags**  
  Images can have multiple versions, called **tags** (e.g., `latest`, `1.0`, `2.1`).  
  If you don’t specify a tag (as in `docker run hello-world`), Docker defaults to using the `latest` tag.

- **Pull Command**  
  Each image page shows a pull command you can use to manually download the image without running it.  
  Example:

  ```bash
  docker pull hello-world
  ```

- **Dockerfile**  
  Many images provide a link to their `Dockerfile`, which is the script used to build the image. Reviewing it can help you understand what’s inside the image and how it was created.
---
