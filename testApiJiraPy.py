from jira import JIRA
import json
import os

jsonFolderPath = 'data'
if not os.path.exists(jsonFolderPath):
    os.mkdir(jsonFolderPath)
url = "https://dariotest.atlassian.net"

jira = JIRA(server=url, options={'rest_api_version': 3})

issues = jira.search_issues('project=10000')

for issue in issues:
    print(json.dumps(issue.raw, indent=4, sort_keys=False))
    with open(jsonFolderPath + '/' + issue.fields.issuetype.name + '-' + issue.id + '.json', 'w') as outfile:
        json.dump(issue.raw, outfile, indent=4)
