import sys
from os import path

class runnr_ver:
    ver = 'v0.3.0'

    runnr_help = """
Usage:
    runnr [options] <file>

runnr Options:
    -h, --help                          Shows help.
    -V, --version                       Shows current runnr version.
    -U, --update                        Checks and update runnr using pip.

Config Options:
    --config                            Shows current directory of config file.
    --reset-config                      Resets config directory and its configurations to default.
    --set-path <full-path>              Sets new path as default for config file.
    --remove-path                       Removes custom path from config file.
    init, -i                            Initializes a new config file in current working directory.
    -default, -d                        Uses configs from default config file.

General Options:
    -debug <other-options> <file>       Prints executed runnr commands.
    -run <Y/N> <file>                   Sets running after compilation to on or off.
    -out <output-file-name> <file>      Sets output file name of the executable.
    -param <parameter> <file>           Passes additional configurations to the compiler/interpreter.
    -args <arguments> <file>            Passes additional command line arguments to the executable.
    -open <file>                        Opens a file in a program. (Uses "-open" configuration from runnr.conf)
    -files <file1>, <file2>, ...        Executes multiple files simultaneously.
    -link <library-name>                Passes specified libaray name to the compiler while automatically adding "-l".
    -lf                                 Disables auto addition of "-l" in "-link" option.
"""

    def defaultPath(self) -> str:
        match  sys.platform:
            case 'win32':
                return f"{path.expanduser('~')}\\runnr.conf"

            case 'darwin' | 'linux':
                return path.expanduser('~') + '/.config/runnr.conf' 

            case _ :
                print(f'runnr: error: unsuported operation system {sys.platform}')
                exit(1)

        return ''