'''задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.'''

def RLE_Code(string):
    str_rle = ''
    count_ch = 1
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i+1]: count_ch += 1
        else:
            str_rle += str(count_ch) + string[i]
            count_ch = 1
        i += 1
    str_rle += str(count_ch) + string[len(string)-1]
    return str_rle

def RLE_Decode(string):
    count = ''
    str_txt = ''
    for ch in string:
        if ch.isdigit():
            count += ch
        else:
            str_txt += ch*int(count)
            count = ''
    print(f"Восстановление данных выглядит так: {str_txt}")
    return str_txt

with open('text.txt', 'r', encoding="utf-8") as text:
        line = text.read()
print(f"Сжатие данных выглядит так: {RLE_Code(line)}")
with open('rle.txt', 'w') as rle_text:
        rle_text.write(RLE_Code(line))
with open('rle.txt', 'r') as rle_text:
        line_rle = rle_text.read()
RLE_Decode(line_rle)