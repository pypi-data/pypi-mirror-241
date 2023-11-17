from .lang.applescript import AppleScript
from .lang.html import HTML
from .lang.javascript import JavaScript
from .lang.powershell import PowerShell
from .lang.python import Python
from .lang.r import R
from .lang.shell import Shell

language_map = {
    "python": Python,
    "bash": Shell,
    "shell": Shell,
    "sh": Shell,
    "zsh": Shell,
    "javascript": JavaScript,
    "html": HTML,
    "applescript": AppleScript,
    "r": R,
    "powershell": PowerShell,
}
