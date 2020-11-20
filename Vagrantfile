Vagrant.configure("2") do |config|
config.vm.box = "hashicorp/bionic64"
config.vm.provision "shell", privileged: false, inline: <<-SHELL
sudo apt-get update
# TODO: Install pyenv prerequisites
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
# TODO: Install pyenv
sudo rm -rf ~/.pyenv
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile
source ~/.profile
  pyenv install 3.7.9
  pyenv global 3.7.9
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
SHELL
end