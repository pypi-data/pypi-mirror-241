import sys
import os

data = """#PATH="<full-path>"
#USE PATH="<full-path>" by removing '#' and setting a full-path in double-quotes. It is used to set custom config file path from different location.
#PATH enviorment variable should be mentioned at line number: 1

#config file syntax: (<extension-name>) :: <arguments> = <parameters>, ....
#C
(.c) :: COMPILER="gcc", OUTPUT_FILENAME="$FILE"
#cpp
(.cpp) :: COMPILER="g++", OUTPUT_FILENAME="$FILE"
#python
(.py) :: INTERPRETER="python3"
#open a file
(-open) :: USE="code" """

class runnr_parser():
    default_path : bool = False
    custom_path : bool = False
    runnr_config_table : [dict] = []

    def init(self):
        self.set_path_and_lines()

        for i, line in enumerate(self.lines):
            self.runnr_parse_line(line.replace('\n', ''), i + 1)

    def create_config_file(self):
        f = open(self.path_of_config, 'w')
        f.write(data)
        exit(0)


    def set_path_and_lines(self):
        os_p : str = sys.platform

        if not self.custom_path:
            match os_p:
                case 'win32':
                    self.same_dir_path = f"{os.getcwd()}\\runnr.conf"
                    self.path_of_config = f"{os.path.expanduser('~')}\\runnr.conf"        
                case 'linux' | 'darwin':
                    self.same_dir_path = f"{os.getcwd()}/runnr.conf"
                    self.path_of_config = os.path.expanduser('~') + '/.config/runnr.conf' 
            
                case _ :
                    print(f'runnr: error: {os_p} is not supported at the moment')
                    exit(1)

        if os.path.isfile(self.same_dir_path) and not self.default_path:
            self.runnr_config_file = open(self.same_dir_path, 'r')
            self.path_of_config = self.same_dir_path
        else:
            try:
                self.runnr_config_file = open(self.path_of_config, 'r')
            except:
                print(f'runnr: error: no config file found in "{self.path_of_config}"')
                choice = input('Create a new config file? [Y/n]: ')

                if not choice in ['N', 'n']:
                    self.create_config_file()

                exit(1)

        self.lines = self.runnr_config_file.readlines()

        if not self.lines:
            print(f'runnr: error: config: empty config file found at "{self.path_of_config}"')
            choice = input(f'Write default config datas to "{self.path_of_config}"? [Y/n]: ')

            if not choice in ['N', 'n']:
                self.create_config_file()

            exit(1)

        self.runnr_parse_and_set_custom_path(self.lines[0])


    def runnr_parse_line(self, line : str, line_no : int):
        if '#' in  line or not line:
            return
        
        if line.find('::') == -1:
            print(f'runnr: error: config: no argument separetar "::" found in "{line}" at line number {line_no}')
            exit(1)
        
        parsed_data_list = {}
        if line.count('::') > 1:
            print(f'runnr: syntax error: config: multiple argument separetar "::" in "{line}" at line number {line_no}')
            exit(1)

        un_p_extension, un_p_arguments = line.split('::')
        self.runnr_parse_extension(un_p_extension, line_no, parsed_data_list)
        self.runnr_parse_tokens(un_p_arguments, line_no, parsed_data_list)

        self.runnr_config_table.append({key : parsed_data_list[key]  for key in parsed_data_list})
        parsed_data_list.clear()


    def runnr_parse_extension(self, un_p_extension : str, line_no : int, parsed_data : dict) -> None:
        extension = un_p_extension[un_p_extension.find('(') + 1 : un_p_extension.rfind(')')].replace(' ', '')

        if extension.find(')') != -1 or extension.find('(') != -1:
            print(f'runnr: syntax error: config: multiple parentheses in "{un_p_extension}" at line number {line_no}. Extension must be wrapped with only one level of parentheses "(<extension>)"')
            exit(1)

        if not extension[1:].isalpha():
            print(f'runnr: error: config: "{extension}" is not a valid extension at line number {line_no}')
            exit(1)

        parsed_data['extension'] = extension


    def runnr_parse_tokens(self, un_p_arguments : str, line_no : int, parsed_data : dict) -> None:
        if un_p_arguments.isspace():
            print(f'runnr: syntax error: config: at least one argument is required for an defined extension at line number {line_no}')
            exit(1)

        tokens : [str] = un_p_arguments.split(',')
        
        for i in range(len(tokens)):
            if not tokens[i]:
                print(f'runnr: syntax error: config: unnecessary "," at line number {line_no}')
                exit(1)

            if tokens[i].isspace():
                print(f'runnr: syntax error: config: empty argument between "," at line number {line_no}')
                exit(1)

            if tokens[i].find('"') == -1:
                print(f'runnr: syntax error: config: error at line number {line_no}. All arguments\'s parameters much be wrapped in " "')
                exit(1)

            param = tokens[i][tokens[i].find('"') + 1:tokens[i].rfind('"')]
            args = tokens[i].replace(param, '').replace(' ', '').replace('=', '').replace('"', '')
            self.runnr_set_args_param(args, param, line_no, parsed_data)


    def runnr_set_args_param(self, args : str, param : str, line_no : int, parsed_data : dict):
        match args:
            case 'COMPILER':
                parsed_data['executor'] = param
                parsed_data['type'] = 'c'

            case 'INTERPRETER':
                parsed_data['executor'] = param
                parsed_data['type'] = 'i'

            case 'OUTPUT_FILENAME':
                parsed_data['out'] = param

            case 'USE':
                parsed_data['executor'] = param

            case _:
                print(f'runnr: error: config: unknown argument "{args}" at line number {line_no}')
                exit(1)

    def runnr_get_extension_config(self, extension : str) -> dict:
        for rows in self.runnr_config_table:
            if rows['extension'] == extension:
                return rows
            
        return {}
    
    def runnr_parse_and_set_custom_path(self, line : str) -> bool:
        if self.custom_path:
            self.lines = self.lines[1:]
            return

        separator = line.find('=')
        comment = line.find('#')

        if comment != -1:
            return

        if separator != -1:
            key, value = line[0:separator], line[separator + 1:]

            if key == 'PATH':
                value = value[value.find('"') + 1 : value.rfind('"')]

                if not os.path.isfile(value):
                    print(f'runnr: error: config: no config file found at "{value}"')
                    exit(1)

                self.path_of_config = value
                self.custom_path = True
                self.runnr_config_file.close()          
                self.set_path_and_lines()
            else:
                print(f'runnr: error: config: unknown enviorment variable "{key}" at line number {1}')
                exit(1)
            

        