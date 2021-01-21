FROM python:3.10-rc-buster

ENV DISPLAY=host.docker.internal:0.0
ENV PATH $PATH:/root/.poetry/bin

RUN mkdir -p /workspace

RUN apt-get update \
    && apt-get install -y software-properties-common \
    gnupg2
RUN apt-get update  \
    && wget -q http://emacs.ganneff.de/apt.key -O- | apt-key add
RUN add-apt-repository "deb http://emacs.ganneff.de/ buster main"

RUN apt-get update \
    && apt-get -y install emacs \
    llvm \
    clang \
    libclang-dev \
    git \
    curl \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
    && git clone https://github.com/tsukudamayo/dotfiles.git \
    && cp -r ./dotfiles/linux/.emacs.d ~/ \
    && cp -r ./dotfiles/.fonts ~/

WORKDIR /workspace
copy . .
#RUN pip install -r requirements.txt

CMD ["/bin/bash"]


