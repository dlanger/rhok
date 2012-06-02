Forms = RHOK.module 'forms'

LEARNING_OPTIONS = [
    val: 'lt_adequate'
    label: 'Less than adequate'
  ,
    val: 'adequate'
    label: 'Adequate'
  ,
    val: 'bt_adequate'
    label: 'Better than adequate'
]



class Forms.Learning extends Backbone.Model
  schema:
    reading: 
      type: 'Radio'
      options: LEARNING_OPTIONS
    spelling: 
      type: 'Radio'
      options: LEARNING_OPTIONS
    math: 
      type: 'Radio'
      options: LEARNING_OPTIONS
    story_writing: 
      title: 'Story Writing'
      type: 'Radio'
      options: LEARNING_OPTIONS
