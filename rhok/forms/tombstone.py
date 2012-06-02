import colander

class Tombstone(colander.Schema):
    name = colander.SchemaNode(colander.String())
    date_of_birth = colander.SchemaNode(colander.Date())

