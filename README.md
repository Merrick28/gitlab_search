# gitlab_search

Simple script to allow a full text search on all your repositories/branches

## Usage

First, you have to [create a personal GitLab access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#creating-a-personal-access-token) with the read_api 

```
pyhton3 gitlab_search.py --gitlab_token xxxxxxx --search_string needle
```

## Options

You can also use specific options :

* --request_sleep : allows a sleep (in seconds) between each request, to avoid a "too many requests" exception
* --gitlab_api_url : if you use a self hosted or entreprise gitlab (not gitlab.com)

```
pyhton3 gitlab_search.py --gitlab_token xxxxxxx --search_string needle --request_sleep 0.25 --gitlab_api_url https://gitlab.mycomany.com/api/v4
```
