from MyJsonHelper import MyJsonHelper


# step1: download json file
json_file_download_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
file_name = 'docs/btc_close_2017_urllib.json'
json_helper = MyJsonHelper(json_file_download_url, file_name)
# json_data = json_helper.download_file_v2()
# print(json_data)

# step2: fill to format
json_helper.fill_to_format_data()

# step3 draw
json_helper.draw_line_chart()
print('finish!')


