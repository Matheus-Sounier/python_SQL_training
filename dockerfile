FROM ubuntu:latest

# Evita interações geográficas
ENV DEBIAN_FRONTEND=noninteractive

# Dep
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    git \
    ripgrep \
    python3 \
    python3-pip \
    python3-venv \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @gitlawb/openclaude

# Define código no Ubuntu
WORKDIR /app

# Mantém aberto
CMD ["tail", "-f", "/dev/null"]