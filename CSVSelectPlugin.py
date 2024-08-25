import PyPluMA
import PyIO

class CSVSelectPlugin:
    def input(self, infile):
      self.parameters = PyIO.readParameters(infile)
      filestuff = open(PyPluMA.prefix()+"/"+self.parameters["csvfile"], 'r')
      self.lines = []
      for line in filestuff:
         self.lines.append(line.strip().split(','))

      filestuff2 = open(PyPluMA.prefix()+"/"+self.parameters["keepfile"], 'r')
      self.keep = [0]
      for line in filestuff2:
          self.keep.append(self.lines[0].index(line.strip()))
      self.keep.sort()

    def run(self):
      pass

    def output(self, outfile):
      outputfile = open(outfile, 'w')
      for i in self.keep:
         for j in range(len(self.keep)):
             outputfile.write(self.lines[i][self.keep[j]])
             if (j != len(self.keep)-1):
                 outputfile.write(',')
         outputfile.write('\n')
