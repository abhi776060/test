class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class LinkList:
    def __init__(self):
        self.head=Node()
    
    def append(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.next!= None:
            cur =cur.next
        cur.next=new_node
    def length(self):
        cur=self.head
        total=0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total

    def display(self):
        elems=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
            
        print(elems)

my_list=LinkList()
my_list.append(1)
my_list.append(2)

my_list.display()
