import colander
import deform

class GrossMotorSkills(colander.Schema):
    supervision = colander.SchemaNode(
        colander.Boolean(),
        title="Constant supervision",
        description=("Is constant supervision required because of " +
                     "the lack of the safety awareness?"))
    decreased_muscles_tone = colander.SchemaNode(
        colander.Boolean(),
        descrition="Is the muscles tone decreased?")
    head_control = colander.SchemaNode(
        colander.Boolean(),
        title="Inadequate head control",
        descrition=("Any problems with keeping head up? " +
                    "Is there any head flopping, keeping to side?"))
    sitting = colander.SchemaNode(
        colander.Boolean(),
        title="Started sitting after 7 months")
    crawling = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
            values=(('normal', "Normal"),
                    ('commando', "Commando crawling"),
                    ('shuffle', "Butt shuffle"),
                    ('none', "No crawling at all"))))
    late_walking = colander.SchemaNode(
        colander.Boolean(),
        descrition="Started walking later than in 15 months")
    late_running = colander.SchemaNode(
        colander.Boolean(),
        descrition="Started runing in more than 2 months after walking")
    climbing = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
            values=(('normal', "Normal"),
                    ('fearful', "Fearful"),
                    ('fearless', "Fearless"))))
    running = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
            values=(('normal', "Normal"),
                    ('awkward', "Awkward run"),
                    ('floppy', "Floppy run"),
                    ('none', "Not running at all"))))
    excited_jumping = colander.SchemaNode(
        colander.Boolean(),
        descrition="Likes to spin/jumps when excited")
    overall_motor_skills = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
            values=(('normal', "Normal"),
                    ('over', "Unusually good"),
                    ('floppy', "Exceptionally bad"))))


class FineMotorSkills(colander.Schema):
    dressing = colander.SchemaNode(
        colander.Boolean(),
        title="Avoids self-dressing")
    buttons = colander.SchemaNode(
        colander.Boolean(),
        title="Has difficulties with buttons and zippers")
    hand_preference = colander.SchemaNode(
        colander.String(),
        widget=deform.widget.SelectWidget(
            values=(('right', "Right"),
                    ('left', "Left"),
                    ('both', "Both"))))
    drawing = colander.SchemaNode(
        colander.Boolean(),
        title="Drawing difficulties",
        description=("Any difficulties with drawing, colouring or copying?"))
    writing = colander.SchemaNode(
        colander.Boolean(),
        title="Writing difficulties",
        description=("Any difficulties with writing or staying on line " +
                     "when writing?"))
    puzzle = colander.SchemaNode(
        colander.Boolean(),
        title="Excellent puzzling skill")
    
