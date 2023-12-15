FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y python3 wget unzip

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    sh /tmp/miniconda.sh -b -u -p /opt/miniconda3 && \
    rm -rf /tmp/miniconda.sh

# Update package lists and install Git
RUN apt-get update && \
    apt-get install -y git

# Set up environment variables
ENV PATH="/opt/miniconda3/bin:${PATH}"

# Install AWS CLI
RUN /opt/miniconda3/bin/conda install -y -c conda-forge awscli

# Copy your application files
COPY . /home/app
WORKDIR /home/app


CMD ["bash", "./deployment/index.sh"]
