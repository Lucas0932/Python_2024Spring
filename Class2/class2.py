# make a new class
class Car: 
    def __init__(self, color):
        self.color = color
        self.next = None
# traverse the list
def traverse(head):
    ptr = head
    while True:
        print("The color of the car is {}.".format(ptr.color))
        if ptr.next ==head:
            break
        ptr = ptr.next
    print("finish traverse!")

# make the first element
head = Car("red")
ptr = head
ptr.next = None
# add new element
new_data = Car("blue")
ptr.next = new_data
new_data.next = head
ptr = new_data
traverse(head)