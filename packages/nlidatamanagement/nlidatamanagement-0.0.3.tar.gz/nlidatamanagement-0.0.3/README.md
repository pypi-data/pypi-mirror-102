
# Uploading tagged data to Girder and Zotero using a GUI

## Getting Started
### Prerequisites

#### 1. Install python3
Any python above 3.6 should be fine. Python 3.8 is recommended. You can install python3 from one of the following:
-   Download from the python official website [here](https://www.python.org/downloads/).
-   Install python3 using brew if you are using macOS ```
brew install python@3.8```
- Install python3 using `pyenv`. See [here](https://github.com/pyenv/pyenv#basic-github-checkout).

---
**NOTE**

If you used ```pyenv``` to install Python on a Mac, ```tkinter``` might not be integrated by default. To install ```tkinter``` lib, you have to first uninstall your current python (if python is already installed), then reinstall it with:
```
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl8.6 -ltk8.6'" 
pyenv install {your python version}
```
---


#### 2. Create Girder API key

A Girder API Key is needed in order to Login the Girder System.

1. Login [NutritionalLungImmunity](https://data.nutritionallungimmunity.org/). Create an account if you don't have one.
2. Click your username on the top right -> MyAccount -> API Keys Tab -> Create new key. **Keep this key private!**

#### 3. Create a Zotero API Key (optional)

If you want to attach Zotero Item with the tag list from Girder, a Zotero API Key is needed.

1. Login [Zotero](https://www.zotero.org/ ). Go to [account setting page](https://www.zotero.org/settings/keys).
2. Click `Create new private key`.
3. Under `Personal Library`, check all options. Under `Default Group Permissions`, select `Read/Write`. Then click `Save key`.
4. **Mark down the pop-up API key.** Save it in a safe place.

### Installation

1. Install the virtual environment package

     ```python3 -m pip install virtualenv``` (on Windows add `.exe` to `python3`)
     
   If you have trouble with permission issues installing any packages system-wide, you may have more luck by installing them as user-local packages:
   
   ```python3 -m pip install --user virtualenv``` 

1. Create and move to a directory where you want to keep the virtual environment
   
   ```mkdir my-nlidatamanagement; cd my-nlidatamanagement```
   
1. Create a virtual environment

    ```virtualenv -p python3 venv``` (on Windows add `.exe` to `virtualenv`)
   
1. Enter the virtual environment:

    ```. venv/bin/activate```
    
    on Windows: ```.\venv\bin\activate.bat```
    
1. Install the uploader into the virtual environment

    ```python3 -m pip install nlidatamanagement```

1. Launching the uploader

    ```nli_data_management```
    
    
Note: To re-launch the program, perform steps 4 and 6. 

Note 2: The virtual environment is optional and serves to simplify potential package dependency problems. If you wish to install the uploader outside the virtual environment, only the last two steps are required. Re-launch is done via step 6. 

To update the tool to a new version, enter the virtual environment and run 

```python3 -m pip install --upgrade nlidatamanagement```

### Initialize Connection

#### Connect to Girder

1. Click `Upload to Girder` and a new setting window will pop up.
2. Under  `Add new Girder instance`:
    * Give the new Girder instance a name.
    * For `Host`, type `data.nutritionallungimmunity.org `
    * Copy and paste your Girder API Key in the `API Key`
3. Click the `add` button
4. Select the new added Girder instance and click `Connect`

#### Connect to Zotero

1. Click `Upload to Zotero`
2. Add a new Girder Instance, if you haven't done it yet.
3. Under `Add new zotero Instance`:
    * Give the new Zotero instance a name.
    * For `Library ID`, type `2345225`
    * For `Library Type`, type `group`
    * Copy and paste your Zotero API Key in the `API Key`
4. Click the `add` button
5. Select both Girder instance and Zotero instance. Click `Connect`
