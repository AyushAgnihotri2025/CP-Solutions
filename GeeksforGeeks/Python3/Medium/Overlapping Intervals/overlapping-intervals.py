class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
        # Check if the Intervals list is empty
        if not Intervals:
            return Intervals
    
        # Sort the Intervals list by the start time
        Intervals.sort()
    
        # Initialize a variable to store the current interval
        current_interval = Intervals[0]
    
        # Initialize a list to store the merged Intervals
        merged_intervals = []
    
        # Iterate over the Intervals list
        for interval in Intervals:
            # If the current interval overlaps with the next interval
            if interval[0] <= current_interval[1]:
                # Update the end time of the current interval
                current_interval[1] = max(current_interval[1], interval[1])
            else:
                # Add the current interval to the merged Intervals list
                merged_intervals.append(current_interval)
                # Set the current interval to the next interval
                current_interval = interval
    
        # Add the current interval to the merged Intervals list
        merged_intervals.append(current_interval)
    
        # Return the merged Intervals list
        return merged_intervals

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends