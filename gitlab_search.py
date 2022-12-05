import requests,time

api_url = 'https://gitlab.xxxxx.fr/api/v4/'
token = 'xxxxxxxxxxx' # token api-read
search_text = 'text_to_search'
sleep_time = 0.3
# Définition du header
headers = {'PRIVATE-TOKEN': token}


def get_groups():
    url = api_url + 'groups'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()


def get_projects(mygroup):
    url = api_url + 'groups/' + str(mygroup) + '/projects'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()


def get_branches(myproject):
    url = api_url + 'projects/' + str(myproject) + '/repository/branches'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def get_search(myproject, mybranch):
    url = api_url + 'projects/' + str(myproject) + '/search?scope=blobs&search=' + search_text + '&ref=' + mybranch
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    groups = get_groups()
    for group in groups:
        projects = get_projects(group['id'])
        for project in projects:
            branches = get_branches(project['id'])
            for branch in branches:
                search_results = get_search(project['id'], branch['name'])
                for my_result in search_results:
                    print("Found in project " + project['name'] + ", branch " + branch['name'] + " in file " + my_result["basename"])
                time.sleep(sleep_time)
    print(' -- Over --')
