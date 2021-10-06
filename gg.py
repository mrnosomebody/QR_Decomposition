import string

letters = string.ascii_uppercase.replace('',' ').strip().split()
p = int(input('В какой системе записано число? ( если не указано значит пишем "10")'))
q = int(input('Какое основание?'))
a = int(input('Введите число'))
number = []
if p != 10:
    a = int(a, p)
while True:
    x = int(a) % q
    j = int(a) // q
    a = j
    if j == 0 and x == 0:
        break
    else:
        if x < 10:
            number.append(x)
        else:
            number.append(letters[x - 10])
number.reverse()
print(number)

if __name__ == '__main__':
    print(number)