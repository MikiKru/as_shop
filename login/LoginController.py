class LoginController:
    def __init__(self):
        while(True):
            print("Co chcesz zrobić:")
            decision = input("1. logowanie 2. rejestracja Q. quit")
            if(decision == "1"):
                self.fun1()
                # tutaj wywołanie przejście do panelu usera przez obiekt UserController lub administratora itd
            elif(decision == "2"):
                self.fun2()
            elif(decision.upper() == "Q"):
                break
            else:
                print("Zły wybór")
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
