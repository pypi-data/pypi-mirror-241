from datetime import date, timedelta
from cist.utils import to_timestamp
from cist.transport import api_request

IDCIENT = "&idClient=KNURESked"

class Group():

    def __init__(self, group_id):
        self.group = group_id

    def get_schedule(self, date_from=None, date_to=None):
        if date_from != None:
            t_from = f"&time_from={to_timestamp(date_from)}"
        if date_to != None:
                t_to = f"&time_to={to_timestamp(date_to)}" 
        else:
            t_from, t_to = "", ""

        url = f"/P_API_EVENTS_GROUP_JSON?p_id_group={self.group}{t_from}{t_to}" + IDCIENT
        return api_request(url)

class Teacher():

    def __init__(self, teacher_id):
        self.id = teacher_id

    def get_schedule(self, date_from=None, date_to=None):
        if date_from != None:
            t_from = f"&time_from={to_timestamp(date_from)}"
        if date_to != None:
                t_to = f"&time_to={to_timestamp(date_to)}" 
        else:
            t_from, t_to = "", ""

        url = f"/P_API_EVENTS_GROUP_JSON?p_id_teacher={self.id}{t_from}{t_to}" + IDCIENT
        return api_request(url)
    
class Auditory():

    def __init__(self, id_auditory):
        self.id = id_auditory

    def get_schedule(self, date_from=None, date_to=None):
        if date_from != None:
            t_from = f"&time_from={to_timestamp(date_from)}"
        if date_to != None:
                t_to = f"&time_to={to_timestamp(date_to)}" 
        else:
            t_from, t_to = "", ""

        url = f"/P_API_EVENTS_AUDITORY_JSON?p_id_auditory={self.id}{t_from}{t_to}" + IDCIENT
        return api_request(url)
       
class Couple():

    def __init__(self, id_object, mode=None):
        self.id = id_object
        if mode == None or mode == 'group':
            self.mode = ''
        elif mode == 'teacher':
            self.mode = f'&type_id=2'
        elif mode == 'auditory':
            self.mode = f'&type_id=3'

    def get_schedule(self, date_from=None, date_to=None):
        if date_from != None:
            t_from = f"&time_from={to_timestamp(date_from)}"
        if date_to != None:
                t_to = f"&time_to={to_timestamp(date_to)}" 
        else:
            t_from, t_to = "", ""

        url = f"/P_API_EVENTS_AUDITORY_JSON?timetable_id={self.id}{self.mode}{t_from}{t_to}" + IDCIENT
        return api_request(url)