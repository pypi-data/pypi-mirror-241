from rdmhelper.keeper import Seafile
import os
import pytest
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='module')
def sf():
    sf = Seafile(
        server = 'https://keeper.mpdl.mpg.de',
        username = os.getenv('SEAFILE_USER'),
        password = os.getenv('SEAFILE_PW')
    )
    return sf

@pytest.fixture(scope='module')
def repo():
    return 'a6b66f03-86cc-443d-b38c-e40775957996'


class TestSeafileConstructor():

    def test_unknown_servername(self):
        #Not a valid URL
        with pytest.raises(Exception) as e:
            sf = Seafile(
                server = 'asdf',
                username = os.getenv('SEAFILE_USER'),
                password = os.getenv('SEAFILE_PW')
            )
        assert len(str(e.value)) > 0 

        #Valid URL but no Seafile installed
        with pytest.raises(Exception) as e:
            sf = Seafile(
                server = 'https://keeeeper.mpdl.mpg.de',
                username = os.getenv('SEAFILE_USER'),
                password = os.getenv('SEAFILE_PW')
            )
        assert len(str(e.value)) > 0 

    def test_servername_with_trailing_slash(self):
        sf = Seafile(
            server = 'https://keeper.mpdl.mpg.de/',
            username = os.getenv('SEAFILE_USER'),
            password = os.getenv('SEAFILE_PW')
        )
        assert sf.server == 'https://keeper.mpdl.mpg.de'


    def test_server_not_none(self, sf):
        assert sf.server is not None

    def test_server_not_empty(self, sf):
        assert sf.server != ""
    
    def test_server_type(self, sf):
        assert isinstance(sf.server, str)

    def test_token_not_none(self,sf):
        assert sf.token is not None
    
    def test_token_not_empty(self, sf):
        assert sf.token != ""
    
    def test_token_type(self, sf):
        assert isinstance(sf.token, str)


class TestAccountinfo():
    def test_account_info(self, sf):
        resp = sf.account_info()
        assert isinstance(resp, dict)
        assert resp['name'] == os.getenv('SEAFILE_USER').split("@")[0]
        assert resp['email'] == os.getenv('SEAFILE_USER')


class TestRepositoryFunctions():
    def test_list_repos(self, sf):
        resp = sf.repo_list()
        assert isinstance(resp, list)
        assert len(resp) > 0
        resp = sf.repo_list()
        for repo in resp:
            if repo['name'] == 'API_TEST':
                test_repo = repo
                assert test_repo['owner_name'] == 'hbenne'
                assert test_repo['id'] == '9c296bd2-153d-405f-b378-374bcf33e658'
                assert test_repo['type'] == 'repo'

    def test_share_repo(self, sf, repo):
        sf.repo_unshare(repo, user='hbenne@gmx.at').json()
        sf.repo_unshare(repo, user='doesnot_exist@gmail.com').json()
        user_list = user_list = ['hbenne@gmx.at', 'doesnot_exist@gmail.com']
        resp = sf.repo_share(repo, userlist=user_list, permissions='rw')
        resp_json = resp.json()
        assert resp.status_code == 200
        assert resp_json['failed'][0]['email'] == 'doesnot_exist@gmail.com'
        assert resp_json['failed'][0]['error_msg'] == 'User doesnot_exist@gmail.com not found.'
        assert resp_json['success'][0]['user_info']['name'] == 'hbenne@gmx.at'
    
    def test_unshare_repo(self, sf, repo):
        resp = sf.repo_unshare(repo, user='hbenne@gmx.at').json()
        assert resp['success'] == True


class TestFolderFunctions():
    def test_folder_create(self, sf, repo):
        resp = sf.folder_create(repo, 'test')
        assert resp.status_code == 201
        assert resp.json() == 'success'
        folder_content = sf.folder_list_content(repo,'test')
        assert folder_content == []
        test_folder_created = False
        for entry in sf.folder_list_content(repo, '/'):
            if entry['name'] == 'test':
                test_folder_created = True
        assert test_folder_created == True
        sf.folder_delete(repo, 'test')


    def test_folder_rename(self, sf, repo):
        sf.folder_create(repo, 'test')
        resp = sf.folder_rename(repo, 'test', 'test_renamed')
        assert resp.status_code == 200
        assert resp.json() == 'success'
        test_folder_renamed = False
        for entry in sf.folder_list_content(repo, '/'):
            if entry['name'] == 'test_renamed':
                test_folder_renamed = True
        assert test_folder_renamed == True
        resp = sf.folder_rename(repo, 'does_not_exist', 'new_name')
        assert resp.status_code == 404
        assert 'not found' in resp.json()['error_msg']
        sf.folder_delete(repo, 'test_renamed')

    def test_download_folder(self, sf, repo):
        ...

    def test_upload_folder(self, sf, repo):
        ...

class TestFilefunctions():
    def test_file_info(self, sf,repo):
        resp = sf.file_info(repo, 'Downloads/test.csv')
        assert resp['type'] == 'file'
        assert resp['name'] == 'test.csv'

    def test_file_search(self, sf,repo):
        resp = sf.file_search(repo, 'test_does_not_exist.csv')
        assert resp['total'] == 0
        assert resp['results'] == []
        resp = sf.file_search(repo, 'test.csv')
        assert resp['total'] > 0

    def test_file_upload(self, sf, repo):
        resp = sf.file_upload(
            repo, 
            file='tests/upload_folder/upload_test_file.txt', 
            remote_dir='Uploads', 
            add_date=True)
        assert resp.status_code == 200
        assert resp.json()[0]['name'] == 'upload_test_file' + datetime.now().strftime("_%Y_%m_%d") + '.txt'

    def test_file_download(self, sf, repo):
        ...

    def test_file_rename(self, sf, repo):
        with pytest.raises(NotImplementedError):
            sf.file_rename()
    
    def test_file_move(self, sf, repo):
        with pytest.raises(NotImplementedError):
            sf.file_move()