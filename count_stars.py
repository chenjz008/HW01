import requests

#set the original number of the vairables
count = 0

#request the url and save the JSON data in the variable "repo_dicts"
#count the total number of stars
for i in range(1, 5):
        r = requests.get("https://api.github.com/users/emaadmanzoor/repos?page=" + str(i))
        if r.status_code != 200:
            break 
        repo_dicts = r.json()
        for j in repo_dicts:
            count = count + int(j['stargazers_count'])
print(count)
