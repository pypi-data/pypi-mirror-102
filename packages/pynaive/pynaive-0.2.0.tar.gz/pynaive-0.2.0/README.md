# pynaive
A toy project to demonstrate Python development environment and toolchain.

The script `tools/docker.sh` creates, runs and executes a docker container for
developing the project. The script `tools/full_check.sh` runs style checkes,
linters and tests. The project can be built with
`python3 setup.py sdist bdist_wheel` command.
```
host> cd <project_root_dir>
host> ./tools/docker.sh
pynaive_focal
container> ./tools/full_check.sh
Success: no issues found in 2 source files

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

========================= test session starts ==========================
platform linux -- Python 3.8.5, pytest-4.6.9, py-1.8.1, pluggy-0.13.0
rootdir: /pynaive
plugins: flake8-1.0.6
collected 7 items

tests/test_math.py .......                                       [100%]

======================= 7 passed in 0.03 seconds =======================
container> python3 setup.py sdist bdist_wheel
<lots_of_output_here>
container> twine check dist/*
container> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
container> twine upload dist/*
```

## Instanllation
Exectute the following in the command line:
```
shell> pip3 install pynaive
```

## Example
The simplest snippet which uses the package:
```
shell> python3
>>> from naive.math import average
>>> average([2.5, 0.0, -1.0, 3.5])
1.25
>>>
```
