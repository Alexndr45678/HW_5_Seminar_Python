# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ')
text = list(filter(lambda x: 'абв' not in x, text.split()))
print(f'Текст без "абв":', " ".join(text))