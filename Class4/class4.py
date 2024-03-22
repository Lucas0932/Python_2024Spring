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
        if ptr.next == head:
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
# before adding a new one, make it be the head
new = Car("black")
new.next = head
ptr = head
while ptr.next != head:
    ptr = ptr.next
ptr.next = new
# insert new one into middle
head = new
new = Car("pink")
ptr = head
new.next = ptr.next
while ptr.color != "red":
    ptr = ptr.next
new.next = ptr.next
ptr.next = new
#--------------------------------------------------
# fine the element which points to head
ptr = head
while ptr.next != head:
    ptr = ptr.next
# set the new head(the original second node)
head = head.next
# point to new head
ptr.next = head
#--------------------------------------------------
# find the element before the node you want to delete
ptr = head
while ptr.next.color != "pink":
    ptr.next = ptr.next
# connect previous node of delete node to next node of the delete node
ptr.next = ptr.next.next

traverse(head)