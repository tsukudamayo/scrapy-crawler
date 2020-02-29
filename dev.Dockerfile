FROM python:3.7.6-buster

RUN mkdir -p /workspace
WORKDIR /workspace
copy . .
RUN apt-get update \
    && apt-get -y install emacs \
    llvm \
    clang \
    libclang-dev \
    && git clone https://github.com/tsukudamayo/dotfiles.git \
    && cp -r ./dotfiles/linux/.emacs.d ~/ \
    && cp -r ./dotfiles/.fonts ~/ \
    && pip install -r requirements.txt

CMD ["/bin/bash"]


