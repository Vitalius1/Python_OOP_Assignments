from call_class import Call

# Creating the class CallCenter
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
        self.id_pool = []            # we create an ID pool so that when a call is added to the queue the call   
        for x in range(100, 0, -1):  # center has available IDs to asign to the newly created call
            self.id_pool.append(x)

    def add(self, call):
        self.calls.append(call)             # adds call to the calls list
        call.caller_id = self.id_pool.pop() # asigns an ID to the call
        self.queue_size += 1                # incrementing the size of the queue
        return self

    def remove(self):
        self.calls = self.calls[1:] # removes the call at index 0 from the calls list
        self.queue_size -= 1        # decrementing the size of the queue
        return self

    def ninja_remove(self, phone):
        for call in self.calls:
            if phone == call.caller_phone:  # checking if the number passed when method is called is equal to any phone number
                self.calls.remove(call)     # in the call instances. If yes than remove that instance from the calls list
                self.queue_size -= 1        # decrementing the size of the queue
                print "Patient with requested number removed from queue."

    def sort(self):   # Using a build in function to sort the calls list.
        self.calls = sorted(self.calls, key=lambda call: call.call_time)

    def info(self):
        for call in self.calls:
            print "Call ID: {}. / Caller's name: {}. / Phone#: {}. / Call TIME: {}.".format(call.caller_id, call.caller_name, call.caller_phone, call.call_time)
            print "================"
        print "There are " + str(self.queue_size) + " calls in the queue!"
        print
        print
