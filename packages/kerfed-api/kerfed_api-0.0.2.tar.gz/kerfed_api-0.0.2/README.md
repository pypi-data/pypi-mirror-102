# kerfed_api
[![PyPI version](https://badge.fury.io/py/kerfed-api.svg)](https://pypi.org/project/kerfed-api/)


These are Python bindings to access the [Kerfed REST API](https://api.kerfed.com) for analyzing and automatically quoting CAD assemblies. You can create an API key from any account using the [account management console](https://kerfed.com/account).


## Quick Start
```
pip install kerfed-api

ipython -i
>>> import kerfed_api as ka
>>> quote = ka.Quote('models/camera.3dxml')
>>> quote.parts

```
