# Source the bashrc file so we just edit everything in one place
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi

export PATH="$HOME/.cargo/bin:$PATH"
