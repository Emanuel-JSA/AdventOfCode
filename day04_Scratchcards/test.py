with open('F:\\Projects\\AdventOfCode\\day04_Scratchcards\\data.txt') as f:
  l = f.readlines()
  lines = [entry.strip() for entry in l]

def firstPuzzleSolution(lines):
  firstTaskResult = 0

  for line in lines:
    twoCardsList = [cardList.strip() for cardList in line.split(': ')[1].split('|')]
    [winningCardList, guessingCardList] = [map(int, filter(None, cardList.split(' '))) for cardList in twoCardsList]
    numberOfWinningCards = len(list(set(winningCardList).intersection(guessingCardList)))
    if numberOfWinningCards > 0: firstTaskResult += 2**(numberOfWinningCards-1)
  
  return firstTaskResult

print(firstPuzzleSolution(lines))