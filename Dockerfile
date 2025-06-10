# https://docs.docker.com/reference/dockerfile/

# Pull the latest Python 3 image, slim version.
FROM python:3-slim

# Install `make`.
RUN apt update && apt install build-essential -y

# Create non-admin user.
RUN useradd -m app_user

# Create the application working directory and change into it.
WORKDIR /app

# Dependencies are to be installed before copying the source code
# as the former may be cached by Docker to speed up the build process.
COPY requirements.txt .

# Install dependencies. Caching is unnecessary.
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy all other files, except for those specified in `.dockerignore`.
COPY . .

# Make app_user owner of working dir.
RUN chown -R app_user /app

USER app_user

# "Describe which ports your application is listening on."
EXPOSE 5173

# Start Python app in container.
CMD [ "make", "run" ]