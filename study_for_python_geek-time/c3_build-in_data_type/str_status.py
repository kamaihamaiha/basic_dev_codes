import pprint
with open("/Users/kk/Codes/basic_dev_codes/study_for_python_geek-time/c3_build-in_data_type/ docs/demo_article.txt") as file:
    file_data = file.readlines()
    # pprint.pprint(file_data)

# 统计全部行数
print(len(file_data))

# 统计空行行数
print(file_data.count("\n"))

# 非空行行数
print("非空行行数: ", len(file_data) - file_data.count("\n"))

# 统计单词 and 出现的次数
print(str(file_data).split(" ").count('and'))
