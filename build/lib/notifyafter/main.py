#!/usr/bin/env python3
# Jacob Rodal (https://www.jrodal.dev) (jr6ff@virginia.edu)

import subprocess
import sys
from .notify_decorator import notify_after
from .send_notification import send_notification


@notify_after
def call_from_shell(argv):
    try:
        if len(argv) < 2:
            raise IndexError
        return subprocess.run(argv[1], shell=True, check=True)
    except IndexError:
        send_notification("notify-after error",
                          "shell command not provided", error=True)
    except subprocess.CalledProcessError as e:
        send_notification("notify-after error", str(e), error=True)
    except KeyboardInterrupt:
        send_notification("notify-after error", "Keyboard Interrupt",
                          error=True)
    except Exception as e:
        send_notification("notify-after error", str(e), error=True)
    sys.exit(1)


def main():
    call_from_shell(sys.argv)


if __name__ == "__main__":
    main()
