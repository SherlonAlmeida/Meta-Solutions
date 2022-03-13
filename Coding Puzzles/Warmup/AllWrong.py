# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  wrong_answers = ""
  # Write your code here
  for i in range(N):
    if C[i] == 'A':
      wrong_answers += 'B'
    else:
      wrong_answers += 'A'
  return wrong_answers
