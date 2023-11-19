from flask import jsonify
from ds_class import datastack
import pandas as pd
import os
git_dir = r"C:\Users\vvora\Downloads\PortableGit\bin;%PATH%"
os.environ["PATH"] = git_dir
from git import Repo

# repo = Repo(r'C:\\Users\\vvora\\Desktop\\vishal_vora\\projects\\datastack\\data\\notebooks\\pilot_yield')
# repo.index.add('**')
# repo.index.commit("in")
# modified_files = repo.git.diff(name_only=True)
# print('modigied files',repo.git.diff(name_only=True))
# import sys
# sys.path.append(r'\\fs02\Engineering\IndiaTeam\Projects\vvora\sm')
# from data_stack import sql, datasets
# from enovix_sm import fn

# notbook api test
notebook_list = ''
project_list = ''
token = 'e8e0acf46a2d96faa6ccbd8ff37a3a6cd728c497a92acb34'
headers={
        'Authorization': f'Token {token}',
    }
import requests
import json
def get_dir():
    global project_list
    res = requests.get('http://localhost:8888/api/contents/', headers=headers)
    global mydirs
    mydirs = pd.json_normalize(res.json()['content'])
    mydirs = mydirs[mydirs.type=='directory']
    print(mydirs)
    project_list =json.loads(mydirs['name'].to_json(orient='split'))['data']

def get_notebooks(project = ''):
    global notebook_list
    res = requests.get('http://localhost:8888/api/contents/{}'.format(project), headers=headers)
    global mynotebooks
    mynotebooks = pd.json_normalize(res.json()['content'])
    mynotebooks = mynotebooks[mynotebooks.type=='notebook']
    notebook_list =json.loads(mynotebooks['name'].to_json(orient='split'))['data']

# -------------------------------- user py file ------------------------------
def dummy_fn():
    pass

ds = datastack()

def test():
    # startup function

    # print(ds.app)
    return jsonify(ds.build_app())

def rerun():
    # get_scheduler_status()
    global a1
    a1 = {k: v for k, v in globals().items() if not k.startswith("__")}
    return jsonify(ds.rerun(a1, {}))


# this should go to ds lib
def update_var(aaa):
    globals()[f"input_value"]=aaa['payload']

def update_var_select(aaa):
    globals()[aaa['prop']['value_frm']]=aaa['payload']


# git 
def git_info(path):
    global modified_files, file_list
    print('getting file list from git')
    repo = Repo('C:\\Users\\vvora\\Desktop\\vishal_vora\\projects\\datastack\\data\\notebooks\\pilot_yield')
    print(repo.git.ls_files() )
    modified_files = repo.git.diff(name_only=True)
    file_list = repo.git.ls_files()
    print('modified files',modified_files,type(modified_files))
    ds.sidebar().write('Git File List')
    ds.sidebar().list(file_list.split('.ipynb'))

#     return rerun()
notebook_url = 'http://localhost:8888/tree'
selected_list =''

def list_click(a):
    global selected_list, notebook_url
    path = mynotebooks[mynotebooks['name'] == a['payload']]['path'].iloc[0]
    selected_list = "http://localhost:8888/notebooks/"+ path
    notebook_url= selected_list
selected_project = ''

def load_project(a):
    global selected_project
    selected_project = a['payload']
    get_notebooks(selected_project)
    print(mydirs)
    git_info('')

# scheduler status
def get_scheduler_status():
    import json
    global tasks, task_list
    tasks_df = pd.json_normalize(json.load(open(r'\\fs02\Engineering\IndiaTeam\Projects\vvora\sm\enovix_sm\scheduler\scheduler_status.json')))
    tasks = tasks_df.to_html()
    task_list  = json.loads(tasks_df['tags'].to_json(orient='split'))['data']

def show_run_status(a):
    global runs, runs_file_name
    runs_file_name = a['payload'].replace("'",'').replace("{","").replace("}","")
    runs = pd.json_normalize(json.load(open(r'\\fs02\Engineering\IndiaTeam\Projects\vvora\sm\enovix_sm\scheduler\{}.json'.format(runs_file_name)))).tail(10).T.to_html()

def load_notebook_page():
    ds.write('Notebook Page', location='sidebar')

def load_scheduler_page():
    ds.write('Scheduler Page')

def load_page(a):
    if a['payload'] == 'Notebooks':
        ds.set_page('notebooks_page')
    elif a['payload']=='Scheduler':
        ds.set_page('scheduler_page')
    else:
        ds.set_page('main_page')



#  ui
# pages
scheduler_page = ds.page('scheduler_page')
notebooks_page = ds.page('notebooks_page')

# project list
ds.sidebar().write('projects', location='')
get_dir()
ds.sidebar().list(project_list, on_click=load_project)
ds.sidebar().write('selected project: ' + selected_project)

# navigation
ds.sidebar().list(['home','Notebooks','Scheduler'], on_click=load_page, location='sidebar')

# Notebooks
notebooks_page.write("Notebooks")
notebooks_page.list(notebook_list, on_click=list_click)


get_scheduler_status()
scheduler_page.html(tasks)
scheduler_page.list(task_list, on_click=show_run_status)
runs=''
runs_file_name=''
scheduler_page.write(runs_file_name + ' runs')
scheduler_page.html(runs)




# ds.html(mynotebooks.to_html())

ds.sidebar().write('selected_list element: '+selected_list)
ds.iframe(notebook_url)

ds.sidebar().write('Modified files')
modified_files = ''
ds.sidebar().list(modified_files.split('.ipynb'))
