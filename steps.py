open_sequence = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

def getOpenSequence():
  return open_sequence

def getCloseSequence():
  close_sequence = []
  last_index = len(open_sequence) - 1
  for i in range(len(open_sequence)):
    index = last_index - i
    close_sequence.append(open_sequence[index])
  return close_sequence
