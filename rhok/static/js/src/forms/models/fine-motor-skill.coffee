Forms = RHOK.module 'forms'

class Forms.FineMotorSkills extends Backbone.Model
  schema:
    dressing_problems:
      title: 'Does your child have problems dressing themselves using zippers/buttons'
      type: 'Radio'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]

    writing_in_lines:
      title: 'Does your child have difficulty drawing/colouring/writing/copying/staying within the lines?'
      type: 'Radio'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]

    hand_preference:
      title: "What is your child's hand preference?"
      type: 'Radio'
      options: [
          val: 'left'
          label: 'Left'
        ,
          val: 'right'
          label: 'Right'
        ,
          val: 'both'
          label: 'Both'
      ]

    pencil_grasp:
      title: 'Does your child have poor pencil grasp?'
      type: 'Radio'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]

    puzzle_skill:
      title: 'Does your child have poor writing skills but excellent spatial or puzzle skills?'
      type: 'Radio'
      options: [
          val: 'yes'
          label: 'Yes'
        ,
          val: 'no'
          label: 'No'
      ]
