from die import Die

die_1 = Die()

for loop in range(1, 10):
	die_1.roll_die()

print("10 sides die:")
die_1 = Die(10)	
for loop in range(1, 10):
	die_1.roll_die()


print("20 sides die:")
die_1 = Die(20)	
for loop in range(1, 10):
	die_1.roll_die()	