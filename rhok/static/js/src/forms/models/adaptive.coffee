Forms = RHOK.module 'forms'

class Forms.Adaptive extends Backbone.Model
  schema:
    dressing:
      dataType: 'text'
      validators: ['required']
      title: 'When did your child begin to dress him/herself?'
    picky_eater:
      type: 'Select'
      options: [
          val: 'infant'
          label: 'Infant'
        ,
          val: 'toddler'
          label: 'Toddler'
        ,
          val: 'child'
          label: 'Child'
        ,
          val: 'adolescent'
          label: 'Adolescent'
        ,
          val: 'all'
          label: 'All'
      ]
      title: 'Was your child a picky eater as an'
    sensitve_eater:
      type: 'Select'
      title: 'Was sensitive to certain textures, smells or colours of food?'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]
    difficult_sleeping:
      type: 'Select'
      title: 'Difficulty falling asleep?'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]
    assitence_needed_sleeping:
      title: 'Does your child request you or another caregiver to be present when falling asleep'
      type: 'Select'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]
    sound_sleeping:
      title: 'Does your child stay asleep through the night?'
      type: 'Radio'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]
    toilet_training:
      title: 'What age was your child toilet trained?'

