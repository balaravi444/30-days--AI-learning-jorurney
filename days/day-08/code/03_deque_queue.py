# Problem 3 -Queue Operations Using deque
# Day 08 - Collection Module

from collections import deque
queue = deque()
queue.append("Bala")
queue.append("Ravi")
queue.append("Kumar")
print("Queue:", queue)
print("Removed:", queue.popleft())
print("Queue after removal:", queue)
