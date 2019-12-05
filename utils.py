def readByte(f):
  return int.from_bytes(f.read(1), byteorder='little')
def readInt(f):
  return int.from_bytes(f.read(4), byteorder='little')
def readUTF8StopByte(f, stopByte = 0):
  len = 0
  curPos = f.tell()
  while readByte(f) != stopByte:
    len+=1
  f.seek(curPos)
  return f.read(len).decode('utf-8')
def writeByte(f, v):
  f.write((v).to_bytes(1, byteorder='little'))
def writeInt(f, v):
  f.write((v).to_bytes(4, byteorder='little'))
def writeUTF8StopByte(f, s, stopByte = 0):
  f.write(s.encode('utf-8'))
  writeByte(f, stopByte)
def utf8len(s):
  return len(s.encode('utf-8'))