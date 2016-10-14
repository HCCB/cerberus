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

```
  cdproject  # assuming you've set the project directory location like above
  pip install -r requirements.txt
```

## Installing Optional components

### Installing python-pygraphviz for generating ERD diagrams from models

1. Install python-pygraphviz

  ```
  sudo apt-get install python-pygraphviz
  ```

2. Install python packages (locally)

  ```
  pip install django-extensions
  pip install pyparsing==1.5.7
  pip install pydot=1.1.0
  ```

3. Edit project settings.py and add `django-extensions` to the INSTALLED_APPS

  You can now do `./manage.py graph_models registration -o <output image filename>`

[virtualenvwrapper_docs]: http://virtualenvwrapper.readthedocs.org/en/latest/
