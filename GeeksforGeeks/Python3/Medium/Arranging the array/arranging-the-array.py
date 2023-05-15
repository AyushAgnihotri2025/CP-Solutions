#User function Template for python3

def Rearrange( a, n):
    # Your code goes here
    list1 = list()
    list2 = list()
    for i in a:
        if i<0:
            list1.append(i)
        else:
            list2.append(i)
    hello = list1+list2
    for i in range(n):
        a[i] = hello[i]
    return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Rearrange(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends