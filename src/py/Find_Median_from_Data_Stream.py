"""
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/description/

min-heap for top half
max-heap for bottm half
if total num elements even then return mean(min-heap top, max-heap top)
if total num elements odd then 

1. insert in bottm half
2. check size between 2 heaps, if greater than one
    2.1 pop from bottom half and push to top half
3. check if top of bottom half is greater than top of top half
    3.1 swap these two value

[], []
[1], []
[1], [2] -> 2.5
[3,1], [2]
[2,1], [3] -> 2
"""
class MedianFinder:

    def __init__(self):
        self.top_half = []
        self.bottom_half = []

    def addNum(self, num: int) -> None:
        heappush(self.bottom_half, -num)
        if len(self.bottom_half) - len(self.top_half) > 1:
            top_bottom_half = -heappop(self.bottom_half)
            heappush(self.top_half, top_bottom_half)
        if self.bottom_half and self.top_half and -self.bottom_half[0] > self.top_half[0]:
            max_bottom_half = -heappop(self.bottom_half)
            min_top_half = heappop(self.top_half)
            heappush(self.bottom_half, -min_top_half)
            heappush(self.top_half, max_bottom_half)

    def findMedian(self) -> float:
        if (len(self.top_half) + len(self.bottom_half)) % 2:
            return -self.bottom_half[0]
        else:
            return (-self.bottom_half[0]+self.top_half[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
