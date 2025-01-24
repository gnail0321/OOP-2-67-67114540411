#import stu
from stu import Stu
paul = Stu()
print('paul.name=',paul.name)
print('paul.grade=',paul.grade)
print('paul.year=',paul.year)
paul.study_hard()
print(paul)
tony = Stu('tony', 3.99)
tony.year = 2
print(paul < tony)