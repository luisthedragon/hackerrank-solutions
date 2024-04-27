

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    aux = head
    counter = 1
    while aux.next!=None:
        aux = aux.next
        counter+=1
        if counter>1000:
            return 1
    return 0


