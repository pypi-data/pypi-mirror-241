# runnr
runnr is an open-source command line interface tool for building, compiling & executing different programs & files. Simple yet Powerful.

runnr is currently in beta stages, any features or its usage may change unexpectedly. It is expected that until `v0.0.5` everything will be finalised and it will be the first stable release. 

[Official Website](https://runnr-cli.vercel.app/)

# Installation

Install runnr with pip:
```bash
pip install runnr
```
    
# Documentation

- ## Config File:

Before starting to compiling & executing anything, lets take a look at runnr.conf file present at:-
```bash
Windows: C:\Users\<user-name>\runnr.conf
Unix-like: ~\.config\runnr.conf
```

>If config file is not present the try running: runnr --version

This runnr.conf is the main config file that runnr use to execute commands based on file-extension. Once the configuration is set for any file-extension runnr can execute and run it without any problem. As runnr is a config file based tool, it is very easy to use the same config file in different system only after setting it up once.

- ### Syntax of the config file:

```
(<extension>) :: <arguemnt1> = "<parameter1>",  <arguemnt2> = "<parameter2>", ....
```
All `<argument> = <parameter>` are separateed using ','. You can even comment in this config file using '#' and white Spaces are ignored automatically.

- Example:

```
#for adding support for .c files, we simply can write:-
(.c) :: COMPILER = "gcc", OUTPUT_FILENAME="$FILE"
```

The extension must be enclosed withing parenthese: "()". Then the respective arguments & parameters are writen after using argument separator: "::". The arguments must be separated using "," and every argument must have its value/parameter enclosed withing double qoutes: "".

- ## Supported Arguments:
As of version: v0.2.0 suppported aruments are:

```
1. COMPILER="<compiler-name>"
2. INTERPRETER="<interpreter-name>"
3. USE=<cli-program> : It is used for special arguments like "-open"
4. OUTPUT_FILENAME=<variables or name> : It is used for setting special output name.
```

- ### Output Name Values:
```
$FILE : It sets the output name to be same as input file name but without the extension.
$NONE : It is mostly used for interpreter based languages, as those don't have any compiled file.
        Using $NONE on compiled based languages, turns off generation of any custom output file.

<any-custom-name> : Creates an output file with the given name.
```
- Examples:
```
#for javascript
(.js)::INTERPRETER="node", OUTPUT_FILENAME="$NONE"
```

For interpreter based languages, it is optional to set "OUTPUT_FILENAME" argument.

- ## CLI Tool:
Now lets see how to interact with the runnr tool :- 

First lets see if it installed or not? : Simply Type-
```bash
$ runnr --version
v0.x.x
```

>If any error occurs then install runnr first.
>If it prompts to create config file, enter "Y". Then retry with the command.

Now if it is installed correctly, lets proceed with its usages:-

- ### Comiling or Interpreting a file:
runnr can compile or interpret different programs based on extensions from "runnr.conf" file. Now lets see some examples. Suppose we have "hello.py" & "hello.cpp" file with "Hello, World" printing program.

Then to run this files:
``` bash
$ runnr hello.py
Hello, World
```


```bash
$ runnr hello.cpp
Hello, World
```

It can execute different files based on .conf file.
* It is important to note that the file that is being compiled/interpreted must be the last argument, after any options.

- ### Only compiling not executing:
We can make runnr to only compile a programs but not execute it by using '-run' option.

Example:
```bash
$ runnr -run N hello.cpp
```

It outputs nothing as we set running after compilation to off. It just generates the binary executable file.

This option only works for compiled based programs like C, C++, rust. The "-run" option's parameter can be either "Y" or "N".

- ### Custom output file name for Compiled programs:

We can make runnr to output the compiled executable file-name as we want it to be instead of default set value from config.

Examples:
```bash
$ runnr -run N -out helloworld hello.cpp
$ ./helloworld
Hello, World
```
>Yes, we can use these different options and parameters all together.
So, "-out" option takes only one parameter that is the file name of the output file.

- ### More compiler arguments - 1:
There may be some cases where we need to pass more compiler arguemnts to compile it. For example, in C++ we might need to tell the compiler to use C++11, as we have used 'auto' data-type in out program. 

This can be achieved by two ways:

- Parmanent:
Modifying the "runnr.conf" file for ".cpp" extension.

Examples:
```
#this will use C++11 std library
(.cpp)::COMPILER="g++ -std=c++11", OUTPUT_FILENAME="a.out"
```

- Temporary:
For single file use cases.

Examples:
```bash
$ runnr -param "-std=c++11" -out helloworld hello.cpp
```

"-param" takes the compiler arguemnt and directly pass it to the compiler. It is also a good practice to wrap them in "".

- ### More compiler arguments - 2:
While building a project we might use many libraries to make our task easy. For this in C/C++ we might need to specify the libraries(staic/dynamic) to compiler to link to while compiling. This can be achieved using "-link" option. "-link" option allows us to pass the neccessary library names to the compiler. "-link" option automatially adds "-l" to the library name so we only need to specify the library name. 

For example I am building a program in C++ which uses fmt library.

Example:
```bash
$ runnr -debug -link fmt hello.cpp
runnr: debug: config: using config from "/home/aniket/.config/runnr.conf"
runnr: debug: executed: "g++ hello.cpp -o hello -lfmt"
runnr: debug: run: "./hello"
Hello, World!
```

There might be some cases where you want to link multiple libraries at once. For that we can use:

```bash
$ runnr -debug -lf -link "-lfmt -lm" hello.cpp
runnr: debug: config: using config from "/home/aniket/.config/runnr.conf"
runnr: debug: executed: "g++ hello.cpp -o hello -lfmt -lm"
runnr: debug: run: "./hello"
Hello, World!
```

"-lf" option disables the automatic addition of "-l" and passes the "-link" arguments directly to the compiler.

- ### Execuable file's command-line arguemnts:
You might write some programs that takes command line arguments directly, as runnr can compile and execute simultaneously, you might want to pass the necessary arguments to the program. This can be achieved by using "-args".

Suppose we have written a program which takes 2 number directly from command line like "./a.exe 5 7" & outputs its sum. Lets see how to do that with runnr.

Examples:

```bash
$ runnr -args "5 7" sum_2_no.c
12
```

Again it is necessary to wrap the arguments within "" as it containes spaces.

- ### Executing multiple files at once:
Multiple different or same files can be executed simultaneously using "-files" option.

```bash
$ runnr -run N -files hello.c hello.py hello.cpp sum.c
```

- By default all the input files gets executed. Use `-run N` to turn it off for compiled based language.
- If any custom output file-name in set in the config or by using `-out` option, it will be ignored and the executable output name will be same as of the file-name without the extension.
- After "-files" option all the arguments must be files.
- For using "-args" option, all the executable will recieve same command-line argument.
- "-param" option is ignored while using "-files", otherwise it will result in passing of same compiler/interpreter parameter to different compiler/interpreter. It is recommended to set these parameter options in config-file instead.
- Opening of multiple files using "-open" isn't implemented yet.

- ### Current-Working-Directory specific config files:

When building a project with multiple files, it may be required to use some certian version specific tools, compilers, interpreters. Managing them globally throughout the system
with different projects becomes challenging. To tackle this problem Directory specific runnr-config files can be created which can have different version tools, compilers & interpreters from the rest of the system.

runnr from and after `v0.3.0` first checks if a config file exists in current working directory or not. If exists then runnr uses that config file else it uses the set/default config file.

To initialize a directory specific config file in runnr use "init" or "-i" option:

```bash
$ runnr init
$ runnr -i
```

This will create a empty config file in the directory it was initialized from. Now add all the configs you need to this new config file which will only work for this directory.

- -default:

Sometimes you might want to use configs from your set/default config file instead of the working-directory one. Use "-default" or "-d" option for that:

```bash
$ runnr -default ...args <file>
```

- "-default" option must be specified first before any other option or files.

- ### Setting and reseting config file path:

- Set Path:
runnr allows developers to set a custom config file to load configs from.

For setting custom config file name use "--set-path" option, it takes `<full-path>` as argument.

```bash
$ runnr --set-path "/Users/aniket/Desktop/myConfig.conf"
```

- Reset Path:
For reseting the config file path to default "runnr.conf" use "--remove-path" option.

```bash
$ runnr --remove-path
```

- Reset Path & Data:
For reseting the config file path to default "runnr.conf" with its default configurtaions data use "--reset-config" option.

```bash
$ runnr --reset-config
```

- ### Debug:

Sometimes developers need to see what is actually getting executed by runnr to find any error or mis-compilation of programs & executions. To solve this a particular option is to be used called "-debug".

Examples:
```bash
$ runnr -debug -out helloworld -param "-std=c++11" hello.cpp
runnr: debug: config: using config from /Users/aniket/.config/runnr.conf
runnr: debug: executed: g++ -std=c++11 -o helloworld hello.cpp
runnr: debug: run: ./helloworld
Hello, World
```

Using the "-debug" gives a detailed output of the underneath commands execution.

- ### Version:
To check the version of runnr:

```bash
$ runnr --version
v0.x.x
$ runnr -V
v0.x.x
```

- ### Help:

```bash
$ runnr --help
$ runnr -h
```

- ### Update:
Update runnr using `--update or -U` option. It uses pip to update itself.
```bash
$ runnr --update
$ runnr -U
```

# VERSION:
- Version rule :: `<major>.<minor>.<patches>`
>v0.3.0

# What's New in this Update:
>0.3 update is focused arround improving the runnr, config file support and its options with bug fixes.

1. Added support for changing the config file path using `PATH="<path>"` enviorment variable in default runnr.conf file. {This variable should be mentioned at the line number: 1}
2. Added "--config" option to show current default config file directory.
3. Added "--reset-config" option to reset default config file to its default values by erasing all configurations.
4. Added "--set-path" option to change config file directory to any other location. {Instead of manually adding the PATH in config file}
5. Added "--remove-path" option to remove custom added path to default.
6. Added "init" or "-i" option to create config file in current-working-directory.
7. Added "-default" or "-d" option to use default config file instead of current-working-directory.
8. Added "-link" option to link to libaries for C and C++ ["-link" option adds "-l" automatically] {Linking libaries using "-param" is deprecated as modern compilers takes liabries names as last argument.}
9. Added "-lf" option to stop auto addition of "-l" while using "-link".
10. Fixed the bug in config, where parser didn't checked wheter config-variables starting with "$" are correctly named or not for "OUTPUT_NAME".
11. Fixed the bug for compiled languages where runnr didn't checked if "OUTPUT_FILENAME" was declared or not.
12. Fixed the bug where "-param" caused the command execution to break due to no space separation. 
13. Updated "--help" option for new config options.
14. Removed unnecessary file "MANIFEST.in".