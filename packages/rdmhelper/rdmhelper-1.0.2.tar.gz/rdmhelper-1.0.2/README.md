# Installing

```
pip install rdmhelper
```

# Seafile 

API documentation: https://download.seafile.com/published/web-api/home.md

## Usage

```python
from rdmhelper.keeper import Seafile
sf = Seafile(
    server=server, 
    username=username, 
    password=password)
```

### View Account details

```python
sf.account_info()
```

### List repositories
Seafile is organized in repositories. You need to pass a reposirory id to most functions

```python
sf.repo_list()
repo = sf.repo_list()[0].get('id')
```

### Make dir 

```python
 resp = sf.folder_create(repo, 'testfolder')
```

### Upload Folder

add_date=True will append the current date to the name of the uploaded folder.
add_date_recursive = True will append the current date to all files in the uploaded folder and subfolders.

```python
sf.folder_upload(
    repo, 
    local_dir='data/',
    remote_dir='/testfolder',
    add_date=True,
    add_date_recursive=False
)
```

### List folder content

```python
content_json = sf.folder_list_content(repo, '/testfolder')
```

### Show Folder Detail

```python
detail_json = sf.folder_detail(repo, 'testfolder/data_2021_07_14/subfolder')
```

### Delete folder

```python
resp = sf.folder_delete(repo, 'testfolder2')
```

### Rename folder

```python
sf.folder_rename(repo, path='testfolder/data_2021_07_14/subfolder', new_name='subfolder_renamed')
```

### Download folder

```python
sf.folder_download(repo, remote_dir='testfolder/data_2021_07_14/subfolder', local_dir='downloads')
```

### Share repository

```python
resp = sf.repo_share(repo, userlist=['hbenne@gmx.at', 'existiertnicht@gmail.com'], permissions='rw')
```

Revoke permissions:
```python
resp = sf.repo_unshare(repo, user='hbenne@gmx.at')
```

### Show file details

```python
sf.file_info(repo, file='/testfolder/data_2021_07_14/test.csv')
```

### Search file

```python
results_json = sf.file_search(repo,file='data.txt')
```

### Read file


```python
import pandas as pd
url = sf.downloadlink(repo, '/testfolder/data_2021_07_14/test.csv')
df = pd.read_csv(url)
print(df.head())
```

If the example above does not run on your mac have a look at: 
https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org


### Download file

```python
sf.file_download(repo, file='/testfolder/data_2021_07_14/test.csv', local_dir='downloads/data/')
```

### Delete file

```python
resp = sf.file_delete(repo, file='/testfolder/data_2021_07_14/test.csv')
```

# Nextcloud

API documentation: https://docs.nextcloud.com/server/latest/developer_manual/client_apis/index.html

## App password

It is recommended not to use your login password. 
You can create app specific passwords: Settings -> security -> new app password.

## Usage

```python
from rdmhelper.nextcloud import Nextcloud
cloud = Nextcloud(
    server='https://SERVERNAME/remote.php/dav/files/',
    username=USERNAME, 
    password=PASSWORD, 
    webdav_token=WEBDAV_TOKEN
    )
```

In the official nextcloud documentation the webdav_token is referred to as "username". But it is different from the login name and can be found in settings -> WebDAV. 

### List files/folders

list root directory
```python
cloud.list('')
```

list https://SERVERNAME/apps/files/?dir=/WebdavTest/subfolder
```python
cloud.list_dir('WebdavTest/subfolder')
```

### Make Dir

Create directory named New in WebdavTest

```python
cloud.make_dir('WebdavTest/neu')
```

### Upload file

Upload Datei.md from the local dir data/ to WebdavTest/subfolder.
If add_date is True a timestamp will be added to the filename.

```python
cloud.upload_file(
    local_file='data/Datei.md', 
    path='WebdavTest/subfolder', 
    filename='Datei1.md',
    add_date=True
    )
```

### Upload folder

Upload the local folder ./Testfolder into the WebdavTest folder on Nextcloud.
Add a timestamp to the foldername if add_date is True.
Add a timestamp to all files in the folder if add_date_recursive is True.

```python
cloud.upload_folder(
    local_folder='Testfolder', 
    target_folder='WebdavTest', 
    add_date=True, 
    add_date_recursive=False)
```

### Download file


```python
cloud.download_file(
    path='WebdavTest/', 
    filename='kwg_mpg.xlsx', 
    target_dir='data/'
    )
```

### Read file

Read Excel file from Nextcloud.

```python
import pandas as pd
df = pd.read_excel(
    cloud.read_file(path='WebdavTest/', filename='kwg_mpg.xlsx'), engine='openpyxl'
    )
```

Read CSV

```python
import pandas as pd
from io import BytesIO
csv = cloud.read_file(path='WebdavTest/Subfolder/', filename='datei.csv')
df = pd.read_csv(BytesIO(csv))
```

### Delete file/ folder

Delete file
```python
cloud.delete_file(path='WebdavTest/subfolder/Datei.md')
```

Delete folder
```python
cloud.delete_file(path='WebdavTest/subfolder/Datei.md')
```