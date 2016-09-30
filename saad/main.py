"""
Nothing
"""
from six.moves import queue
from saad.manage import QueueManager
from saad.tar import backup_stream
from saad.tar import storage
from datetime import datetime
import sys


def handle_queue():
    print "Start queue handler"
    pipe_queue = queue.Queue(maxsize=3)
    print "pipe queue created !"
    imq = QueueManager(backup_stream,
                       pipe_queue,
                       kwargs={'path': '/home/saad/Desktop/dev/learn/freezerp/files_saad/'})
    print "First thread initialized !"
    smq = QueueManager(storage,
                       pipe_queue,
                       kwargs={
                           'path':
                               '/home/saad/Desktop/dev/learn/freezerp/bksaad/'
                       })
    print "Second thread initialized !"
    imq.daemon = True
    smq.daemon = True
    imq.start()
    print "Started first daemon thread"
    smq.start()
    print "Started second daemon thread"
    imq.join()
    print "First daemon thread joined !"
    smq.join()
    print "Second daemon thread joined !"
    print pipe_queue.empty()


def main():
    start = datetime.now()
    print "Welcome to our test !!!"
    print "Let's hope this will be your lucky day !"
    handle_queue()
    print "Done !"
    end = datetime.now()
    print "Time: {0}".format(end-start)


if __name__ == "__main__":
    print "started !"
    sys.exit(main())
