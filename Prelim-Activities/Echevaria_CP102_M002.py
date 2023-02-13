# John Leo D. Echevaria
# CP102 - M001

class Employee:
    # Employee constructor with private attributes
    def __init__(self):
        self.__Name = ""
        self.__Gender = ''
        self.__Bdate = ""
        self.__Position = ""
        self.__Rate = 0
        self.__Dayswork = 0

    # Setters
    def setName(self,name):
        self.__Name = name

    def setGender(self,gender):
        self.__Gender = gender

    def setBdate(self,Bdate):
        self.__Bdate = Bdate

    def setPosition(self,Position):
        self.__Position = Position

    def setRate(self,Rate):
        self.__Rate = Rate

    def setDayswork(self,Dayswork):
        self.__Dayswork = Dayswork


    # Getters
    def getName(self):
        return self.__Name

    def getGender(self):
        return self.__Gender

    def getBdate(self):
        return self.__Bdate

    def getPosition(self):
        return self.__Position

    def getRate(self):
        return self.__Rate

    def getDayswork(self):
        return self.__Dayswork


    # Gross Method
    def getGross(self):
        self.__Gross = self.__Dayswork * self.__Rate
        return self.__Gross

    # SSS Method
    def getSSS(self):
        if self.__Gross < 10000:
            self.__SSS = 500
        elif self.__Gross > 10000 and self.__Gross < 20000:
            self.__SSS = 1000
        else:
            self.__SSS = 1500
        return self.__SSS

    # Tax Method
    def getTax(self):
        if self.__Gross < 10000:
            self.__Tax = 0
        elif self.__Gross > 10000 and self.__Gross < 20000:
            self.__Tax = self.__Gross * 0.10
        elif self.__Gross > 20000 and self.__Gross < 30000:
            self.__Tax = self.__Gross * 0.20
        else:
            self.__Tax = self.__Gross * 0.25
        return self.__Tax

    # Net Salary Method
    def getNetSalary(self):
        self.__netSalary = self.__Gross - self.__SSS - self.__Tax
        return self.__netSalary

    # Employee Method
    def getEmployeeDetails(self):
        print(f"Name: {self.__Name}\nGender: {self.__Gender}\nBirth Date: {self.__Bdate}\nPosition: {self.__Position}\n")
    

def main():
    # Setting employee object
    emp = Employee()
    emp.setName(input("Enter Employee Name: "))
    emp.setGender(input("Enter Employee Gender (M/F): "))
    emp.setBdate(input("Enter Birth Date: "))
    emp.setPosition(input("Enter Position: "))
    emp.setRate(int(input("Enter Rate per day: ")))
    emp.setDayswork(int(input ("Enter Days Worked: ")))

    # Printing employee details
    print("\nEmployee Details:\n")
    emp.getEmployeeDetails()

    # Printing Salary Details
    print("\nSalary Details:\n")

    print(f"Gross Salary: P{emp.getGross():.2f}")
    print(f"SSS: P{emp.getSSS():.2f}")
    print(f"Tax: P{emp.getTax():.2f}")
    print(f"Net Salary: P{emp.getNetSalary():.2f}")

if __name__=="__main__":
    main()