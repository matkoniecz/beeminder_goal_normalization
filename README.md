Automate keeping beeminder goal settings as desired
===========================

Useful for keeping settings on goals as desired, even after changing mind how settings should be used across multiple goals.

Implemented using [pyminder](https://github.com/narthur/pyminder).

Note that this is not a library but script customized to fit how I use Beeminder - you are more likely to be inspired by it or fork it than to  use it directly.

## install

`pip3 install --user -r requirements.txt`

Create `token.secret` file with your Beeminder API token. See [https://api.beeminder.com/#preliminaries](https://api.beeminder.com/#preliminaries), section "Personal authentication token".

## Running tests

```nosetests3``` or ```python3 -m unittest```
