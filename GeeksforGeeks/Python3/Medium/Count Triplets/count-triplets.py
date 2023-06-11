#User function Template for python3

def countTriplets(head,x):
    # code here
    curr1 = head
    answer = []
    while curr1:
        hashmap = {}
        curr2 = curr1.nxt
        while curr2:
            value = x - (curr1.val + curr2.val)
            if value in hashmap:
                answer.append([curr1.val, curr2.val, value])
            else:    
                hashmap[curr2.val] = 1
            curr2 = curr2.nxt
        curr1 = curr1.nxt
    return len(answer)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.val=x
        self.nxt=None

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        x = int(line[1])
        line = input().strip().split()
        
        head = Node(int(line[0]))
        tail = head
        for i in range(1,n):
            tail.nxt = Node(int(line[i]))
            tail = tail.nxt
        
        print(countTriplets(head,x))


# } Driver Code Ends