import math
a = int(input('введіть цифру1 '))
b = int(input('введіть цифру2 '))

print('''Додавання:\n\t1. Файл\n\t2. Вид\n\t3. Вихід\n''')

choice = int(input('Ваш вибір: '))

if choice == 1:
    print('Ви вибрали пункт меню "Додавання"')
    print(a+b)
elif choice == 2:
    print('Ви відкрили меню "Віднімання"')
    print(a-b)
elif choice == 3:
    print('Ви відкрили меню "Множення"')
    print(a*b)
elif choice == 4:
    print('Ви відкрили меню "Ділення"')
    print(a/b)
elif choice == 5:
    print('Ви відкрили меню "Зведення в ступінь"')
    print(a ** b)
