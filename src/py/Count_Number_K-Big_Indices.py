class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        heap = []
        forward_iteration, backward_iteration = set(), set()
        for i,num in enumerate(nums):
            if len(heap)<k:
                heappush(heap, -num)
                continue
            if num>-heap[0]:
                forward_iteration.add(i)
            heappush(heap, -num)
            heappop(heap)
            
            
            
        heap = []
        for i,num in enumerate(nums[::-1]):
            if len(heap)<k:
                heappush(heap, -num)
                continue
            if num>-heap[0]:
                backward_iteration.add(len(nums)-1-i)
            heappush(heap, -num)
            heappop(heap)
            
        # print(forward_iteration, backward_iteration )
        
        return len(forward_iteration.intersection(backward_iteration))
            
            
