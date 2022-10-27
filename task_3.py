'''задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT
юзать нельзя.'''

txt = input('Введите текст:').split()
txt = list(filter((lambda el: "абв" not in el), txt))
new_txt = " ".join(txt)
print(new_txt)

