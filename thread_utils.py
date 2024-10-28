import queue
import threading

q = queue.Queue()  # Initialize the queue here

# ______add_to_queue_______#
def add_to_queue(data):
    """
    Adds data to the queue.
    """
    q.put(data)

# ______get_dict_from_queue_______#
def get_dict_from_queue(filter=None):
    """
    Retrieves a dictionary from the queue.
    If a filter is provided, it will return the value associated with that key.
    """
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

# ______get_from_queue_______#
def get_from_queue():
    """
    Retrieves data from the queue.
    """
    try:
        data = q.get(block=False)
        return data  # Try to get data without blocking
    except queue.Empty:
        print('Queue is empty')
        return None

# ______get_all_from_queue_______#
def get_all_from_queue():
    """
    Retrieves all data from the queue.
    """
    data_list = []
    while not q.empty():
        try:
            data = q.get(block=False)
            data_list.append(data)
        except queue.Empty:
            break
    return data_list

# ______queue_size_______#
def queue_size():
    """
    Returns the current size of the queue.
    """
    return q.qsize()

# ______is_queue_empty_______#
def is_queue_empty():
    """
    Returns True if the queue is empty, False otherwise.
    """
    return q.empty()

# ______clear_queue_______#
def clear_queue():
    """
    Clears the queue.
    """
    while not q.empty():
        try:
            q.get(block=False)
        except queue.Empty:
            break

# ______queue_thread_______#
def queue_thread(target, args=()):
    """
    Creates a new thread that runs the target function with the given arguments.
    """
    t = threading.Thread(target=target, args=args)
    t.start()
    return t

# ______queue_daemon_thread_______#
def queue_daemon_thread(target, args=()):
    """
    Creates a new daemon thread that runs the target function with the given arguments.
    """
    t = threading.Thread(target=target, args=args)
    t.daemon = True
    t.start()
    return t
