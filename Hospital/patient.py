class Patient(object):
    def __init__(self, p_name, allergies, ID = None, bed_number = None):
        self.ID = ID
        self.p_name = p_name
        self.allergies = allergies
        self.bed_number = bed_number

    def show(self):
        print "name: {}, allergies: {}, ID: {}, Bed: {}".format(self.p_name, self.allergies, self.ID, self.bed_number)