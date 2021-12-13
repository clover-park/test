def ave(list):
  total = 0
  for k in list:
    total += k
  average = total/case
  return average

def above_average(list):
  above_ave = 0
  for l in list:
    if l > ave(list):
      above_ave += 1
    percentage = above_ave/case*100
  return percentage

score_list = []
case = int(input())

for i in range(case):
  score = int(input())
  score_list.append(score)

print('%.3f%%'%(above_average(score_list)))