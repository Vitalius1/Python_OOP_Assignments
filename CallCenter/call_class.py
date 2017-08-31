# Creating the Call class
class Call(object):
    def __init__(self, caller_name, caller_phone, call_time, call_reason, caller_id=None):
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.call_time = call_time
        self.call_reason = call_reason
        self.caller_id = caller_id

    def display(self):
        print "Caller ID: " + str(self.caller_id)
        print "Caller Name: " + self.caller_name
        print "Caller Phone number: " + str(self.caller_phone)
        print "Time of the call: " + str(self.call_time)
        print "Call reason: " + self.call_reason