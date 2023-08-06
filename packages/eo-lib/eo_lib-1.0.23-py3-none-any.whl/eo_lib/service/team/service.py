from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from eo_lib.model.team.models import *
from eo_lib.service.base_service import BaseService

class PersonService(BaseService):

    """ Service of Person"""

    def __init__(self):
        super(PersonService,self).__init__(Person)

class Team_MemberService(BaseService):

    """ Service of Team_Member"""

    def __init__(self):
        super(Team_MemberService,self).__init__(Team_Member)

class Team_MembershipService(BaseService):

    """ Service of Team_Membership"""

    def __init__(self):
        super(Team_MembershipService,self).__init__(Team_Membership)

class Organizational_RoleService(BaseService):

    """ Service of Organizational_Role"""

    def __init__(self):
        super(Organizational_RoleService,self).__init__(Organizational_Role)

class TeamService(BaseService):

    """ Service of Team"""

    def __init__(self):
        super(TeamService,self).__init__(Team)

class Project_TeamService(BaseService):

    """ Service of Project_Team"""

    def __init__(self):
        super(Project_TeamService,self).__init__(Project_Team)

class ProjectService(BaseService):

    """ Service of Project"""

    def __init__(self):
        super(ProjectService,self).__init__(Project)

class Organizational_TeamService(BaseService):

    """ Service of Organizational_Team"""

    def __init__(self):
        super(Organizational_TeamService,self).__init__(Organizational_Team)

class OrganizationService(BaseService):

    """ Service of Organization"""

    def __init__(self):
        super(OrganizationService,self).__init__(Organization)

