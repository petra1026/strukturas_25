class Node:
    def __init__(self, info, prev=None, next=None):
        self.info = info
        self.next = next
        self.prev = prev
        return

    def read(self):
        print(self.info)
        return 


class List:
    def __init__(self):
        self.head = None
        self.size = 0
        return

    def add(self, new, index = -1):
        if index == -1 or index >= self.size:
            if self.head == None:
                self.head = Node(new)
            else:
                last = self.head
                while last.next:
                    last = last.next
                last.next = Node(new, prev = last)
        else:
            if index == 0:
                element = Node(new, next = self.head)
                self.head.prev = element
                self.head = element
            else:
                current = self.head
                for i in range(index):
                    current = current.next
                prev_node = current.prev
                element = Node(new, prev_node, current)
                prev_node.next = element
                current.prev = element

        self.size += 1
        return

    def read(self):
        if self.head == None:
            print("List is empty!")
        current = self.head
        while current:
            current.read()
            current = current.next
        return

    def pop(self):
        if self.size == 0:
            print("Nothing to delete!")
            return 
        if self.size == 1:
            self.head = None
            self.size = 0
            return
        
        second_last = self.head
        while second_last.next.next :
            second_last = second_last.next

        second_last.next = None
        self.size -=1
        return

    def switch(self, index1, index2):
        if index1 >= self.size or index2 >= self.size:
            print("One of the indices is out of range!")
            return
        if index1 == index2:
            return

        # atrast pirmo elementu
        elem1 = self.head
        for i in range(index1):
            elem1 = elem1.next

        # atrast otro elementu
        elem2 = self.head
        for i in range(index2):
            elem2 = elem2.next

        elem1.info, elem2.info = elem2.info, elem1.info
        return


# Testēt kodu
my_list = List()

# 1. Tests add() ar dažādām pozīcijām
print("1. Testing add() operation:")
my_list.add("First")  # Add to end
my_list.add("Second") # Add to end
my_list.add("Third")  # Add to end
my_list.add("Start", 0)  # Add to start
my_list.add("Middle", 2)  # Add to middle
print("After adding elements:")
my_list.read()

# 2. Tests switch() ar dažādām kombinācijām
print("\n2. Testing switch() operation:")
print("Switch first and last elements (0, 4):")
my_list.switch(0, 4)
my_list.read()

print("\nSwitch adjacent elements (1, 2):")
my_list.switch(1, 2)
my_list.read()

# 3. Tests pop() vairākas reizes
print("\n3. Testing pop() operation:")
print("After first pop():")
my_list.pop()
my_list.read()

print("\nAfter second pop():")
my_list.pop()
my_list.read()

# 4. Testing edge cases
print("\n4. Testing edge cases:")
print("Trying to switch invalid indices:")
my_list.switch(0, 10)  # Index out of range

print("\nTrying to pop from small list:")
my_list.pop()
my_list.pop()
my_list.pop()  # Last element
print("List after removing all elements:")
my_list.read()

print("\nTrying to pop from empty list:")
my_list.pop()  # Should print error message

# 5. Tests pievienot tukšajam listam pēc after clearing
print("\n5. Testing list rebuild:")
my_list.add("New Start")
my_list.add("New End")
print("Rebuilt list:")
my_list.read()