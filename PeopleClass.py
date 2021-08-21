class student:
    def __init__(self, name, average, uni, program):
        self.name = name
        self.average = float(average)
        self.uni = uni
        self.program = program

    def get_attributes(self):
      return self.name, self.average, self.uni, self.program
    
    def get_program(self):
      return self.program

    def get_uni(self):
      return self.uni

    def get_average(self):
      return self.average

    