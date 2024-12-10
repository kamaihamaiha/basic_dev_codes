# 个性化消息
name = 'Eric'
print("Hello " + name + ", would you like to learn some Python today?")

# 2-4 调整名字的大小写
name = 'Ada Lovelace'
print("Hello " + name.title() + ", would you like to learn some Python today?")
print("Hello " + name.upper() + ", would you like to learn some Python today?")
print("Hello " + name.lower() + ", would you like to learn some Python today?")

# 2-5
print('Albert Einstein once said: "A person who never made a mistake never tried anything new."')

# 2-6
famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(famous_person + ' once said: "' + message + '"')

# 2-7 
name = ' \tTrump\n '
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())