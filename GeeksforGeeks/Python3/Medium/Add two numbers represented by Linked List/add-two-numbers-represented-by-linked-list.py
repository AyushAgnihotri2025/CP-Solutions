#User function Template for python3

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class llist:
    def __init__(self):
        self.head=None
        self.tail=None
        
class carry_data:
    def __init__(self):
        self.data=0
'''

def reverse(head):
    prev=None
    cur=head
    while(cur):
        tmp=cur.next
        cur.next=prev
        prev=cur
        cur=tmp
    return prev

#Function which adds two linked lists of same size represented by head1 
#and head2 and returns head of the resultant linked list. Carry
#is propagated while returning from the recursion
def addSameSize(h1,h2,carry):
    
    '''
    param: h1,h2: head of linked list 1 and 2
    param: carry: is instance of carry_data class, used to store carry
    return: head of resultant linked list(same size), and set the carry data, so that it could be added further
    '''
    # code here
    h1,h2=reverse(h1),reverse(h2)
    cur1,cur2=h1,h2
    c=0
    while(cur1 and cur2):
        tmp=cur1.data+cur2.data+c
        cur1.data=tmp%10
        c=tmp//10
        cur1,cur2=cur1.next,cur2.next
    carry.data=c
    return reverse(h1)



#This function is called after the smaller list is added to the sublist of 
#bigger list of same size. Once the right sublist is added, the carry
#must be added to left side of larger list to get the final result.
def addCarryToRemaining(h1,curr,result,carry):
    
    '''
    param: h1:      head of largest linked list
    param: curr:    node till largest linked list has been added
    param: result:  resultant linked list(not head),formed from above function
    param: carry:   is instance of carry_data class, used to store carry,
    
    return: None,   set new resultant head to result linklist.
    '''
    # code here
    h1,c=reverse(h1),carry.data
    curr=curr.next
    while(curr):
        tmp=curr.data+c
        curr.data=tmp%10
        c=tmp//10
        curr=curr.next
    carry.data=c
    result.head=reverse(h1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class llist:
    def __init__(self):
        self.head=None
        self.tail=None
        
class carry_data:
    def __init__(self):
        self.data=0
        
def append(h,t,data):
    if not h:
        h=Node(data)
        return (h,h)
    else:
        t.next=Node(data)
        return (h,t.next)

def push(head,data):
    
    nn=Node(data)
    nn.next=head
    return nn


def printlist(head):
    
    while head:
        print(head.data,end=' ')
        head=head.next
    print()
    
def addList(head1,head2,size1,size2,result,carry):
    if not head1:
        result.head=head2
        return
        
    if not head2:
        result.head=head1
        return
    
    
    if size1==size2:
        result.head=addSameSize(head1,head2,carry)
    else:
        diff=abs(size1-size2)
        
        if size1<size2:
            head1,head2=head2,head1
            
        cur=head1
        for _ in range(diff):
            cur=cur.next
            
        result.head=addSameSize(cur,head2,carry)
        
        addCarryToRemaining(head1,cur,result,carry)
        
       
    if carry.data!=0:
        result.head=push(result.head,carry.data)
    
        
    


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        size1,size2 = list(map(int, input().strip().split()))
        nodes1 = list(map(int, input().strip().split()))
        nodes2 = list(map(int, input().strip().split()))
        
        ll1=llist()
        ll2=llist()
        result=llist()
        carry=carry_data()
        
        for e in nodes1:
            ll1.head,ll1.tail=append(ll1.head,ll1.tail,e)
        
        for e in nodes2:
            ll2.head,ll2.tail=append(ll2.head,ll2.tail,e)
        
        
        addList(ll1.head,ll2.head,size1,size2,result,carry)
        
        printlist(result.head)
# } Driver Code Ends