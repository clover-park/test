def cal_score(list):
  count = 0
  score = 0
  for i in list:
    if i == 'O':
      count += 1
      score += count
    if i == 'X':
      count = 0
  return score

answer_list = []

while True:
  answer = input('답을 입력하세요: ')
  if answer == 'O' or answer == 'X': 
    answer_list.append(answer)
  else:
    break

print('점수: ',cal_score(answer_list))