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
RUN mkdir pencil-api

# Copy configuration files and API code
COPY start.in .
COPY . ./pencil-api
#
## Uncomment for local debugging
CMD [ "bash", "-c", "source /app/pencil-code/sourceme.sh && bash" ]

#CMD ["python3","./run.py"]
