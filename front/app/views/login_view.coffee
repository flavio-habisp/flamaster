{LoginModel} = require 'models/session_model'
{GenericView} = require 'views/generic_view'

{baseContext, serializeForm} = require 'helpers'

class exports.LoginView extends GenericView
  className: 'login'
  template: require './templates/login'
  events:
    "click #signin-form [type='submit']": "submit"

  initialize: ->
    @model = new LoginModel

    app.homeView.getCurrentUser
      success: (model, resp) =>
        @model.set model.toJSON(), silent: true

  render: ->
    @$el.html @template(baseContext)
    @el

  submit: (ev) ->
    @clearErrors()
    data = serializeForm($(ev.target).parents 'form')
    # @model.set data, silent: true
    @model.save data,
      success: (model, response) ->
        if !response.is_anonymous
          app.router.navigate "!/profile/#{response.uid}", trigger: true
      error: (model, response) =>
        if response.responseText?
          for field, message of JSON.parse(response.responseText)
            @renderError field, message
        else
          for field, message of response
            @renderError field, message

        console.log response
    return false

