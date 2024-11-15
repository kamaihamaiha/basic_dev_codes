# 读取通讯录
import os

# 先得到当前python 程序执行的路径
cur_script_exe_path = os.path.dirname(os.path.abspath(__file__))
contacts_file_path = os.path.join(cur_script_exe_path, 'docs', 'contacts.csv')
with open(contacts_file_path, 'r') as f:
    file_data = f.readlines()
    print(file_data)

# 使用小型的数据库 tinydb
from tinydb import TinyDB

# 指定存放通讯录的文件
db = TinyDB('./contacts.json')
friend1_info = file_data[0].split(',')
friend2_info = file_data[1].split(',')
friend3_info = file_data[2].split(',')

friend_1 = {'name': friend1_info[0], 'source': friend1_info[1], 'tel': friend1_info[2].strip()}
friend_2 = {'name': friend2_info[0], 'source': friend2_info[1], 'tel': friend2_info[2].strip()}
friend_3 = {'name': friend3_info[0], 'source': friend3_info[1], 'tel': friend3_info[2].strip()}

# 把通讯录的好友信息，写入数据库
db.insert_multiple(
    [friend_1, friend_2, friend_3]
)
`