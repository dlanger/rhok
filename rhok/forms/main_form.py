import colander
from tombstone import Tombstone
from psychological import Psychological

class MainForm(colander.Schema):
    tombstone = Tombstone()
    psychological = Psychological()


