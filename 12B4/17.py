queue = []
max_size = 5

def enqueue(queue, item, max_size):
    if len(queue) == max_size:
        print("Queue is full")
        return    
    queue.append(item)


insert = [10, 20, 30]  
for item in insert:
    enqueue(queue, item, max_size)
    
print(queue)