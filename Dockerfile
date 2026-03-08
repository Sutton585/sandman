# Use the official Python 3.12 slim image
FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies for Playwright and Chromium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxrender1 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements files first to leverage Docker cache
# We use a wildcard to capture all module requirements
COPY modules/*/requirements.txt /tmp/requirements/
RUN for f in /tmp/requirements/*.txt; do pip install --no-cache-dir -r "$f"; done

# Install Playwright browsers globally in the container
RUN playwright install chromium && playwright install-deps

# Keep the container running for interactive use
CMD ["tail", "-f", "/dev/null"]
