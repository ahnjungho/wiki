# Wiki

[![Build Status](https://travis-ci.org/ahnjungho/wiki.svg?branch=master)](https://travis-ci.org/ahnjungho/wiki)

[Personal wiki site](http://wiki.ahnjungho.org)

## Requirements

- Python 3.4.3

## Install & Run

``` shell
$ git clone git@github.com:ahnjungho/wiki.git
$ cd wiki
$ pyvenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Test

### Django Test

``` shell
$ python manage.py test
```

### Coverage.py

``` shell
$ coverage run --source='.' --omit='./venv/*.*' manage.py test
$ coverage html
$ open htmlcov/index.html
```
