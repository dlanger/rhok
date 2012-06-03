from pyramid.response import Response
from pyramid.view import view_config

import json
import datetime

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
    form = json.loads(request.POST.get('data', "{}"))
    form = json.loads("""
    {"Tombstone":{
       "header":"Tombstone",
       "name":"Jack",
       "date_of_birth":null
     },
     "Learning":{
       "header":"Learning",
       "reading":"bt_adequate",
       "spelling":"adequate",
       "math":"lt_adequate"
     },
     "Adaptive":{
       "header":"Adaptive",
       "dressing":"4",
       "picky_eater":"infant",
       "sensitve_eater":"yes",
       "difficult_sleeping":"yes",
       "assitence_needed_sleeping":"yes",
       "toilet_training":""
      },
      "Fine Motor Skills":{
        "header":"Fine Motor Skills",
        "puzzle_skill":"no"
      },
      "Gross Motor Skills":{
        "header":"Gross Motor Skills",
        "crawling":8,
        "walking":10,
        "running":1
      }
    }""")

    data = extract(form)
    result = evaluate(data)
    save_record(data, result)
    return dict(result=result)


adequacy_values = dict(lt_adequate=0, adequate=1, bt_adequate=2)
age_factors = dict(infant=0, child=1, teenager=2, adolescent=3)
yes_no = dict(yes=True, no=False)

def extract(form):
    return dict(name=form["Tombstone"]["name"],
                reading=adequacy_values[form["Learning"]["reading"]],
                spelling=adequacy_values[form["Learning"]["spelling"]],
                math=adequacy_values[form["Learning"]["math"]],
                dressing_age=int(form["Adaptive"]["dressing"]),
                picky_eater=age_factors[form["Adaptive"]["picky_eater"]],
                sensitive_eater=yes_no[form["Adaptive"]["sensitve_eater"]],
                difficult_sleeping=yes_no[form["Adaptive"]["difficult_sleeping"]],
                assitence_needed_sleeping=yes_no[form["Adaptive"]["assitence_needed_sleeping"]])

def evaluate(record):
    # ok, I'm totally making it up here.
    # in real life it would be something like multiplying some kind of a
    # model matrix by the data vector..

    ASD = 0.
    ADHD = 0.
    DD = 0.
    LI = 0.
    
    ASD += 1 if record["reading"] in [0,3] else 0
        
    return dict(ASD=ASD,
                ADHD=ADHD,
                DD=DD,
                LI=LI)

def save_record(data, result):
    session = DBSession()
    record = Record(datetime.date.today(),
                    json.dumps(data),
                    json.dumps(result))
    session.add(record)
