# How to Use

## Install Prerequisites Libraries for Pillow

```
sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```

## Install python-pip

```
sudo apt-get install python-pip
```

## Install virtualenvwrapper

_See [virtualenvwrapper Docs][virtualenvwrapper_docs]_ for more details.

1. Install virtualenv using python-pip

  ```
  sudo pip install virtualenvwrapper
  ```

2. Create virtual environment for cerberus

  ```
  mkvirtualenv cerberus
  cd <cerberus path>
  setvirtualenvproject
  ```

## Install NPM v5

**NB: you should _not_ run scripts directly off the internet, it is dangerous to say the least**

```
  sudo apt-get purge npm nodejs nodejs-legacy # remove any existing nodejs installs
  wget -qO- https://deb.nodesource.com/setup_5.x | sudo -E bash - # run the bash script from nodesource (see NB above)
  sudo apt-get install nodejs # install nodejs
  sudo npm install -g --upgrade npm # upgrade npm just in case
```

## Install nodejs dependencies

1. Install Babel globally, it doesn't like local installs

  ```
  sudo npm install -g babel
  ```

2. Install dependencies in devDependencies

  ```
  npm -d install
  ```

## Install required python packages

[virtualenvwrapper_docs]: http://virtualenvwrapper.readthedocs.org/en/latest/
