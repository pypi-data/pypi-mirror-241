from flask import jsonify
import datastack as ds
import pandas as pd
import requests, json, os

# -------------------------------- user py file ------------------------------
def dummy_fn():
    pass

# ds = datastack()

# def test():
#     # startup function

#     # print(ds.app)
#     return jsonify(ds.build_app())

# def rerun():
#     # get_scheduler_status()
#     global a1
#     a1 = {k: v for k, v in globals().items() if not k.startswith("__")}
#     return jsonify(ds.rerun(a1, {}))

# this should go to ds lib
# def update_var(aaa):
#     # globals()[f"input_value"]=aaa['payload']
#     globals()[aaa['prop']['input_var']]=aaa['payload']
#     # print(globals()[f"input_var"], aaa['payload'])

# def update_var_select(aaa):
#     globals()[aaa['prop']['value_frm']]=aaa['payload']
#     globals()[aaa['prop']['on_change_name']]()

# functions
notebook_list = ''
project_list = ''
notebook_url=''
notebook_name = ''
jupyter_url = 'http://localhost:8888/api/contents/'
project_folder_path = r'C:\Users\vvora\Desktop\vishal_vora\projects\datastack\data\notebooks'
token = 'e8e0acf46a2d96faa6ccbd8ff37a3a6cd728c497a92acb34'
headers={
        'Authorization': f'Token {token}',
    }
def get_dir():
    global project_list
    res = requests.get('http://localhost:8888/api/contents/', headers=headers)
    global mydirs
    mydirs = pd.json_normalize(res.json()['content'])
    mydirs = mydirs[mydirs.type=='directory']
    print(mydirs)
    project_list =json.loads(mydirs['name'].to_json(orient='split'))['data']

def load_project(a):
    global selected_project
    selected_project = a['payload']
    get_notebooks(selected_project)
    print(mydirs)

def load_project1():
    get_notebooks(selected_project)

def open_notebook(a):
    global selected_list, notebook_url
    path = mynotebooks[mynotebooks['name'] == a['payload']]['path'].iloc[0]
    selected_list = "http://localhost:8888/notebooks/"+ path
    notebook_url= selected_list
    ds.set_page('notebook_i_page')


def get_notebooks(project = ''):
    global notebook_list
    res = requests.get('http://localhost:8888/api/contents/{}'.format(project), headers=headers)
    global mynotebooks
    mynotebooks = pd.json_normalize(res.json()['content'])
    try:
        mynotebooks = mynotebooks[mynotebooks.type=='notebook']
        notebook_list =json.loads(mynotebooks['name'].to_json(orient='split'))['data']
    except:
        notebook_list = []
    ds.set_page('notebooks_page')

def load_page(a):
    if a['payload'] == 'Notebooks':
        ds.set_page('notebooks_page')
    elif a['payload']=='Scheduler':
        ds.set_page('scheduler_page')
    elif a['payload'] =='Notes':
        ds.set_page('notes')
    else:
        ds.set_page('main_page')
def new_project(a):
    ds.set_page('new_project_page')

def create_new_project(a):
    global new_project_name
    os.mkdir(os.path.join(project_folder_path,new_project_name))
    get_dir()

def create_new_notebook(a):
    # global notebook_name
    # print(notebook_name)
    # open(os.path.join(project_folder_path,selected_project,notebook_name+'1.ipynb'), 'w+')
    res = requests.post(os.path.join(jupyter_url, selected_project), headers=headers, json={'type':'notebook'})
    # if res.status_code == 200:
    get_notebooks(selected_project)


# def new_notebook(a):
#     notebook_name = 'new_notebook'
#     notebook_page.input(notebook_name)
#     notebook_page.button('save', on_click=create_new_notebook)
# --------



# ui
selected_project=''
get_dir()
ds.sidebar().write("projects")
selected_project = ds.sidebar().select(project_list, value=selected_project, on_change=load_project1)
# ds.sidebar().write('seleted projetc: ' + selected_project)
# ds.sidebar().write('seleted projetc_vallue assign: ' + s_projetc)


# ds.sidebar().list(project_list, on_click=load_project)
ds.sidebar().button('Add_new_project', on_click=new_project)
ds.sidebar().write('-------------------------------------------')

notebook_expander = ds.sidebar().expander('notebooks')
notebook_expander.list(notebook_list, on_click=open_notebook)

# pages
notebook_page = ds.page('notebooks_page')
notebook_i_page = ds.page('notebook_i_page')
new_project_page = ds.page('new_project_page')
notes = ds.page('notes')
ds.sidebar().list(['home','Notebooks','Scheduler', 'Notes'], on_click=load_page, location='sidebar')



# notebook page
notebook_page.write('Notebooks')
notebook_page.list(notebook_list, on_click=open_notebook)
notebook_page.button('Create new notebook', on_click=create_new_notebook)
notebook_i_page.iframe(notebook_url)


# new project page
new_project_page.write('Add new project')
new_project_name = 'Project Name'
new_project_page.input(new_project_name)
new_project_page.button('save', on_click=create_new_project)


# notes page
notes.write('Notes')
notes.editable_html('my_notes7')



# test_container = ds.container()
# test_container.write('This is inside the test container from py')
# ds.write('this is out side the container form py')
# test_container.list(['a','b','c'])

# test_expander = ds.expander('test expander')
# test_expander.write('this is inside the expander from py')

# new_expander = ds.expander('new_expander')
# new_expander.write('this is new expander')
# test_expander.write('agian in the test expander')

# acv = ds.special()

# widget value assign test
# s_v =''
# options = ['a','b','c']
# ds.select(options, value=s_v, on_change=dummy_fn)
# ds.write('normal value assign', s_v)
# ds.write('special value assign',var_value)
