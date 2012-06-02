import colander
from tombstone import Tombstone
from psychological import Psychological
from motorskills import GrossMotorSkills, FineMotorSkills
from earlydev import EarlyDevelopment
    
class MainForm(colander.Schema):
    tombstone = Tombstone()
    psychological = Psychological()
    gross_motor_skills = GrossMotorSkills()
    fine_motor_skills = FineMotorSkills()
    #early_development = EarlyDevelopment()


