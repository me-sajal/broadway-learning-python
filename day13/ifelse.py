class Bank:
    # Private variable
    __password = "673A24E0"

    # Public Variable
    attempts = 0

    # Setter
    def setPassword(self):
        password = input("Please enter the password: ")
        self.password = password
        Bank.attempts += 1

    # Check Method
    def checkPassword(self):
        if self.password == Bank.__password:
            return (1)
        else:
            return (0)


#
# print(Bank._password)
b1 = Bank()
print(b1._Bank__password)
while Bank.attempts != 3:
    print(f"Attempt {Bank.attempts + 1}")
    b1.setPassword()
    verification = b1.checkPassword()
    if verification == 1:
        break
    else:
        continue
if verification:
    print("Access Granted!!!")
else:
    print("Access Denied!!!")