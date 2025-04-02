import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

allow_lans = ['JavaScript', 'Ruby', 'C', 'Java', 'C++', 'Perl', 'Haskell', 'Go', 'Kotlin', 'C#', 'Python', 'Html']
diaplay_lans = ', '.join(allow_lans)
tips = f'Please input the dev language({diaplay_lans}): '
dev_language_name = input(tips)

while dev_language_name not in allow_lans:
    print('Please input the correct dev language')
    dev_language_name = input(tips)

dev_language_repos_url = f'https://api.github.com/search/repositories?q=language:{dev_language_name.lower()}&sort=stars'
r = requests.get(dev_language_repos_url)

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

names, plot_dicts = [], []
for repo in items:
    # show_repo_info(repo)
    names.append(repo['name'])
    plot_dict = {
        'value': repo['stargazers_count'],
        'label': repo['description'],
        'xlink': repo['html_url']
    }
    plot_dicts.append(plot_dict)
    # print('\n')   

# 可视化
def get_config():
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    return my_config

my_style= LS('#333366', base_style=LCS)

chart = pygal.Bar(get_config(), style=my_style, x_label_rotation=45, show_legend=False)
chart.title = f'Most-Starred {dev_language_name} Projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)    
chart.render_to_file(f'{dev_language_name}_repos.svg')
print('Done: saved file: ', f'{dev_language_name}_repos.svg')