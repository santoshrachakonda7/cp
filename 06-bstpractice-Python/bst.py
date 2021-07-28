class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        node = Node(new_val)
        if(self.root == None):
            self.root = node
        else:
            cur = self.root
            r = self.root
            while (cur != None):
                r = cur
                #should be moved left
                if(new_val < cur.value):
                    cur = cur.left
                #should be moved right
                else:
                    cur = cur.right
            if(new_val < r.value):
                r.left = node
            else:
                r.right = node

    def printSelf(self):
        # Your code goes here
        print(self.root)
        
    def search(self, find_val):
        # Your code goes here
        while(self.root!=None):
            #searching the value
            if(self.root.value > find_val):
                self.root = self.root.left 
            if(self.root.value < find_val):
                self.root = self.root.right
            else:
                return True
        return False

