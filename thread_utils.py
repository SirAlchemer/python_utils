import queue

q = queue.Queue()  # Initialize the queue here

def add_to_queue(data):
    q.put(data)

def get_dict_from_queue(filter=None):
    try:
        data = q.get(block=False)  # Try to get data without blocking
    except queue.Empty:
        print('Queue is empty')
        return None

    if filter is not None:
        if filter in data:  # Check if filter key exists in the dictionary
            return data[filter]
        else:
            print('Error data not found')
            return None
    else:
        return data

def get_from_queue():
    try:
        data = q.get(block=False)
        return data  # Try to get data without blocking
    except queue.Empty:
        print('Queue is empty')
        return None
