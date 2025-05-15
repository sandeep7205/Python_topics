**Comprehensive Docker Commands Reference Note: Essential & Commonly Used**

This note provides a summary of key Docker commands for managing images, containers, data, networking, cleanup, and multi-container applications using Docker Compose.

**Prerequisite:** Ensure Docker Engine is installed and running on your system.

---

**1. General Info & Help**

*   **`docker version`** or **`docker -v`**
    *   **Use:** Show the installed Docker version and client/server information.
    *   **Example:**
        ```bash
        docker version
        ```
*   **`docker info`**
    *   **Use:** Display detailed system-wide information about your Docker installation (daemon details, storage driver, resources, etc.).
    *   **Example:**
        ```bash
        docker info
        ```
*   **`docker help`**
    *   **Use:** List all main Docker commands available.
*   **`docker <command> --help`** (e.g., `docker run --help`, `docker network --help`)
    *   **Use:** Get detailed usage instructions, options, and examples for a specific Docker command or command group.
    *   **Example:**
        ```bash
        docker build --help
        ```

---

**2. Image Management (Building, Pulling, Pushing, Listing, Removing)**

*   **`docker pull <image_name>[:tag]`** (e.g., `docker pull ubuntu`, `docker pull python:3.10`, `docker pull nginx:latest`)
    *   **Use:** Download an image (a read-only template for creating containers) from a registry (like Docker Hub).
    *   **Explanation:** `<image_name>` is required. `<:tag>` is optional; if omitted, `latest` is assumed.
    *   **Example:**
        ```bash
        docker pull centos:7         # Pulls CentOS version 7
        docker pull node             # Pulls the latest Node.js image
        ```
*   **`docker images`** or **`docker image ls`**
    *   **Use:** List all Docker images currently stored on your local machine.
    *   **Example:**
        ```bash
        docker images
        ```
*   **`docker build -t <name>[:tag] PATH`** (e.g., `docker build -t my-web-app:v1.0 .`)
    *   **Use:** Build a new Docker image using instructions from a `Dockerfile`.
    *   **Explanation:**
        *   `-t <name>[:tag]`: Assigns a name and optional version tag to the resulting image.
        *   `PATH`: Specifies the "build context" – the directory containing the `Dockerfile` and any files needed for the build. The contents of this directory are sent to the Docker daemon. The `.` means "current directory".
    *   **Example:** (Run from the directory containing your `Dockerfile`)
        ```bash
        docker build -t my-python-app:latest .
        ```
*   **`docker build -f <path/to/Dockerfile> -t <name>[:tag] PATH`** (e.g., `docker build -f dockerfiles/prod.Dockerfile -t my-app:prod .`)
    *   **Use:** Build an image when the `Dockerfile` is located *outside* the root of the build context.
    *   **Explanation:**
        *   `-f <path/to/Dockerfile>`: Specifies the path to the `Dockerfile`, relative to where you run the command.
        *   `PATH`: Still specifies the root of the build context directory whose contents are sent to the daemon.
    *   **Example:** (Run from project root, Dockerfile is in `./dockerfiles/`)
        ```bash
        docker build -f dockerfiles/Dockerfile -t my-app:latest .
        ```
*   **`docker push <image_name>[:tag]`** (e.g., `docker push my-username/my-image:latest`)
    *   **Use:** Upload (push) a local image to a registry (like Docker Hub or a private registry).
    *   **Explanation:** You usually need to tag the image with your registry username or the registry URL before pushing (e.g., `docker tag my-app:latest my-username/my-app:latest`). You'll also need to log in (`docker login`).
    *   **Example:**
        ```bash
        docker tag my-app:latest your-dockerhub-username/my-app:latest
        docker login # Enter your Docker Hub credentials
        docker push your-dockerhub-username/my-app:latest
        ```
*   **`docker tag <source_image>[:tag] <target_image>[:tag]`** (e.g., `docker tag my-app:v1.0 my-app:latest`)
    *   **Use:** Create a new tag for an existing image. Useful for giving an image multiple names or preparing it for pushing to a specific registry.
    *   **Example:**
        ```bash
        docker tag my-app:build-12345 my-username/my-app:latest
        ```
*   **`docker rmi <image_name>[:tag] or <image_id>`** (e.g., `docker rmi alpine:latest`, `docker rmi f7b6a5c4d3e2`)
    *   **Use:** Remove one or more Docker images from your local machine.
    *   **Explanation:** Identify the image by name:tag or its Image ID.
    *   **Note:** You must first remove any containers that were created from this image. Use the `-f` (force) flag (`docker rmi -f <image>`) to force removal, which also removes dependent containers (use with caution!).
    *   **Example:**
        ```bash
        docker rmi old-unused-image
        ```
