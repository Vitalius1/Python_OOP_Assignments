from hospital import Hospital
from patient import Patient
# creating 6 instances of Patient class
p1 = Patient("Vitalie", "No allergies")
p2 = Patient("Diana", "No allergies")
p3 = Patient("Galina", "Yes")
p4 = Patient("Nicolae", "Yes")
p5 = Patient("Ion", "No allergies")
p6 = Patient("Olivia", "Yes")

# Create the hospital giving it a name and a capacity
hospital1 = Hospital("Braga", 5)

# Admiting the patients into the hospital
hospital1.admit(p1)
hospital1.admit(p2)
hospital1.admit(p3)
hospital1.admit(p4)
hospital1.admit(p5)
hospital1.admit(p6) # this patient will receive a message that hospital is full (capacity = 5) and will not be admited to it.
print

# Discharge a patient by his name and setting it's bed attribute to None, but he still keeps his ID in case he returns.
hospital1.discharge("Galina")
print                           # When the patient is discharged he gives the bed back to be reused by new patients.
hospital1.discharge("Nicolae")
print
hospital1.admit(p3)  # Testing the admition of 2 previous patients in case they come back they still have the same ID
hospital1.admit(p4)  # but reusing beds left by other users