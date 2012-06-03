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
    data = extract(form)
    result = evaluate(data)
    #save_record(data, result)
    items = []
    if (result['ASD'] >= 4):
        items.append('Autism Spectrum Disorders')
    if (result['DD'] >= 1):
        items.append('Developmental Disorder')
    if (result['ADHD'] >= 1):
        items.append('Attention deficit hyperactivity disorder ')
    return dict(items=items)


adequacy_values = dict(lt_adequate=0, adequate=1, bt_adequate=2)
age_factors = dict(infant=0, toddler=1, child=2, teenager=3, adolescent=4)
yes_no = dict(yes=True, no=False)

def extract(form):
    ''' Expecting something like this
    { u'Adaptive': { u'assistence_needed_sleeping': u'yes',
                     u'difficult_sleeping': u'no',
                     u'dressing': 4,
                     u'header': u'Adaptive',
                     u'picky_eater': u'infant',
                     u'sensitve_eater': u'no',
                     u'sound_sleeping': u'yes',
                     u'toilet_training': 2},
      u'Fine Motor Skills': { u'dressing_problems': u'yes',
                              u'hand_preference': u'right',
                              u'header': u'Fine Motor Skills',
                              u'pencil_grasp': u'no',
                              u'puzzle_skill': u'no',
                              u'writing_in_lines': u'yes'},
      u'Gross Motor Skills': { u'crawling': 12,
                               u'header': u'Gross Motor Skills',
                               u'running': 16,
                               u'walking': 14},
      u'Learning': { u'header': u'Learning',
                     u'math': u'bt_adequate',
                     u'reading': u'lt_adequate',
                     u'spelling': u'adequate',
                     u'story_writing': u'adequate'},
      u'Personal Information': { u'date_of_birth': u'2012-06-03T04:00:00.000Z',
                                 u'header': u'Personal Information',
                                 u'name': u'Jack'},
      u'Social Development': { u'affection': u'always',
                               u'crawling': 12,
                               u'header': u'Social Development'}}
    '''
    return dict(name=form["Personal Information"].get("name"),

                # Learning
                reading=adequacy_values[form["Learning"].get("reading")],
                spelling=adequacy_values[form["Learning"].get("spelling")],
                math=adequacy_values[form["Learning"].get("math")],

                # Adaptive
                dressing_age=int(form["Adaptive"].get("dressing")),
                picky_eater=age_factors[form["Adaptive"].get("picky_eater")] if form["Adaptive"].get("picky_eater") else None,
                sensitive_eater=yes_no[form["Adaptive"].get("sensitve_eater")],
                difficult_sleeping=yes_no[form["Adaptive"].get("difficult_sleeping")],
                assistence_needed_sleeping=yes_no[form["Adaptive"].get("assistence_needed_sleeping")],
                sound_sleeping=yes_no[form["Adaptive"].get("sound_sleeping")],
                toilet_training=int(form["Adaptive"].get("toilet_training")),

                # Fine Motor Skills
                dressing_problems=yes_no[form["Fine Motor Skills"].get("dressing_problems")],
                hand_preference=form["Fine Motor Skills"].get("hand_preference"),
                pencil_grasp=yes_no[form["Fine Motor Skills"].get("pencil_grasp")],
                puzzle_skill=yes_no[form["Fine Motor Skills"].get("puzzle_skill")],
                writing_in_lines=yes_no[form["Fine Motor Skills"].get("writing_in_lines")],

                # Gross Motor Skills
                crawling=int(form["Gross Motor Skills"].get("crawling")),
                walking=int(form["Gross Motor Skills"].get("walking")),
                running=int(form["Gross Motor Skills"].get("running")),

                # Social Development
                affection=form["Social Development"].get("affection"),
                eye_contact=int(form["Social Development"].get("eye_contact")),
            )

def evaluate(record):
    '''
    { 'affection': u'always',
      'assistence_needed_sleeping': True,
      'crawling': 9,
      'difficult_sleeping': False,
      'dressing_age': 12,
      'dressing_problems': True,
      'eye_contact': 9,
      'hand_preference': u'right',
      'math': 2,
      'name': u'Jack Hsu',
      'pencil_grasp': False,
      'picky_eater': 1,
      'puzzle_skill': False,
      'reading': 1,
      'running': 16,
      'sensitive_eater': False,
      'sound_sleeping': False,
      'spelling': 1,
      'toilet_training': 2,
      'walking': 12,
      'writing_in_lines': True}
    '''

    # ok, I'm totally making it up here.
    # in real life it would be something like multiplying some kind of a
    # model matrix by the data vector..

    ASD = 0.
    ADHD = 0.
    Anxiety = 0.
    # Dev delay
    DD = 0.
    LI = 0.
    
    ASD += 1 if record["reading"] in [0,3] else 0

    # Hack :)
    if record.get('dressing_age') >= 4:
        ASD += 1
    if record.get('picky_eater'):
        ASD += 1
    if record.get('sensitve_eater'):
        ASD += 1
    if record.get('toilet_training') >= 3:
        ASD += 1
        DD += 1
    if record.get('assistence_needed_sleeping'):
        Anxiety += 1
    if record.get('dressing_problems'):
        ASD += 1
    if record.get('writing_in_lines'):
        ASD += 1
        ADHD += 1
    if record.get('pencil_grasp'):
        ASD += 1
    if record.get('puzzle_skill'):
        ASD += 1


    crawl = int(record.get('crawling'))
    walk = int(record.get('walking'))
    run = int(record.get('running'))

    if crawl - walk > 2:
        ASD += 1
    if walk >= 15:
        ASD += 1
    if run - walk > 2:
        ASD += 1

    if record.get('affection') >= 12:
        ASD += 1
    if record.get('pointing') < 13:
        ASD += 1
    if record.get('eye_contact') >= 12:
        ASD += 1
        
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
