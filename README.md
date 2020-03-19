# *N*otify *M*e *A*fter

## About

*N*otify *M*e *A*fter (nma) is a python package that sends a desktop notification whenever a shell process or decorated function finishes execution. This repository provides a python shell script for general use and a decorator for use within python code.

## Requirements:

- Linux or MacOS
    - If running Linux, `send-notify` also needs to be installed
        - Google it for your distro. It's probably already installed, unless you're running something like arch with no desktop enviroment.
    - If running MacOS, `terminal-notifier` also needs to be installed
        - `brew install terminal-notifier`
- python 3.6+

## Installation

enter the `nma` directory and run `python3 -m pip install .`

## Examples

### In shell scripts

`nma "echo test"`


`nma "sudo pacman -Syu"`


`nma "sleep 1; echo test"`

`sleep 1; echo test | nma -`

```bash
my_func() {
    sleep .1;
}
my_func | nma -
```
### Decorator

```python
from nma.notify_decorator import notify_after
@notify_after
def test():
    print("basic test")
```

## Unimplemented Features

* ~~Call script via piping (ex: `sleep 1 | nma -`)~~
* Email notifications
* Text notifications
