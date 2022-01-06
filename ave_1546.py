subject_num = int(input('과목 개수: '))
score = []
for i in range(subject_num):
  subject = int(input('점수: '))
  score.append(subject)

max = max(score)
new_score = []
for i in score:
   i = i/max*100
   new_score.append(i)

average = sum(new_score)/subject_num
print('평균:',average)