class Atm:
    def __init__(self) -> None:
        self.__pin=""
        self.__balance = 0
        self.menu()

    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("pin chaged")

    def menu(self):
        user_input = input(""" 
            presss 1 to create pin
            press 2 to deposit
            press 3 to withdwa;
            press 4 to check balance
            press 5 for exit
                           """)
        if user_input =="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()

        elif user_input=="3":
            self.withdrawl()
        elif user_input=="4":
            self.checkBalance()
        else:
            
            print("BYE")

    def create_pin(self):
        self.__pin = input("type you pin : ")
        print("pin set succesfully")

    def deposit(self):
        temp = input("type your pin to deposit ")
        if temp == self.__pin:
            self.__balance += input("pin matched succefully \n type your amount")
        else:
            print("pin is incorrect")

    def withdrawl(self):
        temp = input("type your pin to withdrawl ")
        if temp == self.__pin:
            self.__balance -= input("pin matched succefully \n type your amount")
        else:
            print("pin is incorrect")

    def checkBalance(self):
        temp = input("type your pin to check balance ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("pin is incorrect")
