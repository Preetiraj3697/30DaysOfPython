
# Install
1. Go to [Website](https://www.python.org)
 <img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/installing_on_macOS.png" alt="python website">

 - # Some time you facing this issue
  ### python was not found; run without arguments to install from the microsoft store, or disable this shortcut from settings > manage app execution aliases.

For most people, the simple fix is to install Python from the official Python website and check the "Add Python to environment variables" option during installation.

Step 1: Locate Your Python Installation Paths


Step 2: Access and set the path Environment Variables
 
 search for "Environment Variables" in Windows search as shown below:
 <img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step-1-search-for-environment-variables.png" alt="environment">

 Navigate to the System Properties, and then click on the "Environment Variables" button.

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step2-system-properties.png" alt="environment">

Step 3: Modify the System Variables

Click on the "System variables" and then click "Path" as shown below

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step3-system-variable.png" alt="environment">

After you select the "Path" variable, click "Edit."

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step4-edit-system-variable.png" alt="environment">

Click "New" and then Add the previously copied Python paths to the list.

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/step-5-click-new.png" alt="environment">

This is what it will look like:

<img src="https://cwh-full-next-space.fra1.cdn.digitaloceanspaces.com/blogpost/solving-python-not-found/edit-environment-variable-dialogue.png" alt="environment">

Note: The key to solving this issue lies in adding the Python paths to the System variables, not the User variables. I initially made the mistake of using the User variables, which led to another error. Hence, I want to make sure you do not repeat the mistake I did!

To check if python is installed write the following command on your device terminal.

```
python --version  
``` 
<img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/python_versio.png" alt="cmd">


# Python Shell
Python is an interpreted scripting language, so it does not need to be compiled. It means it executes the code line by line. Python comes with a Python Shell (Python Interactive Shell). It is used to execute a single python command and get the result.

Python Shell waits for the Python code from the user. When you enter the code, it interprets the code and shows the result in the next line. Open your terminal or command prompt(cmd) and write:
```
python
```
<img src="https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/images/adding_on_python_shell.png" alt="shell">