import threading


class QueueManager(threading.Thread):
    def __init__(self, target, input_queue, args=(), kwargs={}):
        self.ipq = input_queue
        kwargs['ipq'] = input_queue

        super(QueueManager, self).__init__(target=target,
                                           args=args,
                                           kwargs=kwargs
                                           )

    def run(self):
        try:
            super(QueueManager, self).run()
        except Exception as e:
            print e
            raise


