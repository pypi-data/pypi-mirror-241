from .schedule import Group, Teacher, Auditory
from .objects import Object
from cist.transport import api_request
from cist.utils import help_text

def get_groups():
    return api_request("/P_API_GROUP_JSON")
    
def get_struct():
    return api_request("/P_API_PODR_JSON")
    
def get_audiences():
    return api_request("/P_API_AUDITORIES_JSON")

def get_faculties():
    return api_request("/P_API_FACULTIES_JSON")    

def get_audiences_types():
    return api_request("/P_API_AUDITORY_TYPES_JSON")
    
def help():
    return help_text
