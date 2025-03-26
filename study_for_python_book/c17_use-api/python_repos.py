import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
# for key in sorted(first_repo.keys()):
    # print(key)

def show_repo_info(repo):
    print('repo name: ', repo['name'])    
    print('repo owner: ', repo['owner']['login'])    
    print('repo url: ', repo['url'])    
    print('repo language: ', repo['language'])    
    print('repo homepage: ', repo['homepage'])    
    print('repo git url: ', repo['git_url'])    
    print('repo created_at: ', repo['created_at'])    
    print('repo stargazers_count: ', repo['stargazers_count'])    
    print('repo updated_at: ', repo['updated_at'])    
    print('repo description: ', repo['description'])

names, stars = [], []
for repo in items:
    # show_repo_info(repo)
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])
    # print('\n')   

# 可视化
my_style= LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', stars)    
chart.render_to_file('python_repos.svg')