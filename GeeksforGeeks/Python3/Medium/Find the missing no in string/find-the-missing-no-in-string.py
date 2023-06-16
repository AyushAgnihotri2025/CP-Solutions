# your task is to complete this function
# function should return the missing number
# else return -1
def missingNumber(string):
    # Code here
    s = ""
    for i in range(len(string)):
        if i >= 6:
            break
        s += string[i]
        j = i + 1
        s1 = s
        s2 = ""
        f = 0
        while j < len(string):
            s1 = str(int(s1) + 1)
            k = string.find(s1, j)
            if k != -1 and j == k:
                j = j + len(s1)
            else:
                if f:
                    break
                f = 1
                s2 = s1
        if f and j >= len(string):
            return int(s2)
    return -1

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        string = input().strip()
        print(missingNumber(string))
# Contributed by: Harshit Sidhwa

# } Driver Code Ends