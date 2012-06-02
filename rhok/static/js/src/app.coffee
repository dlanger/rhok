Forms = RHOK.module 'forms'

class App
  $el: $('#Main')

  init: =>
    tombstone = new Forms.Tombstone()

    tombstoneView = new Forms.SectionView({
      model: tombstone
    }).render()

    @$el.append(tombstoneView.el)

window.app = new App()

$(window.app.init)
