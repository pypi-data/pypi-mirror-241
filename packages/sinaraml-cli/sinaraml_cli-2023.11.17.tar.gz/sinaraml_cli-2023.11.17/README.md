# Description
This a SinaraML CLI library which contains main module for launching CLI commands. It also needs plugin packages to work.

# CLI Installation
Linux / WSL:
```
sudo pip install sinaraml_cli
```

Windows:
```
pip install sinaraml_cli
```

# Plugins installation
Linux / WSL:
```
sudo pip install sinaraml_cli_host
sudo pip install sinaraml_cli_jupyter
```

Windows:
```
pip install sinaraml_cli_host
pip install sinaraml_cli_jupyter
```

# CLI Quick Start
Commands start with the keyword sinara (similar to git, docker, kubectl)<br>
If a command call is made without a mandatory parameter, help is displayed on the available parameters and methods of calling the command, for example:

```
~$ sinara
usage: sinara [-h] {server,model} ...

options:
  -h, --help            show this help message and exit

subject:
  {server,model,pipeline}
                        subject to use [server, model, pipeline]
    server              server subject
    model               model subject
    pipeline            pipeline subject
```

```
~$ sinara server
usage: sinara server [-h] {create,start} ...

options:
  -h, --help      show this help message and exit

action:
  {create,start}  Action to do with subject [create, start, stop, etc]
    create        create action
    start         start action
```