from DS.queue.PrintQueueDesign.Printer import Printer
from DS.queue.PrintQueueDesign.Task import Task
from DS.queue.Queue import Queue

import random


def new_print_task(students_num_in_class: int = 10):
    # there are N number of students
    # each student prints twice per hour
    tasks_per_hour = students_num_in_class * 2



    # for example, for 10 students - 2 * 10 = 20
    # 20 / (60 min * 60 sec) = 1 / 180
    # new need to print something appears every 180 seconds
    task_chance = 3600 // tasks_per_hour
    num = random.randrange(1, task_chance + 1)
    return num == task_chance


def simulation(seconds, page_per_minute):

    lab_printer = Printer(page_per_minute)
    print_queue = Queue()
    waiting_times = []

    for second in range(seconds):

        if new_print_task(students_num_in_class=100):
            task = Task(second)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task: Task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait_time = sum(waiting_times)/len(waiting_times)
    tasks_left_pending = print_queue.size()
    print("Average Wait %6.2f secs %3d tasks remaining."%( average_wait_time, tasks_left_pending))



if __name__ == "__main__":
    # start 10 simulation processes
    for i in range(10):
        # 1 hour time, 3600 sec
        time_period_in_seconds = 60 * 60
        simulation(time_period_in_seconds, 10)
