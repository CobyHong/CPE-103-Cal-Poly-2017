from event_queue import *
import sys
 
def print_each_second(equeue):
   print('\ttime {}: every one'.format(equeue.time))
   add_event(equeue, print_each_second, 1)

def print_5_second(equeue):
   print('\ttime {}: every 5'.format(equeue.time))
   add_event(equeue, print_5_second, 5)
 
 
def stop(equeue):
   print('\ttime {}: stopping'.format(equeue.time))
   sys.exit(0)
 
def test(equeue):
   print('\ttime {}: minecraft rules at 15'.format(equeue.time))
 
if __name__ == '__main__':
   equeue = EventQueue()
 
   add_event(equeue, stop, 20)
   add_event(equeue, print_each_second, 1)
   add_event(equeue, print_5_second, 5)
   add_event(equeue, test, 15)
 
   run_events(equeue)