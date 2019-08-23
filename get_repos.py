import requests
import json
from datetime import datetime
import pprint

list_pub_repo = 'https://api.github.com/repositories?since=364'

r = requests.get(list_pub_repo)

# last_repo = r.json()[-2]
# print(json.dumps(last_repo, sort_keys = True, indent = 4))
# last_updated = last_repo.get("id")
# print(last_updated)
# for repositories in r.json():
# 	print(repositories)
# 	dt = datetime.strptime("2011-01-26T19:14:43Z", "%Y-%m-%dT%H:%M:%SZ")
	# print(dt)
for repo in r.json():
	print(r)
	repo_url = repo.get("owner").get("url")
	if repo_url is not None:
		repo_get_request_data = requests.get(repo_url)
		repo_data = repo_get_request_data.json()
		repo_updated = repo_data.get("updated_at")
		# print(repo_updated)
		dt = datetime.strptime(repo_updated, "%Y-%m-%dT%H:%M:%SZ")
		# print(dt)
		dt_year = dt.year
		print(dt_year)


# repoURL = r.json.repo("url")
# print(repoURL)
