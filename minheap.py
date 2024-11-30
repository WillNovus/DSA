# Using heapq to create a min heap.

import heapq

#create a min-heap in python
heap = [8, 4, 1, 7]
heapq.heapify(heap)

print ("Min-Heap:", heap)

min_element = heapq.heappop(heap)

heapq.heappush(heap, 3)

print("Min Element:", min_element)
print("Min-Heap: ", heap)
