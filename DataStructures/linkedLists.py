class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class DoubleNode:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_previous(self, new_prev):
        self.previous = new_prev


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def get_node_by_item(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = current
            else:
                current = current.get_next()
        return found

    def iterate_list(self):
        current = self.head
        found = False
        while current is not None and not found:
                next = current.get_next()
                if next is None:
                    print (current.get_data())
                else:
                    print (current.get_data(),end=', ')
                current = current.get_next()

    def remove(self, item):
        current = self.head
        previous = None
        removed = False
        while current is not None and not removed:
            if current.get_data() == item:
                removed = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        elif current is None: #assume at end node
            return removed #item to exist doesn't exist
        else:
            previous.set_next(current.get_next())
        return removed

class UnorderedDoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        empty = self.isEmpty()
        temp = DoubleNode(item)
        temp.set_next(self.head)
        self.head = temp
        if empty:
            self.tail = temp
        else:
            previous = temp.get_next()
            previous.set_previous(temp)

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def search_reverse(self, item):
        current = self.tail
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_previous()
        return found

    def iterate_list(self):
        current = self.head
        while current is not None:
                next = current.get_next()
                if next is None:
                    print (current.get_data())
                else:
                    print (current.get_data(),end=', ')
                current = current.get_next()
        return None

    def iterate_list_reverse(self):
        current = self.tail
        while current is not None:
            previous = current.get_previous()
            if previous is not None:
                print (current.get_data(), end=', ')
                current = current.get_previous()
            else:
                print (current.get_data())
                current = current.get_previous()


    def get_node_by_item(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = current
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        removed = False
        while current is not None and not removed:
            if current.get_data() == item:
                removed = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        elif current is None: #assume at end node
            return removed #item to exist doesn't exist
        else:
            previous.set_next(current.get_next())
        return removed


mylist = UnorderedList()
#print(mylist.length()) #0
mylist.add(1)
mylist.add(5)
mylist.add(5467)
mylist.add(748)

# print(mylist.length())  # 4
# print(mylist.search(5))  # True
# print(mylist.get_node_by_item(5))  # node Object
# print(mylist.search(2))  # False
# print(mylist.remove(5))  # True
# print(mylist.length())  # 3
# print(mylist.search(5))  # False
# mylist.iterate_list()
# print('------------------------')

mylist2 = UnorderedList()

# print(mylist2.length())  # 0
# (mylist2.add(5))
# mylist2.add(10)
# mylist2.add(20)
# print(mylist2.remove(10))  # True
# print(mylist2.length())  #2
# print(mylist2.head)  # Node Object
# print(mylist2.remove(10)) # False

my_double_list = UnorderedDoubleLinkedList()
my_double_list.add(10)
my_double_list.add(50)
my_double_list.add(99)
my_double_list.add(2)
print(my_double_list.length())  # 4
my_double_list.iterate_list()
my_double_list.iterate_list_reverse()