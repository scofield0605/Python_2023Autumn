class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next_employee = None

# 創建三個員工物件
amy = Employee("Amy", 25)
eddy = Employee("Eddy", 43)
esme = Employee("Esme", 32)

# 串接單向串列
amy.next_employee = eddy
eddy.next_employee = esme

# 走訪並印出單向串列中的所有內容
def traverse_linked_list(employee):
    current_employee = employee
    while current_employee is not None:
        print(f"員工姓名: {current_employee.name}, 員工年齡: {current_employee.age}")
        current_employee = current_employee.next_employee

# 呼叫函式
traverse_linked_list(amy)
