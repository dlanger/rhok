import colander
from tombstone import Tombstone
from psychological import Psychological
from motorskills import GrossMotorSkills

class MainForm(colander.Schema):
    tombstone = Tombstone()
    psychological = Psychological()
    gross_motor_skills = GrossMotorSkills()


