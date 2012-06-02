import colander

class PriorAssessmentSchema(colander.Schema):
    when = colander.SchemaNode(colander.String())
    where = colander.SchemaNode(colander.String())
    currently_involved = colander.SchemaNode(colander.String())

class Psychological(colander.Schema):
    psychological = PriorAssessmentSchema()
    speech = PriorAssessmentSchema()
    occupational = PriorAssessmentSchema()
    audiology = PriorAssessmentSchema()

