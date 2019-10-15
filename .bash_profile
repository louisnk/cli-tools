# Source the bashrc file so we just edit everything in one place
if [ -f ~/.bashrc ]; then
   source ~/.bashrc
fi


# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

export PATH="$HOME/.cargo/bin:$PATH"
