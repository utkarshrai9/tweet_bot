import requests
import json
from datetime import datetime
import pprint

list_pub_repo = 'https://api.github.com/repositories'

secret_key = "Enter your own secret_key"
headers = {'Authorization': 'token %s' % secret_key}
r = requests.get(list_pub_repo, headers=headers)
# last_repo = r.json()[-2]
# print(json.dumps(last_repo, sort_keys = True, indent = 4))
# last_updated = last_repo.get("id")
# print(last_updated)
# for repositories in r.json():
# 	print(repositories)
# 	dt = datetime.strptime("2011-01-26T19:14:43Z", "%Y-%m-%dT%H:%M:%SZ")
	# print(dt)
for repo in r.json():
	# print(r.json())
	repo_url = repo.get("url")
	if repo_url is not None:
		repo_get_request_data = requests.get(repo_url, headers=headers)
		repo_data = repo_get_request_data.json()
		repo_updated = repo_data.get("updated_at")
		# print(repo_updated)
		if repo_updated is None:
			print("Looking XXX...      ", end="", flush=True)
			continue
		dt = datetime.strptime(repo_updated, "%Y-%m-%dT%H:%M:%SZ")
		dt_year = dt.year
		# print(dt_year)
		if dt_year>=datetime.now().year-1:
			# print(repo_url)
			labels_url = repo.get("labels_url")
			if labels_url is not None:
				labels_url = labels_url.split("{")[0]
				labels = requests.get(labels_url, headers=headers).json()
				if len(labels):
					print([i['name'] for i in labels])
			else:
				print("Looking XXX...      ", end="", flush=True)





# repoURL = r.json.repo("url")
# print(repoURL)
