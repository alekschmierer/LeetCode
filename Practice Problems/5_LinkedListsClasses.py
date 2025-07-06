# class Card():
#     def  __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#     def print_card(self):
#         print(f"{self.rank} of {self.suit}")
#     def is_valid(self):
#         validSuit = ["Hearts", "Spades", "Clubs", "Diamonds"]
#         validRank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#         if self.suit not in validSuit:
#             return False
#         if self.rank not in validRank:
#             return False
#         return True
#     def get_value(self):
#         hasRank = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
#         if self.rank in hasRank:
#             return int(self.rank)
#         elif self.rank == "Ace":
#             return 1
#         elif self.rank == "Jack":
#             return 11
#         elif self.rank == "Queen":
#             return 12
#         elif self.rank == "King":
#             return 13
#         else:
#             return None

# # card = Card("Spades", "8")

# # card = Card("Clubs", "Ace")
# # card.suit = "Hearts"
# # card.print_card()

# # my_card = Card("Hearts", "7")
# # print(my_card.is_valid())

# # second_draw = Card("Spades", "Joker")
# # print(second_draw.is_valid())

# card = Card("Hearts", "7")
# print(card.get_value())

# card_two = Card("Spades", "Jack")
# print(card_two.get_value())

# class Pokemon():
#     def  __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp # hit points
#         self.damage = damage # The amount of damage this pokemon does to its opponent every attack

#     def attack(self, opponent):
#         opponent.hp -= self.damage
#         if opponent.hp <= 0:
#             opponent.hp = 0
#             print(f"{opponent.name} fainted")
#         else:
#             print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

# # pikachu = Pokemon("Pikachu", 35, 20)
# # bulbasaur = Pokemon("Bulbasaur", 45, 30) 

# # opponent = bulbasaur
# # pikachu.attack(opponent)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def add_first(head, newNode):
#     head.next = None
#     newNode.next = head

#     return newNode

# def get_tail(head):
#     if head is None:
#         return None
#     else:
#         while head.next is not None:
#             head = head.next
#         return head.value

# def ll_replace(head, original, replacement):
#     if head is None:
#         return None
#     else:
#         while head is not None:
#             if head.value == original:
#                 head.value = replacement
#             head = head.next
            
#         return head
        
# def listify_first_n(head, n):
#     counter = 0
#     newList = []
#     if head is None:
#         return None
#     while head is not None and counter < n:
#         newList.append(head.value)
#         head = head.next
#         counter += 1
#     return newList

# def ll_insert(head, val, i):
#     counter = 0
#     if head is None:
#         return None
#     while head is not None and counter != i-1:
#         head = head.next
#         counter += 1
#     newNode = Node(val, None)
#     if head.next is not None:
#         tempVariable = head.next
#         head.next = newNode
#         newNode.next = tempVariable
#     else:
#         head.next = newNode
        
#     return head
        
# def list_to_linked_list(lst):
#     if not lst:
#         return None

#     tail = Node(lst[-1])  # Start with the last element
#     for i in range(len(lst) - 2, -1, -1):  # Go backwards
#         tail = Node(lst[i], tail)  # Create new head each time, link to tail
#     return tail  # 'tail' is now the head of the linked list

            

# node_3 = Node("PuffyPuf", next=None)
# node_2 = Node("Wigglytuff", next=node_3)
# node_1 = Node("Jigglypuff", next=node_2)

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

# # Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# print(node_1.value, "->", node_1.next.value)

# linked list: num1->num2->num3
# head = node_1
# tail = get_tail(node_1)
# print(tail)

# num3 = Node(5)
# num2 = Node(6, num3)
# num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

# head = num1
# ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"

# while head is not None:
#     print(head.value)
#     head = head.next


# c = Node("c")
# b = Node("b", c)
# a = Node("a", b)
# head = a
# lst = listify_first_n(head,1)
# print(lst)

# four = Node(9)
# three = Node(12, four)
# two = Node(8, three)
# one = Node(3, two)
# head = one
# ll_insert(head, 20, 2)
# while head is not None:
#     print(head.value)
#     head = head.next

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

#We need to insert a newNode as the head of a linked list
# Need to set the newNode.next head
# Need to check if the head even exists
# Return the newNode
def add_first(head, val):
    if head:
        newNode = Node(val, head)
        return newNode
    else:
        return head
    
# Linked List: A -> B -> C
# New List: 0 -> A -> B -> C
node_c = Node("C", None)
node_b = Node("B",node_c)
node_a = Node("A",node_b)
# new_list = add_first(node_a, 0)
# while(new_list is not None):
#     print(new_list.value, end='')
#     new_list = new_list.next
# print()

# Must return length of linked list
# Set a counter while iterating through list
# Move head forward with counter
def ll_length(head):
    counter = 0
    if head:
        while(head is not None):
            counter+=1
            head = head.next
    return counter
# head = node_a
# print(ll_length(head))

# Must delete the tail element from the linked list
# Check to see if linked list even exists
# delete tail means that list must have two nodes, one as head and one as tail

def delete_tail(head):
    if head:
        while head.next.next is not None:
            print(head.value,head.next)
            head = head.next
        head.next = None
        print(head.value,head.next)

# newList = delete_tail(node_a)


def find_max(head):
    maxValue = head.value
    while head is not None:
        if head.value > maxValue:
            maxValue = head.value
        head = head.next
    return maxValue


node_4 = Node(10, None)
node_3 = Node(30, node_4)
node_2 = Node(15,node_3)
node_1 = Node(20,node_2)

# linked list: num1 -> num2 -> num3 -> num4
# max_val = find_max(node_1)
# print(max_val)


# We take in an index number and pop that node from the list
# Linked list is 0 based indexing
# If i is greather than list length do nothing

def ll_pop(head, i):
    if head:
        counter = 1 #setting to 1, this allows us to stop one before the node so we can set the next to the next next node
        while head.next is not None and counter != i:
            head = head.next
            counter += 1
        if head.next == None:
            return head
        head.next = head.next.next
    return head

# new_list = ll_pop(node_1, 1)
# while(new_list is not None):
#     print(new_list.value)
#     new_list = new_list.next


#Remove the middle node
# If linked list length is odd, remove one node
# If linked list length is even, remove two nodes
# Use list_length and ll_pop methods
def find_middle_node(head):
    listLength = ll_length(head)
    if listLength <= 2:
        return None
    
    if listLength %2 == 0: #If even
        index1 = listLength/2 - 1
        index2 = index1
        ll_pop(head,index1)
        ll_pop(head,index2)
    else: 
        index = listLength//2
        ll_pop(head,index)
    
    return head

# new_list = find_middle_node(node_1)
# while(new_list is not None):
#     print(new_list.value)
#     new_list = new_list.next

head = Node("Ice")
middle = Node("Water")
tail = Node("Steam")

head.next = middle
middle.prev = head

tail.next = None
tail.prev = middle

# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)

class SLLNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class DLLNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

# Traverse dll and create newNode's with the sll data structure
def dll_to_sll(dll_head):
    counter = 0
    sll_head = None
    while dll_head.next is not None:
        dll_head = dll_head.next
        counter += 1
    while counter != 0:
        counter -= 1
        add_first(sll_head,dll_head.value)
        dll_head = dll_head.prev
    return sll_head

new_list = dll_to_sll(head)
while(new_list is not None):
    print(new_list.value)
    new_list = new_list.next