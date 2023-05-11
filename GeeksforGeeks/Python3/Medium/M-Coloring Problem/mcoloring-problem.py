#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    #your code here
    color = [0] * V
    return solve(0, graph, k, V, color)

def is_safe(node, curr_col, graph, m, n, color):
    for i in range(n):
        if i != node and graph[i][node] and color[i] == curr_col:
            return False
    return True

def solve(node, graph, m, n, color):
    if node == n:
        return True
    for i in range(1, m + 1):
        if is_safe(node, i, graph, m, n, color):
            color[node] = i
            if solve(node + 1, graph, m, n, color):
                return True
            color[node] = 0
    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends