# RLE алгоритм.

def compression(file_name):
    with open(file_name, 'r') as file:
        data_in_file = list(file.read())

    element = data_in_file[0]
    encoding = ''
    coun = 0
    for i in data_in_file:
        if element == i:
            coun += 1
        else:
            encoding += str(coun) + element
            element = i
            coun = 1
    encoding += str(coun) + element
    return encoding


def recovery(file_name):
    with open(file_name, 'r') as file:
        data_in_file = list(file.read())
    encoding = ''
    num = 0
    for value in data_in_file:
        if value.isdigit():
            num = int(value)
        else:
            encoding += value*num
    return encoding


print(compression('2.txt'))
print(recovery('3.txt'))
