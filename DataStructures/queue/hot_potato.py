from DS.queue.Queue import Queue
from typing import List


def hot_potato(names: List[str], num: int):
    queue = Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size() > 1:
        turns = num
        # make turns up to num times
        while turns:
            # emulate the circle with queue, dequeue from one end and immediately enqueue back the same element
            queue.enqueue(queue.dequeue())
            turns -= 1
        # the last who holds "hot potato" after N turns is eliminated from the queue
        queue.dequeue()

    # the last item left in the queue is the answer
    return queue.dequeue()


if __name__ == "__main__":
    print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))