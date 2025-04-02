FROM ubuntu:latest

RUN apt update && apt install -y sudo
#RUN useradd -m -s /bin/bash testuser && echo 'testuser:password123' | chpasswd
#RUN usermod -aG sudo testuser
RUN apt install git -y
RUN #cd /home/testuser/
RUN git clone https://github.com/seroburomalinoviy/mytonprovider.git
#USER testuser
RUN mkdir -p /home/root
WORKDIR /mytonprovider
RUN chmod +x ./install.sh
RUN export DEBIAN_FRONTEND=noninteractive

CMD ["bash","-c","./install.sh; sleep infinity"]
