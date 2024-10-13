def factorial(x):
    f = 1
    for i in range(x):
        f = f*(i+1)
    return f
sayi =int(input("sayı girin:"))
print(f"faktöriyel değeri {factorial(sayi)}")
        