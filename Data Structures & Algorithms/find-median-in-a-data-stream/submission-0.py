class MedianFinder:

    def __init__(self):
        self.left = [] #max heap 
        self.right = [] #min heap
        
        #eg. list. [1,2,3,4,5]
        #top of max heap will have largest element in left part of list #[3,2,1]
        #top of min heap will have smallest element in right part of list #[4,5,6] 
        #top of max heap will be the median if length is odd, if even, it'll be avg of top of max and top of min heap (3+4)/2

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        heapq.heappush(self.right, -heapq.heappop(self.left))

        if len(self.left) < len(self.right):
            heapq.heappush(self.left,-heapq.heappop(self.right))

    def findMedian(self) -> float:
        
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0]+self.right[0])/2