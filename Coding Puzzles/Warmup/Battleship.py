from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  # Write your code here
  grid = R * C
  numberOfOnes = 0
  for i in range(R):
    for j in range(C):
      if G[i][j] == 1:
        numberOfOnes += 1
  prob = numberOfOnes/grid
  return prob
