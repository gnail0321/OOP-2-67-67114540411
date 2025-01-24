class Stu(object):
  stu_count = 0
  def __new__(self):
    print('Stu.__new__')
  def __init__(self):
    print('Stu.__init__')
    self.gap=4.00

  def study_hard(self):
    print('Sir, yes sir.')
  
