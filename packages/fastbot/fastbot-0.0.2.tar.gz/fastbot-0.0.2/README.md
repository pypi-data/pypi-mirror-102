# Fastbot

[![PyPI version](https://img.shields.io/pypi/v/fastbot.svg)](https://pypi.org/project/fastbot/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/fastbot.svg)](https://pypi.org/project/fastbot/)
[![PyPI downloads](https://img.shields.io/pypi/dm/fastbot.svg)](https://pypistats.org/packages/fastbot)

Fastbot is an sdk for building enterprise-grade conversational experiences, written in Python.


## How to install 

```shell
pip install fastbost
```


## Integration with other frameworks

```python
from fastbot import DialogManager, InMemoryDataStore, InMemoryDialogSet
from fastbot.responses import init, end, ContentType, Request
app = DialogManager(data_store=InMemoryDataStore(), dialog_set=InMemoryDialogSet())

if __name__ == '__main__':
    @app.root(default="enter_number")
    def root_handler(dialog=None, request=None, state=None, **kwargs):
        return init(text="Hello\nPlease enter\n1. Yes \n2. No")

    @app.dialogue(name="enter_number")
    def selected_choice(dialog=None, request=None, state=None, **kwargs):
        return end(text="You entered request {0}".format(request.text), content_type=ContentType.TEXT)

    rq = Request(channel_type='facebook', session="user-1", text="Hello")

    rp = app.handle(rq)

    print(rp.json())

    rq = Request(channel_type='facebook', session="user-1", text="Hello")

    rp = app.handle(rq)

    print(rp.json())
```




