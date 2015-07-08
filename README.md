# Wiki

[Personal wiki site](http://wiki.ahnjungho.org)

## Requirements

- Python 3.4.3

## Test

```shell
$ pyvenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ coveage run --source='.' manage.py test
$ coverage html
$ open htmlcov/index.html
```
