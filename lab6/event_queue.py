from priority_queue import *
import time

# An Event Queue is an
# EventQueue(pQueue, time)

class EventQueue:

    def __init__(self):

        self.pQueue = empty_pqueue(event_comes_before) # A PriorityQueue representing the queue from which functions will be called.
        self.time = 0 # An integer representing the internal time.

    def __eq__(self, other):

        return (type(other) == EventQueue
                and self.pQueue == other.pQueue
                and self.time == other.time
                )

    def __repr__(self):

        return "Queue: %r Internal Time: %r" % (self.pQueue, self.time)

# An Event is an
# Event(func, time)

class Event:

    def __init__(self, func, time):

        self.func = func # A function representing what should be called when this event is ready.
        self.time = time # An integer representing the seconds required to run the event.

    def __eq__(self, other):

        return (type(other) == Event
                and self.func == other.func
                and self.time == other.time
                )

    def __repr__(self):

        return "Function: %r Scheduled Time: %r" % (self.func, self.time)

# Event Event -> Boolean
# Checks to see whether an event's scheduled time comes before another's.

def event_comes_before(event1, event2):

    return event1.time < event2.time

# EventQueue func int -> None
# Adds an event to a queue.
def add_event(eQueue, func, delay):

    eQueue.pQueue = enqueue(eQueue.pQueue, Event(func, delay + eQueue.time))


# EventQueue -> None
# Runs all events in an event queue.S
def run_events(eQueue):

    queue = eQueue.pQueue
    first_event = queue.plist.first
    while first_event.time != eQueue.time:

        time.sleep(1)
        eQueue.time += 1

    first_event.func(eQueue)
    eQueue.pQueue = dequeue(eQueue.pQueue)[1]
    run_events(eQueue)
    

