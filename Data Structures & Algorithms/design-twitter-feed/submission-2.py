class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) #userid -> [(time, tweetid)]
        self.follows = defaultdict(set) #userid -> {followees}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1 #negative number -> maxHeap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            for t in self.tweets[followeeId]:
                res.append(t)
        heapq.heapify(res)
        
        print(res, self.follows[userId])
        nres = []
        while res and len(nres) < 10:
            time, tweetid = heapq.heappop(res)
            nres.append(tweetid)
        print(nres)

        return nres

       
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

       
