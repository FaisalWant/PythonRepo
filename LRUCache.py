
CAPACITY=4
class Node: 
    
    def __init__(self, id, data): 
        self.id=id 
        self.data= data 
        self.previous_node= None 
        self.next_node=None  



class DoublyLinkedList: 

    def __init__(self): 
        self.head=None 
        self.tail=None 



class LRUCache: 

    def __init__(self): 
        self.actual_size=0 
        self.dictionary={}
        self.linked_list= DoublyLinkedList() 

    def put(self, id, data): 
        if id in self.dictionary: 
            node= self.dictionary(id) 
            node.data= data 
            self.update(node) 
            return 

        node =Node(id, data) 
        if self.actual_size < CAPACITY: 
            self.actual_size= self.actual_size+1 
            self.add(node) 
        else: 
            self.remove_tail() 
            self.add(node)    # to the begining of the list 

    def add(self, node): 

        node.next_node= self.linked_list.head 
        node.previous_node= None 

        if self.linked_list.head: 
            self.linked_list.head.previous_node= node 

        
        self.linked_list.head= node 

        if not self.linked_list.tail: 
            self.linked_list.tail= node 

        self.dictionary[node.id]= node 
    
    def remove_tail(self): 
        
        last_node= self.dictionary[self.linked_list.tail.id] 

        del self.dictionary[self.linked_list.tail.id] 

        self.linked_list.tail= self.linked_list.tail.previous_node 

        if self.linked_list.tail: 
            self.linked_list.tail.next_node= None 

        
        last_node= None 
    

    def get(self, id): 

        if not self.dictionary[id]: 
            return None 
        node = self.dictionary[id] 

        self.update(node) 

        return node 
    

    def update(self, node): 
        previous_node= node.previous_node 
        next_node= node.next_node 


        if previous_node: 
            previous_node.next_node= next_node 
        
        else: 
            self.linked_list.head= next_node 
        

        if next_node: 
            next_node.previous_node= previous_node 
        
        else: 
            self.linked_list.tail= previous_node

        self.add(node) 



    def show(self): 
        actual_node= self.linked_list.head 

        while actual_node: 
            print("%s->"% actual_node.data) 
            actual_node= actual_node.next_node 





if __name__ == "__main__": 
    cache= LRUCache() 
    cache.put(0, "google.com") 


