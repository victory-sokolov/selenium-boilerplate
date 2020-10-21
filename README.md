# Selenium Boilerplate for automation

### Installation

Cookiecutter allows interactively to set up your project
```code
pip3 install cookiecutter
cookiecutter https://github.com/victory-sokolov/selenium-boilerplate.git
```

### Build single executable file 

```
pyinstaller main.py -F --onefile -n <FileName>
```

### Create executable using Make
```
make compile file="main.py" name="OutputFile"
```
