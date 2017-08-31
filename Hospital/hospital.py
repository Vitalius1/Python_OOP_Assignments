from patient import Patient

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.hospital = []
        self.bed = []
        for x in range (capacity , 0, -1):
            self.bed.append(x)   # creates a list of numbers which will be used as beds.
        self.ids = []
        for y in range (100, 0, -1):
            self.ids.append(y)   # creates a list of numbers which will be used as ID

    def admit(self, patient):
        if len(self.hospital) < self.capacity:  # checks if the capacity of hospital is not full
            self.hospital.append(patient)  # put the instance of the patient passed in the method inside the hospital
            if patient.ID == None:   # checks if patient already was assigned an ID than do not assign another one 
                patient.ID = self.ids.pop()
            patient.bed_number = self.bed.pop()  # asigns a bed number to the patient instance and removes it from the list for beds
            print "You have been addmited."
            patient.show()
        else:    # if the capacity is reached and hospital is full than do not admit and display a sorry message
            print "Sorry we are full!"
            patient.show()
        return self
   
    def discharge(self, patient_name):
       for patient in self.hospital:
           if patient_name == patient.p_name:  # passing the name when we call the method we look for the patient with that name
               self.hospital.remove(patient)   # in the hospital and remove him from the list.
               self.bed.append(patient.bed_number)  # we give back the bed number to the bed list in order to be reused later
               patient.bed_number = None
               print "You have been discharged. Congratulations!!!"