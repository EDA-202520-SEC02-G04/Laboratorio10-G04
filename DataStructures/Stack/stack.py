from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as al
def new_stack():
    return al.new_list()

def push(my_stack, element):
    return al.add_first(my_stack,element)

def pop(my_stack):
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return al.remove_first(my_stack)  
        

def is_empty(my_stack):
    return al.is_empty(my_stack)

def top(my_stack):
    if al.size(my_stack)==0:
        raise Exception('EmptyStructureError: stack is empty')
    else:
        return al.first_element(my_stack)

def size(my_stack):
    if al.is_empty(my_stack):
        return 0
    return al.size(my_stack)
