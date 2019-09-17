from collections import deque  # imporing dequeue from the collection module
# dequeue is a class
queue = deque([])  # wrapping queue list with a dequeue object
queue.append(1)  # enter item in queue
queue.append(2)
queue.append(3)
queue.popleft()  # remove item from the beginning of the queue
queue.popleft()
# queue.popleft()
print(queue)

if not queue:  # if we have an empty queue
    print('Empty')
