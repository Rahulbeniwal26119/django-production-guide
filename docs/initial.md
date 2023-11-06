Hi

## Project Structure
```.
├── docs
└── src
```

1) docs will contains All readme and documentation.
2) src will contain all source code for django application

### Inside src
```
src/
├── manage.py
├── requirements
├── simple_medium_clone
└── venv
```
1) requirements dir contains different requirements file diffrent environments

### Inside requirements

```requirements/
├── base.txt
├── local.txt
└── production.txt
```
base.txt will contains common dependencies

### How to use dependency inheritance
Inside requirement file use <i>-r filename</i> to include all dependencies of <i>filename</i> into file.

```
-r base.txt
```

### Create gitignore file
```npx gitignore python```
This will generate .gitignore file for Python projects