*   **`docker history <image_name>[:tag] or <image_id>`**
    *   **Use:** Show the history of an image. Displays each layer that makes up the image and the command that created it.
    *   **Example:**
        ```bash
        docker history ubuntu:latest
        ```

---

**3. Container Management (Run, Start, Stop, Remove, List, Rename)**

*   **`docker run [OPTIONS] <image_name>[:tag] [COMMAND] [ARG...]`**
    *   **Use:** Create a new container from a specified image and start it. This is the fundamental command for launching containers.
    *   **Explanation:** If `[COMMAND]` is provided, it overrides the image's default command (`CMD` or `ENTRYPOINT`). If no command is specified, the image's default is used.
    *   **Common Options (See Examples in General `run` section):**
        *   `-it`: Interactive + TTY (for shells/interactive apps)
        *   `-d`: Detached (run in background)
        *   `--name <container_name>`: Assign a custom name
        *   `-p <host_port>:<container_port>`: Publish ports
        *   `-v <volume_source>:<container_dest>`: Mount volumes or bind mounts
        *   `--network <network_name>`: Connect to a specific network
        *   `--env KEY=VALUE` or `-e KEY=VALUE`: Set environment variables
*   **`docker create [OPTIONS] <image_name>[:tag] [COMMAND] [ARG...]`**
    *   **Use:** Create a new container from an image, but do **not** start it immediately.
    *   **Explanation:** Useful if you want to set up a container's configuration (volumes, ports, etc.) but start it later with `docker start`. Takes the same options as `docker run`.
    *   **Example:**
        ```bash
        docker create --name my-stopped-container -v my-data:/data ubuntu
        # Container created but not running
        ```
*   **`docker ps`** or **`docker container ls`**
    *   **Use:** List currently **running** containers.
    *   **Example:**
        ```bash
        docker ps
        ```
*   **`docker ps -a`** or **`docker container ls -a`**
    *   **Use:** List **all** containers (running, stopped, exited) on your machine.
    *   **Explanation:** `-a` stands for "all".
    *   **Example:**
        ```bash
        docker ps -a
        ```
*   **`docker start <container_name_or_id>`**
    *   **Use:** Start one or more previously created (and currently stopped) containers.
    *   **Example:**
        ```bash
        docker start my-stopped-container
        ```
*   **`docker stop <container_name_or_id>`**
    *   **Use:** Gracefully stop one or more running containers (sends SIGTERM, waits, then SIGKILL).
    *   **Example:**
        ```bash
        docker stop my-running-container
        ```
*   **`docker restart <container_name_or_id>`**
    *   **Use:** Stop and then start one or more containers.
    *   **Example:**
        ```bash
        docker restart my-app-server
        ```
*   **`docker kill <container_name_or_id>`**
    *   **Use:** Forcefully stop one or more running containers immediately (sends SIGKILL).
    *   **Example:**
        ```bash
        docker kill stubborn_container
        ```
*   **`docker rm <container_name_or_id>`**
    *   **Use:** Remove one or more containers.
    *   **Explanation:** Containers must typically be stopped first. Use `-f` (force) to stop and remove a running container (use with caution!).
    *   **Example:**
        ```bash
        docker rm container-to-delete
        docker rm -f container-to-force-delete # Stops and removes
        ```
*   **`docker rename <current_name_or_id> <new_name>`**
    *   **Use:** Change the name of an existing container.
    *   **Example:**
        ```bash
        docker rename old-name new-name
        ```
*   **`docker update [OPTIONS] <container_name_or_id>`**
    *   **Use:** Update the configuration of one or more running containers (e.g., resource limits like CPU or memory).
    *   **Example:**
        ```bash
        docker update --memory 512m my-app-container
        ```

---

**4. Interacting with Running Containers**

*   **`docker logs [OPTIONS] <container_name_or_id>`**
    *   **Use:** Fetch and display the standard output (stdout) and standard error (stderr) logs from a container's main process.
    *   **Options:**
        *   `-f`: Follow log output (like `tail -f`).
        *   `--tail <number>`: Show only the last N lines.
        *   `--since <timestamp or duration>`: Show logs since a specific time.
    *   **Example:**
        ```bash
        docker logs my-web-server         # Show all logs
        docker logs -f my-web-server      # Follow logs in real-time
        docker logs --tail 100 my-web-server # Show last 100 lines
        ```
