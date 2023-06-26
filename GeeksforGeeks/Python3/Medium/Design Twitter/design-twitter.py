#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

from collections import defaultdict

class Twitter:
    def __init__(self):
        self.followers = defaultdict(list)
        self.tweets = []
        
    # Compose a new tweet
    def postTweet(self, userId: int, tweetId: int):
        # Code here
        if userId not in self.followers:
            self.followers[userId] = [userId]
        self.tweets.append((userId, tweetId))
        
    # Retrieve the 10 most recent tweet ids as mentioned in question
    def getNewsFeed(self, userId: int):
        # Code here
        result = []
        count = 1
        index = len(self.tweets)-1
        while count<11 and index>-1:
            if self.tweets[index][0] in self.followers[userId]:
                result.append(self.tweets[index][1])
                count += 1
            index -= 1
        return result
        
    # Follower follows a followee. If the operation is invalid, it should be a no-op.
    def follow(self, followerId: int, followeeId: int):
        # Code here
        if followerId not in self.followers:
            self.followers[followerId] = [followerId]
        self.followers[followerId].append(followeeId)
        
    # Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    def unfollow(self, followerId: int, followeeId: int):
        # Code here
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    obj = Twitter()
    totalQueries = int(input ())
    for _ in range (totalQueries):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            userId, tweetId = query[1], query[2]
            obj.postTweet(userId, tweetId)
        elif (query[0] == 2):
            userId =  query[1]
            vec = obj.getNewsFeed(userId)
            for val in vec:
                print(val, end = ' ')
            print()
        elif (query[0] == 3):
            follower, followee = query[1], query[2]
            obj.follow(follower, followee)
        else:
            follower, followee = query[1], query[2]
            obj.unfollow(follower, followee)
# } Driver Code Ends