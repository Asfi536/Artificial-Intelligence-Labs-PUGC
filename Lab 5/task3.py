import heapq

def process_queue():
    pq = []

    # Adding elements to the priority queue
    heapq.heappush(pq, (1, 'Task B'))
    heapq.heappush(pq, (0, 'Task A'))
    heapq.heappush(pq, (2, 'Task C'))

    # Processing elements based on their priority
    while pq:
        prio, task = heapq.heappop(pq)
        print("Priority Level:", prio, "Task:", task)

process_queue()
