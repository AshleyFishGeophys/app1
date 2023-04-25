waiting_list = ['sen', 'ben', 'john']
waiting_list.sort()

for idx, item in enumerate(waiting_list):
    print(f"{idx + 1}.{item.capitalize()}")
