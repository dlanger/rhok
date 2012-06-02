Forms = RHOK.module 'forms'

class Forms.SectionView extends Backbone.View
  template: _.template('<label><%= label =></label>')

  initialize: ->
    @model.on('all', @render)

  render: =>
    @$el.empty()

    form = new Backbone.Form( model: @model )
    form.render()

    @$el.append(form.el)

    @

