from Queue1 import Queue
from Printer import Printer
from Task import Task
from random import randrange


def simulation(numSeconds, pagePerMinute):
    """Return result of simulation of printer queue bellow numSeconds with
    a rate of pagePerMinute (Supposing that a task is complete once every 180
    seconds (probability), and the pages range from 1 to 20 pages."""
    printerQueue = Queue()
    labPrinter = Printer(pagePerMinute)
    waitingList = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            # If a new task is created we enqueue it to the queue with the
            # second it was enqueued.
            task = Task(currentSecond)
            printerQueue.enqueue(task)

        if not labPrinter.busy() and not printerQueue.isEmpty():
            nextTask = printerQueue.dequeue()  # Dequeue the next element.
            waitingTime = nextTask.waitTime(currentSecond)
            # This calculated how many time passed since the task was created
            # until it started to process. First task always 0.
            waitingList.append(waitingTime)
            labPrinter.startNext(nextTask)  # Only executed when the task is
            # done and there are more elements in queue.

        labPrinter.tick()

    avgWait = sum(waitingList) / len(waitingList)
    return "Avg time per task {:.2f} sec, {} tasks on queue."\
        .format(avgWait, printerQueue.size())


def newPrintTask():
    """To represent the probability to complete a task every 180 seconds."""
    num = randrange(1, 181)
    if num == 181:
        return True
    else:
        return False


for i in range(10):
    print(simulation(3600, 5))

