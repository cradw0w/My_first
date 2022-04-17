import random


print("Добро пожаловать в password generator! v 0.1")

up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dig = ['2', '3', '4', '5', '6', '7', '8', '9']

print("Введите желаемое количество паролей и их длину в формате (5, 5)")

def generate_password(length):
    pasw = ""
    count = 0
    for i in range(length):
        if count < 1:
            random.shuffle(dig)
            elem = dig[0]
            pasw += elem
            count += 1
        elif count < 2:
            random.shuffle(up)
            elem = up[0]
            pasw += elem
            count += 1
        elif count >= 2:
            random.shuffle(low)
            elem = low[0]
            pasw += elem
            count += 1
    return pasw        
    pass

def generate_passwords(count, length):
    clear = []
    for i in range(count):
        s = generate_password(length)
        clear.append(s)
    return(clear)
    pass

n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep = "\n")
