numberNotes = int(input("Nombre de notes: "))
notes = 0
for i in range(numberNotes):
    note = float(input("-> "))
    notes += note
average = notes / numberNotes
print("Moyenne:", average)
