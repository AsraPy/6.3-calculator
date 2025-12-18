def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "تقسيم بر صفر ممکن نيست."

def menu():
    while True:
        print("\n ماشين حساب")
        print("1.جمع")
        print("2.تفريق")
        print("3.ضرب")
        print("4.تقسيم")
        print("5.خروج")
        
        choice = input("(5-1)يک گزينه را انتخاب کنيد")
        if choice == "1":
            num1 = float(input("عدد اول را وارد کنيد"))
            num2 = float(input("عدد دوم را وارد کنيد"))
            print(f"نتيجه جمع:{add(num1,num2)}")
            
        elif choice == "2":
            num1 = float(input("عدد اول را وارد کنيد"))
            num2 = float(input("عدد دوم را وارد کنيد"))
            print(f"نتيجه تفريق:{subtract(num1,num2)}")
            
        elif choice == "3":
            num1 = float(input("عدد اول را وارد کنيد"))
            num2 = float(input("عدد دوم را وارد کنيد"))
            print(f"نتيجه ضرب:{multiply(num1,num2)}")

        elif choice == "4":
            num1 = float(input("عدد اول را وارد کنيد"))
            num2 = float(input("عدد دوم را وارد کنيد"))
            print(f"نتيجهتقسيم:{divide(num1,num2)}")

        elif choice == "5":
                print("برنامه پايان يافت")
                break
        else:
                print("گزينه نامعتبر لطفا دوباره تلاش کنيد")
menu()













            
            
