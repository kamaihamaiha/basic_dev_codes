# 分析文学作品里面的信息
filename = '../txt_files/Alice.txt'

def get_file_content(filename):
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:	
		print("alice file not found.")
	else:
		return contents

book_contents = get_file_content(filename)		
line = len(book_contents.split('\n'))
words = book_contents.split()
print("line: " + str(line) + ", words: " + str(len(words)))	

# word statistics info

word_dict = {}
for word in words:
	if word in word_dict.keys():
		word_dict[word] += 1
	else:
		word_dict[word] =1

print("word count: " + str(len(word_dict.keys())))	

# 按照词频排序
word_dict_sorted = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))

for word, count in word_dict_sorted.items():
	print(word.ljust(15) + "\t\t出现次数: " + str(count) + "次")


