import pandas as pd
import re
from enum import Enum
import numpy as np
from Group import *


class Student:
    st_df: pd.core.frame.DataFrame
    __enr_year: int
    __grade: str
    __last_session: int
    __is_dropout: bool
    __study_period: int
    __mean_mark: float

    def __init__(self, st_df: pd.core.frame.DataFrame):
        self.st_df = st_df.sort_values('#Сессии')

    @property
    def enr_year(self):
        gr = Group.from_string(self.st_df.iloc[0]['#Группы'])
        return (self.st_df.iloc[0]['#Сессии'] - 1)// 2 + 2006 if gr.session == 1 else None

    @property
    def grade(self):
        gr = self.st_df["#Группы"].map(lambda g: Group.from_string(g).grade.value \
                                       if type(Group.from_string(g).grade) != str else 'None')
        return next((g for g in gr if g != Grade.spec.value), "Специалист")

    @property
    def first_session(self):
        return self.st_df['#Сессии'].reset_index(drop=True)[0]

    @property
    def last_session(self):
        return self.st_df['#Сессии'].reset_index(drop=True).iloc[-1]

    @property
    def faculty(self):
        return Group.from_string(self.st_df.reset_index(drop=True).loc[0, '#Группы']).faculty.value

    @property
    def is_dropout(self):
        return len(self.st_df[(self.st_df == 'False').any(axis=1)]) > 0

    @property
    def study_period(self):
        return len(self.st_df)

    @property
    def good_study_period(self):
        return len(self.st_df[(self.st_df != 'False').all(axis=1)])

    @property
    def expelled_immediately(self):
        return (self.st_df.iloc[0,:].dropna() == 'False').any()

    @property
    def mean_mark(self):
        marks = self.st_df[(self.st_df != 'False').all(axis=1)].iloc[:, 4:].stack().tolist()
        return round(np.average([e for e in marks if isinstance(e, float)]), 2) if len(marks) > 0 else None
