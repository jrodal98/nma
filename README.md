# nma

## Requirements:

- Linux or MacOS
    - If running Linux, `send-notify` also needs to be installed
        - Google it for your distro. It's probably already installed, unless you're running something like arch with no desktop enviroment.
    - If running MacOS, `terminal-notifier` also needs to be installed
        - `brew install terminal-notifier`
- python 3.6+

## Installation

enter the `nma` directory and run `python3 -m pip install .`

## About

This python package contains a python shell script (and decorator) that sends a desktop notification whenever a shell process or decorated function finishes execution. 

## Examples

### In shell scripts

`nma "echo test"`


`nma "sudo pacman -Syu"`


`nma "sleep 1; echo test"`

or in actual scripts:

```bash
my_func () {
    ls *
    sleep 2
    echo "nice"   
}

nma my_func
```

### Decorator

```python
from nma.notify_decorator import notify_after
@notify_after
def test():
    print("basic test")
```

