""" Принцип инверсии зависимости
Модули высокого уровня не должны зависеть
от модулей низшего уровня
при этом и то и то может зависеть от какой то
другой абстракции
При этом, абстракция не должна зависеть от деталей
Это детали должны зависеть от асбстракции

Если код уже реализует принципы открытности\закрытости
и принцип подстановки Барбары Лисков, то в принципе
код уже следует принципу инверсии зависимости 

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
    BLUE_TEAM = 1 
    RED_TEAM = 2
    GREEN_TEAM = 3
    
class Student:
    def __init__(self,name):
        self.name = name
    
class TeamMemberships:
    def __init__(self):
        self.team_memberships = []
        
    def add_team_membership(self, student,team):
        self.team_memberships.append((student,team))
            
class Analysis():
    def __init__(self, team_student_memberships):
        memberships = team_student_memberships.team_memberships
        for members in memberships:
            if members[1] == Teams.RED_TEAM:
                print(f'{members[0].name} is in RED team')
                
student1 = Student('Salkin')
student2 = Student('TT')
student3 = Student('Bob')

team_memberships = TeamMemberships()
team_memberships.add_team_membership(student1, Teams.BLUE_TEAM)
team_memberships.add_team_membership(student2, Teams.RED_TEAM)
team_memberships.add_team_membership(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)

 """

""" идет нарушение инкапсуляции
т.е. мы как будто бы знаем, что у Класса TeamMemberships есть свойство team_memberships
и оно - список. Мы предполагаем

2) мы уверены, что каждая запиь в этом списке это коллекиция из минимум двух элементв
но мы предугадываем, нарушая инкапсуляцию - можно легко сломать код
Класс высокого уровня зависит от реализации классов более низшего уровня
Мы должны избавиться от этого  """

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
    BLUE_TEAM = 1 
    RED_TEAM = 2
    GREEN_TEAM = 3
    
class Student:
    def __init__(self,name):
        self.name = name
        
class TeamMembershipLookup:
    @abstractmethod
    def find_all_students_of_team(self,team):
        pass
    
class TeamMemberships(TeamMembershipLookup):
    def __init__(self):
        self.__team_memberships = []
        
    def add_team_membership(self, student,team):
        self.__team_memberships.append((student,team))
        
    def find_all_students_of_team(self, team):
        for members in self.__team_memberships:
            if members[1] == team:
                yield members[0].name
#тут мы знаем как сохраняется информация - можем перебирать 
            
class Analysis():
    def __init__(self, team_student_memberships):
        memberships = team_student_memberships.find_all_students_of_team(Teams.RED_TEAM)
        for name in memberships:
            print(f'{name} is in RED team')
                #т.е. просто реализовали поиск по красной команде
                #теперь инкапсуляция есть, высокия не зависят от деталей низких
                #изменения реализации низкого уровня не влияет на высокий
student1 = Student('Salkin')
student2 = Student('TT')
student3 = Student('Bob')

team_memberships = TeamMemberships()
team_memberships.add_team_membership(student1, Teams.BLUE_TEAM)
team_memberships.add_team_membership(student2, Teams.RED_TEAM)
team_memberships.add_team_membership(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)