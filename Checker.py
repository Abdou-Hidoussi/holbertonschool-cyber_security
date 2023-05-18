from Check_Task import check_all
import requests
import os

def del_folder(folder_name):
    """ clear the content of a folder """
    if os.path.exists(folder_name):
        for filename in os.listdir(folder_name):
            file_path = os.path.join(folder_name, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                del_folder(file_path)
        print(f"Content of '{folder_name}' has been deleted.")
    else:
        print(f"'{folder_name}' does not exist.")

def get_latest_commit_id(username, repo_name):
    """ get the latest commit of a github repo """
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(api_url)
    response_json = response.json()
    try:
        latest_commit = response_json[0]
        latest_commit_id = latest_commit['sha']
        return latest_commit_id
    except :
        return None

def get_content(username, repo_name, file_path):
    """ get github file by repo username and file path and returns it's content"""
    latest_commit_id = get_latest_commit_id(username, repo_name)
    if latest_commit_id == None:
        return None
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}?ref={latest_commit_id}"
    headers = {"Accept": "application/vnd.github.VERSION.raw"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        content = response.text
    else:
        content = None
    return content

def save_content(content, file_path):
    """ save provided content into a file """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w+') as file:
        file.write(content)

def check_repo(username, repo_name, folder,file_list, task_list):
    """ run checker list on a github repo """
    output = {}
    for file in file_list:
        cont = get_content(username, repo_name, file)
        if cont != None:
            save_content(cont, "download_files/"+username+"/"+folder+"/"+file)
    for task in task_list:
        output[task] =  check_all(folder+"/"+task+"/"+task+".json", "output/"+username+"/"+folder+"/"+task, "download_files/"+username+"/"+folder)
    del_folder("download_files/"+username+"/"+folder)
    return output
