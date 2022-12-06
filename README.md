# gitlab_search

Simple script to allow a full text search on all your repositories/branches

## Usage
```
$ python3 gitlab_search.py -h
usage: gitlab_search.py [-h] [--gitlab_api_url API_URL] [--request_sleep SLEEP_TIME] --gitlab_token GITLAB_TOKEN --search_string SEARCH_STRING

Search a string into all your repos/branches in GitLab

options:
  -h, --help            show this help message and exit
  --gitlab_api_url API_URL
                        Your gitlab API url (if self hosted/entreprise)
  --request_sleep SLEEP_TIME
                        Time to wait between two requests (in seconds, ex 0.1)
  --gitlab_token GITLAB_TOKEN
                        Your gitlab token (api read)
  --search_string SEARCH_STRING
                        String to search
```

First, you have to [create a personal GitLab access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#creating-a-personal-access-token) with the read_api.
To search the word "needle" :

```
pyhton3 gitlab_search.py --gitlab_token xxxxxxx --search_string needle
```

## Options

You can also use specific options :

* --request_sleep : allows a sleep (in seconds) between each request, to avoid a "too many requests" exception
* --gitlab_api_url : if you use a self hosted or entreprise gitlab (not gitlab.com)

```
pyhton3 gitlab_search.py --gitlab_token xxxxxxx \
    --search_string needle \
    --request_sleep 0.25 \
    --gitlab_api_url https://gitlab.mycomany.com/api/v4
```
