FROM ubuntu:23.10 as build_pencil

# Install required packages including make, mpi compilers, and vim
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libhdf5-openmpi-dev \
    git \
    vim \
    mpich \
    make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/pencil-code

ENV PENCIL_HOME=/app/pencil-code

RUN git clone https://github.com/pencil-code/pencil-code.git /app/pencil-code

# Run the source script using bash
RUN bash -c "source /app/pencil-code/sourceme.sh"

# Define the command to start bash after sourcing the script
CMD bash