import colander
import deform

class EarlyDevelopment(colander.Schema):
    late_self_dressing = colander.SchemaNode(
        colander.Boolean(),
        description="Started self-dressing later than 4 years old")
    picky_eater = colander.SchemaNode(
        colander.Boolean(),
        description="Tends to stick to certain types of food")
    food_texture = colander.SchemaNode(
        colander.Boolean(),
        title="Sensitive to certain textures of food")
    food_color = colander.SchemaNode(
        colander.Boolean(),
        title="Sensitive to certain colors of food")
    food_smell = colander.SchemaNode(
        colander.Boolean(),
        title="Sensitive to certain smells of food")
    falling_asleep = colander.SchemaNode(
        colander.Boolean(),
        title="Has difficulty falling asleep")
    caregiver_presence = colander.SchemaNode(
        colander.Boolean(),
        title="Dosn't fall asleep alone",
        description="Requests a parent or caregiver presense when falling asleep")
    wakes_up = colander.SchemaNode(
        colander.Boolean(),
        title="Frequetly wakes up",
        description=("Doesn't stay asleep through the night, " +
                     "wakes up frequently"))
    late_toilet_training = colander.SchemaNode(
        colander.Boolean(),
        title="Has been toilet trained later than in 3 years")

