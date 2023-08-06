# cmdtools
[![tests](https://github.com/HugeBrain16/cmdtools/actions/workflows/python-package.yml/badge.svg)](https://github.com/HugeBrain16/cmdtools/actions/workflows/python-package.yml)
  
a module for parsing and processing commands.
  
## Installation
to install this module you can use the methods below 
  
- using pip: 
    + from pypi: `pip install cmdtools-py`  
    + from github repository: `pip install git+https://github.com/HugeBrain16/cmdtools.git`  
  
- from source: `python setup.py install`  
  
## Examples
Basic example
```py
import cmdtools

def ping(raw_args, args):
    print("pong.")

_cmd = cmdtools.Cmd('/ping')
_cmd.parse()

cmdtools.ProcessCmd(_cmd, ping)
```
  
Parse command with arguments
```py
import cmdtools

def greet(raw_args, args):
    print(f"Hello, {greet.name}, nice to meet you")

_cmd = cmdtools.Cmd('/greet "Josh"')
_cmd.parse()

cmdtools.ProcessCmd(_cmd, greet,
    attr= { # assign attributes to the callback
        'name': _cmd.args[0]
    }
)
```
  
Parsing command with more than one argument and different data types
```py
import cmdtools

def give(raw_args, args):
    print(f"You gave {give.item_amount} {give.item_name}s to {give.name}")

_cmd = cmdtools.Cmd('/give "Josh" "Apple" 10')
_cmd.parse(eval=True) # we're going to use `MatchArgs` function which only supported for `eval` parsed command arguments

# check command
if cmdtools.MatchArgs(_cmd, 'ssi', max_args=3): # format indicates ['str','str','int'], only match 3 arguments
    cmdtools.ProcessCmd(_cmd, give,
        attr={
            'name': _cmd.args[0],
            'item_name': _cmd.args[1],
            'item_amount': _cmd.args[2]
        }
    )
else:
    print('Correct Usage: /give <name: [str]> <item-name: [str]> <item-amount: [int]>')
```