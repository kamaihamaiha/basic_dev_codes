from die import Die


die = Die()

results = []
for roll_num in range(100):
    results.append(die.roll())

print(results)    