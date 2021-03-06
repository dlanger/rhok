Forms = RHOK.module 'forms'

class App
  $el: $('#Main')

  init: =>
    # Collection of all sections/fieldsets
    @fieldsets = new Backbone.Collection()

    @fieldsets.add(new Forms.Tombstone( header: 'Personal Information' ))
    @fieldsets.add(new Forms.Learning( header: 'Learning' ))
    @fieldsets.add(new Forms.Adaptive( header: 'Adaptive'))
    @fieldsets.add(new Forms.FineMotorSkills( header: 'Fine Motor Skills'))
    @fieldsets.add(new Forms.GrossMotorSkills( header: 'Gross Motor Skills'))
    @fieldsets.add(new Forms.SocialDevelopment( header: 'Social Development'))
    @formView = new Forms.FormView({
      collection: @fieldsets
    }).render()

    @$el.append(@formView.el)

window.app = new App()

$(window.app.init)
