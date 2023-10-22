print("Hello word")

def suma() :
    a = int(input("a:"))
    b = int(input("b:"))
    print(a + b)
def risnyca() :
    c = int(input("a:"))
    d = int(input("b:"))
    print(c - d)

print("Хотите выполнить отнимание?")
otn = input("")
if "Да" in otn :
    risnyca()
elif "Нет" in otn :
    print("Отнимание не выполнено")
else:
    print("Неивестный символ")