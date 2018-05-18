# NIM_API_Python

网易云信服务端API封装(python)


Installation
------------

### The developer way

```sh
git clone https://github.com/jsli/NIM_API_Python.git
cd NIM_API_Python
git checkout -b develop origin/develop
python setup.py install
```

Compatability
-------------

Zoomus has been tested for Python 2.6, 3.2, 3.3, 3.4, and pypy using [Travis CI](https://travis-ci.org/actmd/zoomus)

Example Usage
-------------

### Create the client

```python
from im import ImClient

client = ImClient('API_KEY', 'API_SECRET')
client.user.create(...)
```

### Using with a manage context

```python
with ZoomClient('API_KEY', 'API_SECRET') as client:
    client.user.create(...)
    ...
```


Available methods
-----------------

* client.user.create(...)



Running the Tests
-----------------

### Simple

First, make sure to install the testing requirements

```sh
pip install -r requirements-tests.txt
```

Then run the tests via nose

```sh
nosetests -v
```
