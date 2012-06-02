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

    @form = new Backbone.Form( model: @model )
    @form.render()

    @$el.append(@form.el)

    @

class Forms.FormView extends Backbone.View
  tagName: 'form'

  buttonTmpl: _.template('<button class="btn btn-primary btn-large" 
      data-loading-text="<%= loadingText %>" type="submit"><%= text %></button>')

  attributes:
    'action': '/process'
    'method': 'POST'

  events:
    'submit': 'onSubmit'

  render: =>
    that = @

    @$el.empty()
    @sections = []

    # Append each section to the form
    @collection.each (model) ->
      section = new Forms.SectionView( model: model ).render()
      that.$el.append(section.el)
      that.sections.push(section)

    @$button = $(@buttonTmpl( text: 'Submit', loadingText: 'Waiting...' )).button()

    @$el.append(@$button)

    @

  onSubmit: (e) ->
    e.preventDefault()

    @$button.button('loading')

    isValid = true
    formJSON = {}

    for section in @sections
      errors = section.form.commit()

      if errors
        isValid = false

      if not errors
        formJSON[section.model.get('header')] = section.model.toJSON()

    $.ajax({
      url: @attributes.action,
      type: 'POST'
      data: {
        data: JSON.stringify(formJSON)
      }
      success: (data) ->
    })

