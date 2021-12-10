def minmax(*values):
  min = values[0]
  max = values[0]
  for i in values:
    if i > max:
      max = i
    elif i < min:
      min = i
  print(values,'min',min,',','max',max)

minmax(1,2,3,4,5)

def below_average(*scores):
  total = 0
  below = 0
  for i in scores:
    total += i
  average = total/len(scores)
  for k in scores:
    if k < average:
      below += 1
  return below

print(below_average(40,80,70,50,90))