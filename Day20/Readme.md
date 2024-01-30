# Python PIP - Python Package Manager
### What is PIP ?
PIP stands for Preferred installer program. We use pip to install different python packages. Package is a python module that can contain one or more modules or other package. IN programming, we do not have to write every utility program instead we install packages and import them to our applications.

# Installing PIP
if you did not install pip, let us install it now. Go to your terminal or command prompt and copy and paste this:
```sh
pip install pip
```
Check if pip is instal by writing
```sh
pip --version
```
```sh
pip 23.2.1 from C:\Users\preet\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)
```

As you can see, I am using pip version 23.2.1, if you see some number a bit below or above that, means you have pip installed.

# installing package using pip
Let us try to install numpy, called numeric python. It is one of the most popular packages in machine learning and data science community.
- NumPy is the fundamental package for scientific computing with python. It contains among other things:
   - a powerful N-dimensional array object
   - sophisticated (broadcasting) functions
   - tools for integrating c/c++ and Fortran code
   - useful linear algebra, Fourier transform, and random number capabilities

```sh
pip install numpy
```
Let us start using numpy. Open your python interactive shell, write python and then import numpy as follows:
```py
PS C:\Users\preet> python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.26.3'
>>> lst = [1,2,3,4,5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr*2
array([ 2,  4,  6,  8, 10])
>>> np_arr+2
array([3, 4, 5, 6, 7])
>>>
```
Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the python programming language. Let us install the big brother of numpy, pandas:
```sh
pip install pandas
```
```sh
PS C:\Users\preet> python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```
This section is not about numpy nor pandas, here we are trying to learn how to install packages and how to import them. if it is needed, we will talk about different packages in other sections.
Let us import a web browser module, which can help us to open any website. We do not need to install this module, it is already by default with python 3. For instance if you like to open any number of websites at any time or if you like to schedule something, this webbrowser module can be used.
```py
import webbrowser

url_lists = [
    'http://www.python.org',
    'https://github.com/Preetiraj3697',
    'https://www.linkedin.com/in/preetiraj3697/',
    'https://www.google.com'
    
]

# Opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)

```
### Uninstalling Packages
if you do not like to keep the installed packages, you can remove them using the following command.
```py
pip uninstall packagename
```
### List of packages
to see the installed packages on our machine. We can use pip followed by list.
```py
pip list
```
```sh
PS C:\Users\preet\OneDrive\Desktop\Python> pip list
Package         Version
--------------- ----------
click           8.1.7
colorama        0.4.6
joblib          1.3.2
nltk            3.8.1
numpy           1.26.3
pandas          2.2.0
pip             23.2.1
python-dateutil 2.8.2
pytz            2023.4
regex           2023.12.25
scikit-learn    1.4.0
scipy           1.12.0
six             1.16.0
threadpoolctl   3.2.0
tqdm            4.66.1
tzdata          2023.4

[notice] A new release of pip is available: 23.2.1 -> 23.3.2
[notice] To update, run: python.exe -m pip install --upgrade pip
```
### Show Package
To show information about a package
```py
pip show packagename
```
```sh
PS C:\Users\preet> pip show click
Name: click
Version: 8.1.7
Summary: Composable command line interface toolkit
Home-page: https://palletsprojects.com/p/click/
Author:
Author-email:
License: BSD-3-Clause
Location: C:\Users\preet\AppData\Local\Programs\Python\Python312\Lib\site-packages
Requires: colorama
Required-by: nltk
```
if we want even more details, just add --verbose
```sh
PS C:\Users\preet> pip show --verbose click
Name: click
Version: 8.1.7
Summary: Composable command line interface toolkit
Home-page: https://palletsprojects.com/p/click/
Author:
Author-email:
License: BSD-3-Clause
Location: C:\Users\preet\AppData\Local\Programs\Python\Python312\Lib\site-packages
Requires: colorama
Required-by: nltk
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Intended Audience :: Developers
  License :: OSI Approved :: BSD License
  Operating System :: OS Independent
  Programming Language :: Python
Entry-points:
Project-URLs:
  Donate, https://palletsprojects.com/donate
  Documentation, https://click.palletsprojects.com/
  Changes, https://click.palletsprojects.com/changes/
  Source Code, https://github.com/pallets/click/
  Issue Tracker, https://github.com/pallets/click/issues/
  Chat, https://discord.gg/pallets
```
### PIP Freeze
Generate installed python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed python packages in a python project.
```sh
PS C:\Users\preet> pip freeze
click==8.1.7
colorama==0.4.6
joblib==1.3.2
nltk==3.8.1
numpy==1.26.3
pandas==2.2.0
python-dateutil==2.8.2
pytz==2023.4
regex==2023.12.25
scikit-learn==1.4.0
scipy==1.12.0
six==1.16.0
threadpoolctl==3.2.0
tqdm==4.66.1
tzdata==2023.4
```
The pip freeze gave us the packags used, installed and their version. We use it with requirements.txt file for deployment.

