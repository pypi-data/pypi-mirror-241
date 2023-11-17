from cist.transport import api_request

IDCIENT = "&idClient=KNURESked"

class Object():

    def __init__(self, param_1, param_2=None):
        self.param_1 = param_1
        if param_2 != None:
            self.param_2 = f"&faculty_id={param_2}"
        else:
            self.param_2 = ""
            
    def get_grp_of_directions(self):

        url = f"/P_API_GRP_OF_DIRECTIONS_JSON?{self.param_1}{self.param_2}" + IDCIENT
        return api_request(url)
        
    def get_grp_of_specialities(self):

        url = f"/P_API_GRP_OF_SPECIALITIES_JSON?{self.param_1}{self.param_2}" + IDCIENT
        return api_request(url)

    def get_specialities(self):
        if self.param_2 == "":
            print("Error: faculty_id is required")
        else:
            url = f"/P_API_SPECIALITIES_JSON?{self.param_1}{self.param_2}" + IDCIENT
            return api_request(url)

    
    def get_directions(self):
        url = f"/P_API_DIRECTIONS_JSON?{self.param_1}" + IDCIENT
        return api_request(url)
    
    def get_teachers(self):
        url = f"/P_API_TEACHERS_JSON?{self.param_1}" + IDCIENT
        return api_request(url)
    
    def get_departments(self):
        url = f"/P_API_DEPARTMENTS_JSON?{self.param_1}" + IDCIENT
        return api_request(url)