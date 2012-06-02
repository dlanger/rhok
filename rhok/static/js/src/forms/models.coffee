Forms = RHOK.module 'forms'

class Forms.Tombstone extends Backbone.Model
  schema:
    name: 
      dataType: 'text'
      validators: ['required']
    date_of_birth:
      title: 'Date of Birth'
      type: 'DateTime'
      validators: ['required']

