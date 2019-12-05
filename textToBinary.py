import sys
import os
import utils

def convert(file):
  print (file)
  lines = []
  filename, _ = os.path.splitext(file)

  with open(file, 'r', encoding='utf-8') as f:
    for line in f:
      lines.append(line[:-1].replace('\\n', '\n'))
  f.close()

  d = open(filename + '.bin', 'wb')

  pointersOffset = 0x20
  pointersLength = (len(lines) * 4) + ((len(lines) * 4) % 0x10)
  lineCount = len(lines)
  linesOffset = pointersOffset + pointersLength

  utils.writeInt(d, 1)
  utils.writeInt(d, 1)
  utils.writeInt(d, pointersOffset)
  utils.writeInt(d, pointersLength)
  utils.writeInt(d, lineCount)

  d.seek(pointersOffset)

  currentOffset = 0
  for line in lines:
    utils.writeInt(d, currentOffset)
    tempOffset = d.tell()
    d.seek(linesOffset + currentOffset)
    utils.writeUTF8StopByte(d, line)
    d.seek(tempOffset)
    currentOffset += utils.utf8len(line)+1

  utils.writeInt(d, currentOffset)

  d.close()
for i in range(1, len(sys.argv)):
  convert(sys.argv[i])

os.system("pause")