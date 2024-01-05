class Member:
    def __init__(self, name, purchase_count):
        self.name = name
        self.purchase_count = purchase_count
        self.next_member = None
        self.prev_member = None

# 建立四個會員物件
abby = Member("Abby", 8)
john = Member("John", 10)
leo = Member("Leo", 17)
brian = Member("Brian", 1)

# 建立雙向串列
abby.next_member = john
john.prev_member = abby

john.next_member = leo
leo.prev_member = john

leo.next_member = brian
brian.prev_member = leo

# 打印雙向串列的內容
current_member = abby
while current_member is not None:
    print(f"會員姓名：{current_member.name}，購買次數：{current_member.purchase_count}")
    current_member = current_member.next_member
