import requests

python_repos_url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(python_repos_url)

print('status coce:', r.status_code)

# 储存网络请求结果
response_dict = r.json()
# show resposne
TOTAL_COUNT_KEY = 'total_count'
INCOMPLETE_RESULTS = 'incomplete_results'
ITEMS = 'items'

total_count = response_dict[TOTAL_COUNT_KEY]
incomplete_results = response_dict[INCOMPLETE_RESULTS]
items = response_dict[ITEMS]

print('total_count:', total_count)
print('incomplete_results:', incomplete_results)
print('Repositories returned: ', len(items))

# 研究第一个仓库
first_repo = items[0]
print('\nKeys:', len(first_repo))
for key in sorted(first_repo.keys()):
    print(key)