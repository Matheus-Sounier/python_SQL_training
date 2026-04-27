FROM ubuntu:latest

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    ca-certificates \
    git \
    code \
    ripgrep \
    python3 \
    python3-pip \
    python3-venv \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @gitlawb/openclaude

RUN mkdir -p /home/ubuntu/.openclaude && chown -R 1000:1000 /home/ubuntu

WORKDIR /home/ubuntu
# WORKDIR /app

CMD ["openclaude"]