class Stu(object):
  stu_count = 0
  #def __new__(cls):
    #print('Stu.__new__')
    #cls.gpa = 4.0

  def __init__(self,name='paul',grade=4.0):
    print('Stu.__init__')
    self.name = name
    self.grade = grade
    self.year = 1

  def __repr__(self):
    return f'{self.__class__.__name__}(name={self.name},grade={self.grade},year={self.year})'

  def __lt__(self,other):
    return self.year < other.year

  def study_hard(self):
    print('Sir, yes sir.')
  
