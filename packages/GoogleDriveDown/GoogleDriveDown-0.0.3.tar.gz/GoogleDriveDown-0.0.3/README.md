This module allows you to download all the content from a shared google drive url to specified directory.

# Requirements:<br/>
* "client_secrets.json" file which is required for integration of Python with Google Drive
    *   You can follow [this](https://medium.com/swlh/google-drive-api-with-python-part-i-set-up-credentials-1f729cb0372b) blog to      generate client secrets file.

* Make sure that your client_secrets.json file and python file must be in same directory.

# Installation using pip:<br/>
```
   pip install GoogleDriveDown 
```

# Code Example:<br/>
```
    import GoogleDriveDown as gd

    url = 'https://drive.google.com/drive/folders/1NIGvjHBuUQHWnMqzboyg-zLI1q_bOuCH'
    gd.get_files(url, 'save to directory(directory name)')
```
