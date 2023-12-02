class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next_employee = None

class Car:
    def __init__(self):
        self.head = None

    def add_employee(self, name, age):
        new_employee = Employee(name, age)
        if self.head == None:
            self.head = new_employee

    def traverse(self):
        current_employee = self.head
        print("員工姓名:", current_employee.name, "員工年齡:",current_employee.age)
        current_employee = current_employee.next_employee

# 創建一個Car物件
car_list = Car()

# 新增員工到單向串列中
car_list.add_employee("Amy", 25)

# 走訪並印出單向串列中的所有內容
car_list.traverse()
