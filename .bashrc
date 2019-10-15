test=$(/bin/ps -ef | grep ssh-agent | grep -v grep | /usr/bin/awk '{print $2}' | xargs)

if [ "$test" = "" ]; then
   # there is no agent running
  if [ -e "$HOME/.ssh/agent.sh" ]; then
    # remove the old  file
    rm -f $HOME/.ssh/agent.sh
    echo "mars"
  fi;
   # start a new agent
    echo "venus"
   /usr/bin/ssh-agent | grep -v echo >&$HOME/.ssh/agent.sh
fi;

test -e $HOME/.ssh/agent.sh && source $HOME/.ssh/agent.sh

alias kagent="kill -9 $SSH_AGENT_PID"

function git_pull {
  git fetch origin &&
  git merge origin/$()
}

function als {
  aws s3 ls s3://$1/$2 $3
}

function s3up.pub {
  aws s3 sync ./$1 s3://$2 --acl public-read
}

function decks {
  docker exec -it  $1 /bin/bash
}

alias dc='docker-compose'
alias dcu='docker-compose up --build -d'
alias dcl='docker-compose up --build'
alias dlog='docker logs -f'
alias dls='docker ps'
alias dssh=decks
alias ga='git add'
alias gaa='git add --all'
alias gb='git branch'
alias gc='git commit -S -m'
alias gd='git diff'
alias gfo='git fetch origin'
alias gk='git checkout'
alias gl='git log'
alias gm='git merge'
alias gp=git_pull
alias gph='git pull && git push heroku'
alias gpp='gp && git push'
alias gpu="git push -u origin $(git branch | grep \* | cut -d ' ' -f2)"
alias gr='git rm'
alias grh='git reset HEAD'
alias gs='git status'
alias kc='kubectl'
alias keys='pbcopy < ~/.keys/vpn'
alias kgp='kubectl get pod'
alias ll='ls -lhFGA'
alias n='nvm'
alias rrf='rm -rf'
alias subl='/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl'
alias w='cd ~/workspace'
alias c='cd ~/workspace/cp/'
alias p='cd ~/workspace/persisto/'
alias f='cd ~/workspace/foundry/'
alias da='direnv allow'
alias rn='react-native'
alias rni='react-native run-ios'
alias rna='react-native run-android'
alias se='swagger project edit'
alias sdf='sls deploy function -f'
alias sds='sls deploy -s'
alias srs='sls remove -s'

alias ..='cd ..'
alias l='ll'
alias s='ssh'

alias pt='ping 8.8.8.8 -c 5'
alias pl='ping 192.168.1.1 -c 5'
alias airport=/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport

function gkb_fn {
  git checkout -b $1 &&
  git push -u origin $1
}

alias gkb=gkb_fn

function gmd_fn {
  gk develop && gp && gk $1 && gm develop && gpp
}

alias gmd=gmd_fn

function mv_fn {
  mv $3.$1 _$3.$2
}

alias mv_=mv_fn

function travis_add_encrypted {
  travis encrypt $1 --add $2
}

alias tae=travis_add_encrypted

alias sindy="c && cd indy-sdk && docker build -f ci/indy-pool.dockerfile -t indy_pool . && docker run -itd -p 9701-9708:9701-9708 indy_pool"

export NVM_DIR="/Users/creativity/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"  # This loads nvm

nvm use 12

# Setup env variables
export ANDROID_HOME=/usr/local/share/android-sdk
export PATH=/usr/local/sbin:$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
export ANDROID_SDK_ROOT=$ANDROID_HOME

# Libindy specific requirements (Hyerledger Indy)
export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"
export PKG_CONFIG_ALLOW_CROSS=1
export CARGO_INCREMENTAL=1
export RUST_LOG=indy=trace
export RUST_TEST_THREADS=1
export OPENSSL_DIR=/usr/local/Cellar/openssl/1.0.2p     ## path may change as versions bump


function prompt {
  local BLACK="\[\033[0;30m\]"
  local BLACKBOLD="\[\033[1;30m\]"
  local RED="\[\033[0;31m\]"
  local REDBOLD="\[\033[1;31m\]"
  local GREEN="\[\033[0;32m\]"
  local GREENBOLD="\[\033[1;32m\]"
  local YELLOW="\[\033[0;33m\]"
  local YELLOWBOLD="\[\033[1;33m\]"
  local BLUE="\[\033[0;34m\]"
  local BLUEBOLD="\[\033[1;34m\]"
  local PURPLE="\[\033[0;35m\]"
  local PURPLEBOLD="\[\033[1;35m\]"
  local CYAN="\[\033[0;36m\]"
  local CYANBOLD="\[\033[1;36m\]"
  local WHITE="\[\033[0;37m\]"
  local WHITEBOLD="\[\033[1;37m\]"
  local RESETCOLOR="\[\e[00m\]"
  local THREEDOTS=$"\u2192"

  export PS1="\n$WHITEBOLD\[☯\] $CYAN\w$GREEN → $RESETCOLOR"
}

eval "$(direnv hook bash)"

[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

export PATH="/usr/local/opt/openssl/bin:$HOME/Library/Python/3.7/bin:$PATH"

if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
eval "$(pyenv init -)"

export PKG_CONFIG_ALLOW_CROSS=1
export CARGO_INCREMENTAL=1
export RUST_TEST_THREADS=1
export OPENSSL_DIR=/usr/local/Cellar/openssl/1.0.2q

export GOPATH=$HOME/workspace
export GOROOT=/usr/local/opt/go/libexec
# export PATH=$PATH:$GOPATH/bin
export PATH=$PATH:$GOROOT/bin
export PYTHONPATH=$PATH:/lib/python2.7/site-packages/

prompt

