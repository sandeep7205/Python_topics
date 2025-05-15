# Use Ubuntu as the base image. 'latest' means the newest version.
# This gives us a clean Ubuntu environment to start with.
FROM ubuntu:latest

# Maintainer (Optional): Information about who built this image
LABEL maintainer="Sandeep Kumar Mishra"

# Prevent dpkg (package manager) from asking questions during installation
ARG DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python 3 and pip 3
# python3 is the Python interpreter
# python3-pip is the package installer for Python (like npm for Node.js, gem for Ruby)
# -y flag automatically says 'yes' to prompts
# && chains commands: if the first succeeds, run the next.
RUN apt update && \
    apt install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* # Clean up apt cache to keep the image size smaller

# Set the working directory inside the container
# This is where subsequent commands (like COPY, RUN, CMD) will be executed from by default.
# It's like doing 'cd /app' when you enter the container.
WORKDIR /app

# Copy your project folders from your computer (host) into the container's working directory (/app)
# The '.' on the left means "everything in the current directory where the Dockerfile is located" (my_python_docker_app).
# The '.' on the right means "copy it to the WORKDIR set above" (/app).
# This copies your 'arithmetic_calculator' and 'caesar_cipher' folders (and the Dockerfile itself, though it's not needed after the build) into /app.
COPY . .

# (Optional but recommended for projects with dependencies)
# If your projects had a requirements.txt file (listing needed libraries),
# you would add these lines AFTER the COPY command:
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt

# Specify the command that will run when the container starts
# CMD ["bash"] means when you run the container, it will start a bash shell.
# This is useful because you want to run *either* of your projects interactively.
# If you only wanted to run ONE specific script automatically, you'd use something like:
# CMD ["python3", "/app/arithmetic_calculator/main.py"]
# But since you have multiple, "bash" is more flexible for this scenario.
CMD ["bash"]




# FROM ubuntu:latest: Start building our image from the official Ubuntu image. This is the base layer.
# LABEL maintainer="...": Adds metadata (optional but good practice).
# ARG DEBIAN_FRONTEND=noninteractive: Prevents package installation from stopping and asking questions. Important for automated builds.
# RUN apt update && apt install -y python3 python3-pip && rm -rf ...: This is a multi-part command executed during the image build.
# apt update: Updates the list of available packages.
# apt install -y python3 python3-pip: Installs the python3 and python3-pip packages. -y means "yes" to prompts.
# rm -rf /var/lib/apt/lists/*: Cleans up the downloaded package lists, reducing the final image size.
# WORKDIR /app: Sets the default directory inside the container to /app. This is where we'll put our project files.
# COPY . .: Copies everything from the directory on your computer where the Dockerfile is located (my_python_docker_app) into the WORKDIR (/app) inside the container. This crucial step brings your arithmetic_calculator and caesar_cipher folders into the image.
# CMD ["bash"]: This specifies the default command that runs when you start a container from this image. Running bash drops you into a command-line interface inside the running container, allowing you to navigate and execute your scripts manually. The CMD command is executed when the container starts, not during the build.
