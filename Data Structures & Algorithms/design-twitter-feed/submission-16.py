class Twitter:

    def __init__(self):
        self.feed = defaultdict(list)
        self.followerMap = defaultdict(list)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.time,tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        followingList = self.followerMap[userId]
        allFollowingTweets = []
        for i in followingList:
            followingTweet = self.feed[i]
            for j in followingTweet:
                allFollowingTweets.append(j)
        userTweets = self.feed[userId]
        allFollowingTweets+=userTweets
        duplicates = set()
        heap = []
        for time,tweetId in allFollowingTweets:
            if time in duplicates:
                continue
            else:
                duplicates.add(time)
                heap.append((-time,tweetId))
        heapq.heapify(heap)
        res = []
        for i in range(10):
            if heap:
                val = heapq.heappop(heap)
                res.append(abs(val[1]))
            else:
                break

        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followerMap[followerId]:
            return
        self.followerMap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)


