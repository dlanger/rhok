from pyramid.response import Response
from pyramid.view import view_config

import json
import deform

from forms.main_form import MainForm

from models import DBSession, Record

@view_config(route_name='home', renderer='forms.mako')
def my_view(request):
    main_form = deform.Form(MainForm(), buttons=('submit',))
    return {
        'form': main_form.render(),
    }

@view_config(route_name='process', renderer='result.mako')
def process_data(request):
    record = json.loads(request.POST.get('data', "{}"))
    save_record(record)
    result = evaluate(record)
    return dict(result=result)

def evaluate(record):
    # somehow figure it out
    return dict(ASD=0.8,
                ADHD=0.3,
                DD=0.2,
                LI=0.1)

def save_record(record):
    session = DBSession()
    r = Record(json.dumps(record))
    session.add(r)
