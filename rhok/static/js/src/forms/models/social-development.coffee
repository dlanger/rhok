Forms = RHOK.module 'forms'

class Forms.SocialDevelopment extends Backbone.Model
  schema:
    affection:
      title: 'How often your child show affection'
      type: 'Select'
      options: [
          val: ''
          label: 'N/A'
        ,
          val: 'always'
          label: 'Always'
        ,
          val: 'on_their_terms'
          label: 'On their terms only'
      ]
    crawling: 
      title: 'At what age did your child start to engage in eye contact? (in months)'
      dataType: 'number'
      type: 'Number'

