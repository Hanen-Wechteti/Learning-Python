class Node:
    def __init__(self , value):
        self.value = value
        self.next =None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print (temp.value)
            temp = temp.next

    def append(self, value):
            new_node = Node(value)
            #if this list is empty
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.length += 1
            return True


    # def pop(self):
    
    #     if self.length == 0:
    #         return None
    #     else:
    #         temp = self.head
    #         pre = self.head
    #         while (temp.next):
    #             pre = temp
    #             temp = temp.next
    #         self.tail = pre
    #         self.tail.next = None
    #         self.length -= 1
    #         if self.length == 0:
    #             self.head = None
    #             self.tail = None 
    #         return temp.value

    # def prepend(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #     self.length += 1
    # def pop_first(self):
    #     # si on a rien dans la liste
    #     if self.length == 0:
    #         return None
    #     #si on a plus qu'un dans la liste
    #     else: 
    #         temp = self.head
    #         self.head = self.head.next
    #         temp.next = None
    #     self.length -= 1
    #     # cette if depends de l'incrementation de length
    #     if self.length == 0:
    #         self.tail = None
    #     return temp.value

    
# My_linked_list = LinkedList(0)
# My_linked_list.append(1)
# My_linked_list.append(2)
# My_linked_list.append(4)

# print (My_linked_list.get(2))
#     def get(self, index):
#         if index < 0 and index >= 0:
#             return None
#         temp = self.head
#         for _ in range(index):
#             temp = temp.next
#         return temp.value  

    def get(self, index):
        if index < 0 and index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.set_value(1,4)
my_linked_list.print_list()
    















