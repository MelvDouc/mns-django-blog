# https://docs.docker.com/reference/dockerfile/

# Pull the latest Python 3 image, slim version.
FROM python:3-slim

# Create non-admin user.
RUN useradd -m app_user

# Create the application working directory and change into it.
WORKDIR /app

# Dependencies are to be installed before copying the source code
# as the former may be cached by Docker to speed up the build process.
COPY requirements.txt .

# Install dependencies. Caching is unnecessary.
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn psycopg2-binary

# Copy all other files, except for those specified in `.dockerignore`.
COPY . .

# Create directories for static files.
RUN mkdir -p /app/static
RUN mkdir -p /var/www/media

# Give app_user ownership of relevant directories.
RUN chown -R app_user /app
RUN chown -R app_user:app_user /var/www/media

USER app_user

# "Describe which ports your application is listening on."
EXPOSE 8000

# Start Python app in container.
CMD [ "gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000" ]
