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
exit # this will exit the venv, so you can move onto the next question. Do not use `deactivate` as this leave pipenv in a confused state
```