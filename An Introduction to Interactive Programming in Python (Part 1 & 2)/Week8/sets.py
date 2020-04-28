# Examples of Sets 

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

inst2 = set(['Warren', 'Rixner', 'Rixner', 'Rixner', 'Greiner', 'Wong'])
print inst2

print instructors == inst2

for inst in inst2:
    print inst

instructors.add('Colbert')
print instructors
instructors.add('Rixner')
print instructors

instructors.remove('Wong')
print instructors
#instructors.remove('Wong')
#print instructors

print 'Rixner' in instructors
print 'Wong' in instructors