*   **`docker exec -it <container_name_or_id> <command>`** (e.g., `docker exec -it my-app-container bash`, `docker exec -it db-container psql -U user dbname`)
    *   **Use:** Execute a *new* command inside a *running* container.
    *   **Explanation:**
        *   `-it`: Makes the execution interactive with a pseudo-TTY (essential for interactive shells or commands that need input/output).
        *   `<command>`: The command to execute inside the container. Common commands are `bash` or `sh` to get a shell prompt for inspection or debugging.
    *   **Example:**
        ```bash
        docker exec -it my-python-app-container bash # Get a bash shell
        docker exec my-web-server nginx -s reload    # Send a reload signal to Nginx
        ```
*   **`docker attach <container_name_or_id>`**
    *   **Use:** Attach your terminal's standard input, output, and error streams to a running container's main process.
    *   **Explanation:** Use with caution; detaching usually requires a specific key sequence (often Ctrl+P, Ctrl+Q) to avoid stopping the container. Different from `exec`, which runs a *new* process. Useful for seeing the *primary* process output of a container run without `-d`.
    *   **Example:**
        ```bash
        docker attach my-container-running-in-foreground
        ```

---

**5. Data Persistence (Volumes)**

*   **`docker volume create <volume_name>`** (e.g., `docker volume create app-db-data`)
    *   **Use:** Create a named volume managed by Docker. Volumes are the preferred way to persist data and share it between containers.
    *   **Example:**
        ```bash
        docker volume create my-app-persistent-data
        ```
*   **`docker volume ls`** or **`docker volume list`**
    *   **Use:** List all Docker volumes present on your machine.
    *   **Example:**
        ```bash
        docker volume ls
        ```
*   **`docker volume inspect <volume_name>`**
    *   **Use:** Display detailed low-level information about a volume (location on disk, driver, etc.).
    *   **Example:**
        ```bash
        docker volume inspect my-app-persistent-data
        ```
*   **`docker volume rm <volume_name>`**
    *   **Use:** Remove one or more volumes.
    *   **Note:** Cannot remove a volume if it is currently being used by a container.
    *   **Example:**
        ```bash
        docker volume rm old-backup-volume
        ```
*   **`docker volume prune`**
    *   **Use:** Remove all unused local volumes.
    *   **Explanation:** Prompts for confirmation before removing volumes that are not attached to any container.
    *   **Example:**
        ```bash
        docker volume prune
        ```
*   **(Mounting Volumes/Bind Mounts):** Done using the `-v` or `--mount` flag with `docker run` (see `docker run` section above).

---

**6. Networking**

*   **`docker network create [OPTIONS] <network_name>`** (e.g., `docker network create my-app-internal-net --driver bridge`)
    *   **Use:** Create a custom network for containers to connect to. Containers on the same custom network can communicate with each other using container names as hostnames.
    *   **Explanation:** `--driver bridge` is the default and most common type for custom networks.
    *   **Example:**
        ```bash
        docker network create my-web-app-network
        ```
*   **`docker network ls`** or **`docker network list`**
    *   **Use:** List all Docker networks (including default ones like `bridge`, `host`, `none`, and custom ones).
    *   **Example:**
        ```bash
        docker network ls
        ```
*   **`docker network inspect <network_name>`**
    *   **Use:** Display detailed information about a network, including which containers are connected to it.
    *   **Example:**
        ```bash
        docker network inspect my-web-app-network
        ```
*   **`docker network rm <network_name>`**
    *   **Use:** Remove one or more custom networks.
    *   **Note:** Cannot remove a network if containers are currently connected to it.
    *   **Example:**
        ```bash
        docker network rm unused-dev-network
        ```
*   **`docker network prune`**
    *   **Use:** Remove all unused networks.
    *   **Explanation:** Prompts for confirmation before removing networks that no containers are attached to.
    *   **Example:**
        ```bash
        docker network prune
        ```
*   **`docker network connect <network_name> <container_name_or_id>`**
    *   **Use:** Connect a running container to an existing network.
    *   **Example:**
        ```bash
        docker network connect my-new-network existing-container
        ```
*   **`docker network disconnect <network_name> <container_name_or_id>`**
    *   **Use:** Disconnect a running container from a network.
    *   **Example:**
        ```bash
        docker network disconnect default-bridge existing-container
        ```
