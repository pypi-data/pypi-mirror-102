# frostii-api

An API wrapper for frostii-api.

# Installation

```shell
python3 -m pip install frostii-api
```

## Example

```python
import frostiiapi

frostii_api = frostiiapi.Client("Your API token") # If you dont have a token, get one from https://frostii-api.herokuapp.com/

# Always Has been

await frostii_api.alwayshasbeen(text="Your Text Here")
```