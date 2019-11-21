# Documentation

## Requirements
- Python 3.6+
- Git
- Internet connection

---

## Setting up the environment
*This step is not required but it's recommended to avoid altering the original `Python` installation*

### Special instructions if using an IDE other than PyCharm
- You should create a virtual environment in the directory where you'll clone the project. 
- `venv` is already installed with python 3, so there's no need to install it.
- Create the virtual environment

*On windows*
``` python
python -m venv env
```
*macOS or Linux*
``` python
python3 -m venv env
```

- Activate the virtual environment

##### *Note: You must activate the virtual environment before running the app, otherwise the packages will not be available.*

***On windows***
``` python
.\env\Scripts\activate
```
*macOS or Linux*
``` python
source env/bin/activate
```
- Deactivating the virtual environment
``` python
deactivate
```

---

## Installing & Running The App
- Before starting, signup and get an app token at the [Prince George's County Data site](https://data.princegeorgescountymd.gov/signup)
- Once you're in the correct directory, clone the repo
``` python
git clone https://github.com/BDubon/PGCountyDataApp.git
```

- Install the dependencies
``` python
pip install -r requirements.txt
```
*macOS computers*
``` python
pip3 install -r requirements.txt
```
- In the [DataMain Folder](DataMain), create a file called `credentials.py`

- Add your login info and app token to the [credentials.py file](DataMain/credentials.py) using the following code:
```python
APPTOKEN = 'Your App Token'
USERNAME = 'Your Login Email'
PASSWORD = 'Your Password'
```
- Make sure this file is in your [`.gitignore`](.gitignore) to avoid making your credentials public


- To run the app, use the following command:
``` python
python manage.py runserver
```