*   **(Connecting Containers to Networks):** Done using the `--network` flag with `docker run` (see `docker run` section above).

---

**7. System & Cleanup**

*   **`docker system df`**
    *   **Use:** Show Docker disk space usage (images, containers, volumes, build cache).
    *   **Example:**
        ```bash
        docker system df -v # -v for more detail
        ```
*   **`docker system prune`**
    *   **Use:** Remove unused Docker objects: stopped containers, unused networks, and dangling images (image layers not associated with a tagged image).
    *   **Explanation:** This is a safe command for freeing up disk space and will ask for confirmation.
    *   **Example:**
        ```bash
        docker system prune
        ```
*   **`docker system prune -a`**
    *   **Use:** Remove *all* unused Docker objects: all stopped containers, all unused networks, and *all* unused images (not just dangling ones).
    *   **Explanation:** A more aggressive cleanup. Also prompts for confirmation. Use with caution!
    *   **Example:**
        ```bash
        docker system prune -a
        ```
*   **`docker system prune --volumes`**
    *   **Use:** Includes unused volumes in the cleanup. Requires confirmation.
    *   **Example:**
        ```bash
        docker system prune --volumes
        ```

---

**8. Docker Compose (Multi-Container Applications)**

*   **What it is:** A tool for defining and running **multi-container Docker applications** using a YAML file (`docker-compose.yml` or `compose.yaml`).
*   **Command:** Use `docker compose` (newer syntax) or `docker-compose` (older syntax, might still be needed on some systems).
*   **`docker compose up [OPTIONS] [SERVICES...]`**
    *   **Use:** Build (if images aren't found), create, start, and attach to containers for all services defined in the `compose.yaml` file.
    *   **Options:**
        *   `-d`: Run in detached mode (in the background).
        *   `--build`: Force rebuild images before starting.
    *   **Example:** (Run from the directory containing your `compose.yaml` file)
        ```bash
        docker compose up       # Start services in foreground
        docker compose up -d    # Start services in background
        docker compose up --build web # Rebuild and start only the 'web' service
        ```
*   **`docker compose down [OPTIONS]`**
    *   **Use:** Stop and remove containers, networks, and volumes created by `docker compose up`.
    *   **Options:**
        *   `-v`: Remove volumes (by default, volumes are preserved).
        *   `--rmi all`: Remove images used by services.
    *   **Example:** (Run from the directory containing your `compose.yaml` file)
        ```bash
        docker compose down          # Stop and remove containers/networks
        docker compose down -v       # Stop, remove containers/networks, and remove volumes
        ```
*   **`docker compose ps`** or **`docker compose list`**
    *   **Use:** List the containers (services) managed by Docker Compose for the current project.
    *   **Example:**
        ```bash
        docker compose ps
        ```
*   **`docker compose logs [OPTIONS] [SERVICES...]`**
    *   **Use:** View log output from services defined in the `compose.yaml` file.
    *   **Options:**
        *   `-f`: Follow log output.
    *   **Example:**
        ```bash
        docker compose logs web db     # Show logs for web and db services
        docker compose logs -f         # Follow logs for all services
        ```
*   **`docker compose build [SERVICES...]`**
    *   **Use:** Build or rebuild images for services defined in the `compose.yaml` file.
    *   **Example:**
        ```bash
        docker compose build           # Build images for all services
        docker compose build frontend  # Build image only for the frontend service
        ```
*   **`docker compose exec [OPTIONS] SERVICE COMMAND [ARGS...]`**
    *   **Use:** Run a command in a running container managed by Compose. Similar to `docker exec` but targets a service name from the `compose.yaml`.
    *   **Options:**
        *   `-it`: Interactive + TTY (common for shells).
    *   **Example:**
        ```bash
        docker compose exec backend bash # Get a bash shell in the 'backend' service container
        docker compose exec db pg_dump dbname > backup.sql # Run a backup command in the 'db' service container
        ```

---

**9. Inspection & Diagnostics**

*   **`docker inspect <object_name_or_id>`** (e.g., `docker inspect my-container`, `docker inspect my-image:latest`, `docker inspect my-network`, `docker inspect my-volume`)
    *   **Use:** Display detailed low-level information (in JSON format) about a Docker object (container, image, network, volume, etc.). Incredibly useful for debugging and seeing configuration.
    *   **Example:**
        ```bash
        docker inspect my-running-container
        docker inspect my-web-app:latest
        ```
