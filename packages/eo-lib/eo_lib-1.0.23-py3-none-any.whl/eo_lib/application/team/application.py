from eo_lib.service.team.service import *
from eo_lib.application.abstract_application import AbstractApplication

class ApplicationPerson(AbstractApplication):

	""" Application of  Person"""
	def __init__(self):
		super().__init__(PersonService())
	
class ApplicationTeam_Member(AbstractApplication):

	""" Application of  Team_Member"""
	def __init__(self):
		super().__init__(Team_MemberService())
	
class ApplicationTeam_Membership(AbstractApplication):

	""" Application of  Team_Membership"""
	def __init__(self):
		super().__init__(Team_MembershipService())
	
class ApplicationOrganizational_Role(AbstractApplication):

	""" Application of  Organizational_Role"""
	def __init__(self):
		super().__init__(Organizational_RoleService())
	
class ApplicationTeam(AbstractApplication):

	""" Application of  Team"""
	def __init__(self):
		super().__init__(TeamService())
	
class ApplicationProject_Team(AbstractApplication):

	""" Application of  Project_Team"""
	def __init__(self):
		super().__init__(Project_TeamService())
	
class ApplicationProject(AbstractApplication):

	""" Application of  Project"""
	def __init__(self):
		super().__init__(ProjectService())
	
class ApplicationOrganizational_Team(AbstractApplication):

	""" Application of  Organizational_Team"""
	def __init__(self):
		super().__init__(Organizational_TeamService())
	
class ApplicationOrganization(AbstractApplication):

	""" Application of  Organization"""
	def __init__(self):
		super().__init__(OrganizationService())
	
