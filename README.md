# Documentation

## Requirements
- Python 3.6+
- Git
- Internet connection

## Setting up the environment
*This step is not required but it's recommended to avoid altering the original `Python` installation*

### Special instructions if using an IDE other than PyCharm
- You should create a vritual environment in the directory where you'll clone the project. 
- Install `virtualenv` to manage installed packages

***On windows***
```
python -m pip install --user virtualenv
```
***macOS or Linux***
```
python3 -m pip install --user virtualenv
```
- Create the virtual environment

***On windows***
```
python -m venv env
```
***macOS or Linux***
```
python3 -m venv env
```

- Activate the virtual environment

##### *Note: You must activate the virtual environment before running the app, otherwise the packages will not be available.*

***On windows***
```
.\env\Scripts\activate
```
***macOS or Linux***
```
source env/bin/activate
```
- Deactivating the virtual environment
```
deactivate
```

## Installing & Running The App
- Once you're in the correct directory, clone the repo
```
git clone https://github.com/BDubon/PGCountyDataApp.git
```

- Install the dependencies
```
pip install -r requirements.txt
```
***macOS computers***
```
pip3 install -r requirements.txt
```

- To run the app run the following command
```
python manage.py runserver
```
