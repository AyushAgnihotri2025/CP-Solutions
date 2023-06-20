#User function Template for python3

def isAdditiveSequence(num):
    #code here
    for i in range(len(num)//2):
        a=int(num[ :i+1])
        for j in range(i+1, len(num)-i-1):
            b=int(num[i+1:j+1])
            summ=str(a+b)
            idx, flag=0,True
            for k in range(j+1, len(num)):
                if idx==len(summ):
                    if isAdditiveSequence(num[ i+1:]):
                        return 1
                    flag=False
                    break
                if summ[idx]==num[k] :
                    idx+=1
                else:
                    break
            if idx==len(summ) and flag==True:
                return 1
    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        s=input()

        print(isAdditiveSequence(s))
# } Driver Code Ends