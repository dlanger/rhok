Forms = RHOK.module 'forms'

class App
  $el: $('#Main')

  init: =>
    tombstone = new Forms.Tombstone()
    adaptive = new Forms.Adaptive()

    # Collection of all sections/fieldsets
    @fieldsets = new Backbone.Collection()

    @fieldsets.add(new Forms.Tombstone( header: 'Tombstone' ))
    @fieldsets.add(new Forms.Learning( header: 'Learning' ))

    @formView = new Forms.FormView({
      collection: @fieldsets
    }).render()

    adaptiveView = new Forms.SectionView({
      model: adaptive
    }).render()

    @$el.append(tombstoneView.el)
    @$el.append(adaptiveView.el)

window.app = new App()

$(window.app.init)
