half = {
  'open': [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
  ],
  'close': [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0]
  ]
}

full = {
  'open': [
    [1,0,0,0],
    [1,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
  ],
  'close': [
    [0,0,0,1],
    [0,0,1,0],
    [1,1,0,0],
    [1,0,0,0]
  ]
}

def getOpenHalf():
    return half.get('open')

def getOpenFull():
    return full.get('open')

def getCloseHalf():
    return half.get('close')

def getCloseFull():
    return full.get('close')