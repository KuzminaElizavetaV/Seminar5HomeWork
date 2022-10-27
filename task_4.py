'''задача 4 необязательная Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.'''

def find_step(pol):
    step = ''
    for i in range(len(pol)):
        if pol[i] == "^":
            step = step + pol[i + 1]
            while pol[i + 2].isdigit():
                step = step + pol[i + 2]
                i += 1
            break
    return int(step)

def return_koef(pol, max_step):
    list_koef = [(i, 0) for i in range(max_step + 1)]
    koef = 0
    for i in range(max_step, 1, -1):
        for el in pol:
            if f'^{i}' in el:
                if len(el) == len(str(i)) + 2: koef = 1
                else: koef = int(el[:el.find('x')-1])
                list_koef[i] = (i, koef)
    for el in pol:
        if "x" not in el:
            koef = int(el)
            list_koef[0] = (0, koef)
        if el.find('x') == len(el)-1:
            koef = int(el[:-2])
            list_koef[1] = (1, koef)
    return list_koef

with open('polynomial_1.txt', 'r', encoding="utf-8") as pol_1:
    pol_a = pol_1.read()
    print(f"Первый многочлен из файла: {pol_a}")
with open('polynomial_2.txt', 'r', encoding="utf-8") as pol_2:
    pol_b = pol_2.read()
    print(f"Второй многочлен из файла: {pol_b}")

max_degree = find_step(pol_a) if find_step(pol_a) > find_step(pol_b) else find_step(pol_b)
pol_a = ''.join(pol_a.split('=')[:-1]).split('+')
pol_b = ''.join(pol_b.split('=')[:-1]).split('+')
pol_a = list(map((lambda el: el.strip()), pol_a))
pol_b = list(map((lambda el: el.strip()), pol_b))
pol_a_kf = return_koef(pol_a, max_degree)
pol_b_kf = return_koef(pol_b, max_degree)
#print(pol_a_kf)
#print(pol_b_kf)

list_sum_kf = list(map(lambda x, y: (x[0], x[1]+y[1]), pol_a_kf, pol_b_kf))
#print(list_sum_kf)
list_sum_kf.reverse()
list_sum_kf = list(filter(lambda e: e[1] != 0, list_sum_kf))
str_p = list(map(lambda x: (str(x[1]) + "*x^" + str(x[0])), list_sum_kf))
str_p = list(map(lambda x: x.replace("*x^0", ""), str_p))
str_pol = " + ".join(str_p)
str_pol = str_pol.replace(" 1*x", " x").replace("x^1 ", "x ")
str_pol = str_pol + ' = 0'

print(f"Сумма этих многочленов равна: {str_pol}")

with open('polynomial_sum.txt', 'w') as data:
    data.write(str_pol)
