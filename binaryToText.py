import sys
import os
import utils

def convert(file):
  print(file)
  filename, _ = os.path.splitext(file)

  f = open(file, "rb")

  f.seek(8) # skip first 8 unk bytes

  pointersOffset = utils.readInt(f)
  pointersLength = utils.readInt(f)
  lineCount = utils.readInt(f)
  linesOffset = pointersOffset + pointersLength

  f.seek(pointersOffset)

  linesOffsetList = []
  currentLineOffset = utils.readInt(f)

  for _ in range(lineCount):
    linesOffsetList.append(currentLineOffset)
    currentLineOffset = utils.readInt(f)

  linesOffsetList.append(currentLineOffset)

  f.seek(linesOffset)

  d = open(filename + '.txt', 'w', encoding='utf-8')
  for i in range(lineCount):
    f.seek(linesOffset + linesOffsetList[i])
    d.write(utils.readUTF8StopByte(f).replace('\n', '\\n'))
    d.write('\n')

  d.close()
  f.close()

for i in range(1, len(sys.argv)):
  convert(sys.argv[i])

os.system("pause")