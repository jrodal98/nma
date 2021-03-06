import pathlib
import platform
import subprocess
import sys

# Hourglass Icon: <https://www.flaticon.com/authors/flat-icons>
# Exclamation Icon: <https://www.flaticon.com/authors/pixel-buddha>


_directory = pathlib.Path(__file__).parent.absolute()
ERROR_ICON = pathlib.Path.joinpath(_directory, "exclamation-mark.png")
TIME_ICON = pathlib.Path.joinpath(_directory, "hourglass.png")


class NotifierNotFoundException(Exception):
    @staticmethod
    def generate(program):
        return NotifierNotFoundException(f"{program} not found. Please install {program} and then try again. If this is a mistake, please submit an issue here: https://github.com/jrodal98/nma")


class UnsupportedPlatformException(Exception):
    @staticmethod
    def generate():
        return UnsupportedPlatformException(f"Your system doesn't appear to be supported (only Linux and MacOS are). If this is a mistake, please submit an issue here: https://github.com/jrodal98/nma")


if platform.system() == "Linux":
    if subprocess.Popen(["which", "notify-send"],
                        stdout=subprocess.PIPE) \
            .communicate()[0].strip():
        def send_notification(title, message, error=False):
            icon = ERROR_ICON if error else TIME_ICON
            subprocess.run(
                ["notify-send", "-i", icon,
                    "-t", "50000", title, message])
    else:
        def send_notification(titile, message, error=False):
            raise NotifierNotFoundException.generate("notify-send")
elif platform.system() == "Darwin":
    if subprocess.Popen(["which", "terminal-notifier"],
                        stdout=subprocess.PIPE) \
            .communicate()[0].strip():
        def send_notification(title, message, error=False):
            subprocess.run(
                ["terminal-notifier",
                    "-appIcon", ERROR_ICON if error else TIME_ICON,
                    "-title", title, "-message", message])
    else:
        def send_notification(title, message, error=False):
            raise NotifierNotFoundException.generate("terminal-notifier")

else:
    def send_notification(title, message, error=False):
        raise UnsupportedPlatformException.generate()
