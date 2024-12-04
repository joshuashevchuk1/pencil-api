FROM ubuntu:22.04 as build_pencil

# Install required packages including make, MPI compilers, and vim
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libhdf5-openmpi-dev \
    git \
    vim \
    mpich \
    make \
    python3 \
    python3-pip \
    python3-venv && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/pencil-code

ENV PENCIL_HOME=/app/pencil-code

# Clone Pencil Code
RUN git clone https://github.com/pencil-code/pencil-code.git /app/pencil-code

# Create directories for examples and API
RUN mkdir ./examples
RUN mkdir ./examples/example-disc
RUN mkdir ./python/pencil-api

# Copy configuration files and API code
COPY start.in .
COPY . ./python/pencil-api
RUN chmod +x ./python/pencil-api/run.sh
RUN pip3 install -r ./python/pencil-api/requirements.txt

## Uncomment for local debugging
#CMD [ "bash", "-c", "source /app/pencil-code/sourceme.sh && bash"]

CMD ["./python/pencil-api/run.sh"]
