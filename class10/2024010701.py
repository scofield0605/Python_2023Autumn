class Car:
    def __init__(self,color):
        self.color= color
        self.next=None

head = Car("red")
second = Car("blue")
thrid=Car('black')
fourth=Car('pink')
thrid.next=head
head.next=second
second.next=thrid
fourth.next=second
head.next=fourth

def traverse(thrid):
    ptr = thrid
    while True:
        print("The color of the car is {}.".format(ptr.color))
        if ptr.next == thrid:
            break
        ptr = ptr.next
    print("Finish traverse!")
traverse (thrid) 