import factory
from eo_lib.service.team.service import *

class PersonFactory(factory.Factory):
    class Meta:
        model = PersonService

class Team_MemberFactory(factory.Factory):
    class Meta:
        model = Team_MemberService

class Team_MembershipFactory(factory.Factory):
    class Meta:
        model = Team_MembershipService

class Organizational_RoleFactory(factory.Factory):
    class Meta:
        model = Organizational_RoleService

class TeamFactory(factory.Factory):
    class Meta:
        model = TeamService

class Project_TeamFactory(factory.Factory):
    class Meta:
        model = Project_TeamService

class ProjectFactory(factory.Factory):
    class Meta:
        model = ProjectService

class Organizational_TeamFactory(factory.Factory):
    class Meta:
        model = Organizational_TeamService

class OrganizationFactory(factory.Factory):
    class Meta:
        model = OrganizationService

