Before running any script in this test project we need to make sure python is installed correctly. You may have python installed as a user or an admin. All packages should be installed in your user version of python. Run the following commands:

```bash
python --version  # Should be 3.11 or higher
pip install --upgrade pip
pip --version # Should be 23.0.0 or higher
pip install pipenv
```

To create the venv and piplock file run `pipenv install`. This will install all of the packages necessary to run the question for you. 
`pipenv shell` will activate the venv and all subsequent commands will be run inside the venv unless deactivated. E.g. pip install will install directly into the venv

some available commands are:

```bash
python myscript.py  # will now run inside the venv
pytest # w
```


To run any file in this directory, run:

```bash
pipenv install # to install the venv
pipenv sync # to install packages to the venv
pipenv shell # to activate the venv
pipenv run python myscript.py # to run the script "inside" the venv with all of the installed dependencies
```


if you do not have the right python version (check with `python --version` and `pipenv run python --version`) then try this in an elevated shell
```bash
python -m pip install --upgrade pip
pipenv --rm
pipenv install
```