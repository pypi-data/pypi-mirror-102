# Gask 

## Technical documentation

* [Commands](gask/commands/commands.md)
* [FileUtils](gask/fileutils/fileutils.md)
* [GitTools](gask/gittools/gittools.md)
* [Start](gask/start/start.md)
* [TaskUtils](gask/taskutils/taskutils.md)

## Concept 
The idea of this project is to create a terminal task manager 
in the vein of software such as taskwarrior. 

The difference here is to use a git repository as a backend, 
to store the tasks and share tasks between users/devices. 

The software will be written in python, installable using pip 
and should be able to run in the Windows command prompt, the 
Mac OS terminal and the linux terminal, although the focus
will be in the linux terminal. 

## Installation

For now, this software can only be installed using pip. 

You can install the it using the command

`pip install gask`

## Basic Usage

When the `gask` command is first given, the program will invite you
to create a taskspace, where the repository and relevant files are stored. 

You can add a task using:

`gask add <description_of_task>`

You can show the current tasks using:

`gask list`

You can mark a task as complete using:

`gask complete`

For more information about commands, check [here](gask/commands/commands.md).