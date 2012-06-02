Forms = RHOK.module 'forms'

class Forms.GrossMotorSkills extends Backbone.Model
  schema:
    crawling: 
      title: 'At what age did your child start to crawl? (in months)'
      dataType: 'number'
      type: 'Number'

    walking: 
      title: 'At what age did your child start to walk? (in months)'
      dataType: 'number'
      type: 'Number'

    running: 
      title: 'At what age did your child start to run? (in months)'
      dataType: 'number'
      type: 'Number'

