Forms = RHOK.module 'forms'

class Forms.SectionView extends Backbone.View
  tagName: 'fieldset'

  className: 'well'

  headerTmpl: _.template('<h2><%= header %></h2>')

  initialize: ->
    @model.on('all', @render)

  render: =>
    @$el.empty()

    @$el.append(@headerTmpl( header: @model.get('header') ))

    form = new Backbone.Form( model: @model )
    form.render()

    @$el.append(form.el)

    @

class Forms.FormView extends Backbone.View
  tagName: 'form'

  render: =>
    that = @

    @$el.empty()

    @collection.each (model) ->
      view = new Forms.SectionView( model: model ).render()
      that.$el.append(view.el)

    @


