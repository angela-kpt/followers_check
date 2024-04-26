import json, os
from js import document, window, Uint8Array
from pyodide.ffi.wrappers import add_event_listener

filenames = []
files = []

async def upload_file_and_show(e):
    file_list = e.target.files
    
    first_item = file_list.item(0).name
    second_item = file_list.item(1).name
    
    my_json: json = await get_json_from_file(file_list.item(0))
    my_json2: json2 = await get_json_from_file(file_list.item(1))
    
    if first_item == 'following.json':
        following = json.loads(my_json)
        followers_1 = json.loads(my_json2)
    else:
        following = json.loads(my_json2)
        followers_1 = json.loads(my_json)

    check_followers(following, followers_1)
    
async def get_json_from_file(file):
    array_buf = await file.arrayBuffer()
    bytes_file = array_buf.to_bytes()
    json_file  = bytes_file.decode('utf8').replace('\n\t', '')
    return json_file

# Use pyodide's FFI to attach the function as an event listener for the file upload element
# https://pyodide.org/en/stable/usage/api/python-api/ffi.html#pyodide.ffi.wrappers.add_event_listener
add_event_listener(document.getElementById("file-upload"), "change", upload_file_and_show)



def check_followers(following_json, followers_1_json):
    following_list = []
    followers_list = []
    unfollowed_list = []

    for i in range(len(following_json['relationships_following'])):
        following = following_json['relationships_following'][i]['string_list_data'][0]['value']
        following_list.append(following)

    for i in range(len(followers_1_json)):
        followers = followers_1_json[i]['string_list_data'][0]['value']
        followers_list.append(followers)

    unfollowed_list = [i for i in following_list if i not in followers_list]


    print('Not Following You Back:\n')
    for i in unfollowed_list:
        print(i)

    return unfollowed_list
