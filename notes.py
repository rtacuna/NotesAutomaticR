import sys
import os

class NoteAutomatic2():

  def __init__(self):
    self.fileName = 'rNota'
    self.fileFolder = ''
    self.fileExtention = ''

  def getArgs(self):
    self.fileFolder = str(sys.argv[1])
    self.fileExtention = '.txt'
  
  def createNote(self):
    os.chdir(self.fileFolder)
    name = self.fileName + self.fileExtention
    if not os.path.isfile('./' + name):
      open(name, 'a').close()
    os.system('subl ' + name)


if __name__ == '__main__':
  note = NoteAutomatic2()
  note.getArgs()
  note.createNote()
