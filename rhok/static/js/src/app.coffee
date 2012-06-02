Forms = RHOK.module 'forms'

class App
  $el: $('#Main')

  init: =>
    # Collection of all sections/fieldsets
    @fieldsets = new Backbone.Collection()

    @fieldsets.add(new Forms.Tombstone( header: 'Tombstone' ))
    @fieldsets.add(new Forms.Learning( header: 'Learning' ))
    @fieldsets.add(new Forms.Adaptive( header: 'Adaptive'))
    @fieldsets.add(new Forms.FineMotorSkills( header: 'Fine Motor Skills'))
    @formView = new Forms.FormView({
      collection: @fieldsets
    }).render()

    @$el.append(@formView.el)

window.app = new App()

$(window.app.init)
