import re
from enum import Enum


class Faculty(Enum):
    MT = 'МТ'
    SM = 'СМ'
    IU = 'ИУ'
    IBM = 'ИБМ'
    RK = 'РК'
    RKT = 'РКТ'
    RL = 'РЛ'
    FN = 'ФН'
    E = 'Э'
    UR = 'ЮР'


class Grade(Enum):
    PHD = "А"
    master = "М"
    bach = "Б"
    spec = ""


class Group:
    faculty: Faculty
    dep: int
    session: int
    group_num: int
    grade: Grade

    def __init__(self, faculty: Faculty, dep: int, session: int, group_num: int, grade: Grade):
        self.faculty = faculty
        self.dep = dep
        self.session = session
        self.group_num = group_num
        self.grade = grade

    @classmethod
    def from_string(self, group: str):
        split = re.split("(\d+)", group)
        faculty = next((f for f in Faculty if f.value == split[0]), "None")
        grade = next((g for g in Grade if g.value == split[-1]), "None")
        return Group(faculty, int(split[1]), int(split[-2]) // 10, int(split[-2][-1]), grade)

    def to_string(self):
        return f"{self.faculty}{self.dep}-{self.session}{self.gr_num}{self.grade}"

