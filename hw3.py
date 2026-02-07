
# your functions go here!

def insert(n, l):
    if l == []:
        return [n]
    else:
        head = l[0]
        tail = l[1:]
        tailResult = insert(n, tail)
        if n <= head:
            # problem: when recursively called, it keeps inserting for all values n <= 0
            return [n] + l
        else:
            return [head] + tailResult

def insertionSort(l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        tailResult = insertionSort(tail)
        return insert(head, tailResult)
       
       
       
       
       
def merge(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    else:
        headl1 = l1[0]
        headl2 = l2[0]
        taill1 = l1[1:]
        taill2 = l2[1:]
        if headl1 <= headl2:
            print(f"lessthan", [headl1] + merge(taill1, l2))
            return [headl1] + merge(taill1, l2)
        else:
            print(f"greaterthan",[headl2] + merge(l1, taill2))
            return [headl2] + merge(l1, taill2)
        # what if one list is empty, the other is not?
        
def mergeSort(l):
    if len(l) == 1: # base case - 
        return l
    else:
        mid = len(l)//2
        front = l[:mid]
        back = l[mid:]
        sortfront = mergeSort(front)
        sortback = mergeSort(back)
        return merge(sortback, sortfront)
    


        
# binary numbers

def toBinary(n):
    if n == 0:
        return '0' #how to get around if n == 0?
    if n == 1:
        return '1'
    else:
        if n % 2 == 1:
            return toBinary(n //2) + '1'
        elif n % 2 == 0:
            return toBinary(n//2) + '0'
            
def fromBinary(s): #to take a string
    if s == '':
        return 0
    else:
        head = s[0] #string and list can both do head tail recursion
        tail = s[1:]
        tailResult = fromBinary(tail)
        return int(tailResult) + int(head) * pow(2, len(s) - 1)
    



            
        


        
            
       