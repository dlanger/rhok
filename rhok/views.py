from pyramid.response import Response
from pyramid.view import view_config

import deform

from forms.main_form import MainForm

@view_config(route_name='home', renderer='forms.mako')
def my_view(request):
    main_form = deform.Form(MainForm(), buttons=('submit',))

    return {
        'form': main_form.render(),
    }