### Reading from URL
By now you are familiar with how to read or write on a file located on you local machine. Sometimes, we would like to read from a website using url or form an API. API stands for application program interface. It is a means to exchange structured data between servers primarily as json data. To open  a network connection and to implement CRUD(create,read,update and delete) operations. In this section, we will cover only reading or getting part of CRUD.
let us install requests:
```sh
pip install requests
```
We will see get, status_code, headers, text and json methods in requests module:
- get(): to open a network and fetch data from url - it returns a response object.
- status_code: After we fetched data, we can check the status of the operation (success,error,etc)
- headers: To check the header types
- text: to extract the text from the fetched response object
- json: to extract json data let's read a txt file from this website,
  'https://www.w3.org/TR/PNG/iso_8859-1.txt'.

```py
import requests

url = 'https://api.ynos.in/collections/top-startups?page=0&N=10'
response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
```

- Let us read from an API. API stands for Application Program Interface. It is a means to exchange structure data between servers primarily a json data. An example of an API: https://restcountries.com/v3.1/all. Let us read this API using requests module.
```py
import requests
url = 'https://restcountries.com/v3.1/all'
res = requests.get(url)
print(res)
print(res.status_code)
countries = res.json()
print(countries[:1])
```
```sh
<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```
we use json() method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use text.
### Creating a Package
We organize a large number of files in different folders and sub-folders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiply objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. let us create a package named mypackage, using the following steps:
Create a new folder name mypackage inside python folder create an empty init.py file in the mypackage folder. Create module arithmetic.py and greet.py with following code:
```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```
```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```
The folder structure of your package should look like this:
```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```
Now let's open the python interactive shell and try the package we have created:
```sh
PS C:\Users\preet\OneDrive\Desktop\Python> python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1,2,3,4,5)
15
>>> arithmetics.subtract(6,3)
3
>>> arithmetics.division(6,3)
2.0
>>> arithmetics.remainder(5,3)
2
>>> arithmetics.multiple(5,3)
15
>>> arithmetics.power(5,3)
125
>>> from mypackage import greet
>>> greet.greet_person('Paarthav','Shah')
'Paarthav Shah, welcome to 30DaysOfPython Challenge!'
>>>
```
As you can see our package works perfectly. The package folder contains a special file called init.py - it stores the package's content. if we put init.py in the package folder, python start recognizes it as a package. The init.py exposes specified resources from its modules to be imported to other python files. An empty init.py file makes all functions available when a package is imported. The init.py is essential for the folder to be recognized by Python as a package.

# Further Information About Packages
- Database
  - SQLAlchemy or SQLObject - Object oriented access to several different database systems
  - pip install SQLAlchemy
- Web Development
  - Django = High-level web framework.
  - pip install django
  - Flask = micro framework for python based on Werkzeug, Jinja 2. (It's BSD licensed)
  - pip install flask
- HTML Parser
  - Beautiful Soup = HTML/XML parser designed for quick turnaround projects like screen-scrapping, will accept bad markup.
  - pip install beautifulsoup4
  - PyQuery - Implement jQuery in python; faster than BeautifulSoup, apparently.
- XML Processing
  - ElementTree = The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the standard Library.
- GUI
  - PyQt - Bindings for the cross-platform Qt framework.
  - Tklnter - The traditional Python user interface toolkit.
- Data Analysis, Data Science and Machine Learning
  - Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
  - Pandas - is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
  - SciPy - Scipy is a machine learning library for application developer and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
  - TensorFlow: is a machine learning library built by Google.
  - Keras: is considered as one of the coolest machines learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
  
- Network:
  -  requests: is a packages which we can use to send requests to a server(GET,POST,DELETE,PUT)
  -  pip install requests