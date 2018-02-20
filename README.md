# Functional Python

Here I am going to document what I can learn about functional programing in python under one single week.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

I do not work here in a NEW virtualbox or Docker environment.
As a home project I just Use my default ubuntu 16.04 what is obviously not that default because I am using conda environment git and som other stuff. 


### Prerequisites

I am using sublime text with anaconda
In sublime i use the conda environment for building
Take a look at lines in my 
```
~/$USER/.config/sublime-text-3/Packages/User/funpy.sublime-build
```

```
{
    "cmd": ["/home/$USER/.conda/envs/funpy/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
```