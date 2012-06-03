Forms = RHOK.module 'forms'

class Forms.Tombstone extends Backbone.Model
  schema:
    name: 
      title: 'Full Name'
      dataType: 'text'
      validators: ['required']
    date_of_birth:
      title: 'Date of Birth (dd/mm/yyyy)'
      type: 'Date'
      validators: ['required']


