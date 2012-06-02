import colander
from tombstone import Tombstone
from psychological import Psychological
from motorskills import GrossMotorSkills, FineMotorSkills

class MainForm(colander.Schema):
    tombstone = Tombstone()
    psychological = Psychological()
    gross_motor_skills = GrossMotorSkills()
    fine_motor_skills = FineMotorSkills()


