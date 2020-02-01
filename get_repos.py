import requests
import json
from datetime import datetime
import pprint
import threading
import time

list_pub_repo = 'https://api.github.com/repositories'

secret_key = "4e57f5f97acc7781c93acfc19b7af5bbd87a9162"
headers = {'Authorization': 'token %s' % secret_key}


def get_tags(base_response):
	for repo in base_response.json():
		repo_url = repo.get("url")

		if repo_url is not None:
			repo_get_request_data = requests.get(repo_url, headers=headers)
			repo_data = repo_get_request_data.json()
			repo_updated = repo_data.get("updated_at")
			
			if repo_updated is None:
				print("repo_updated not found")
				continue
			
			datetime_object_repo_updated = datetime.strptime(repo_updated, "%Y-%m-%dT%H:%M:%SZ")
			repo_updated_year = datetime_object_repo_updated.year
			
			if repo_updated_year>=datetime.now().year-1:
				labels_request_url = repo.get("labels_url")
				
				if labels_request_url is not None:
					labels_request_url = labels_request_url.split("{")[0]
					repo_labels = requests.get(labels_request_url, headers=headers).json()
					
					if len(repo_labels):
						print([i['name'] for i in repo_labels])
					else:
						print(f"No repo labels found for {repo_url}")
				else:
					print(f"skipped labels_request_url: {labels_request_url}")
		else:
			print("repo url not found") 

threads = []
base_response = requests.get(list_pub_repo, headers=headers)
if base_response.status_code == 403:
	time.sleep(60*60)

while "next" in base_response.links.keys():
	
	next_url = base_response.links.get("next").get("url")

	#threading

	x = threading.Thread(target = get_tags, args = (base_response,))
	threads.append(x)

	x.start()

	base_url = next_url
	base_response = requests.get(base_url, headers=headers)

for thread in threads:
	
	thread.join()

