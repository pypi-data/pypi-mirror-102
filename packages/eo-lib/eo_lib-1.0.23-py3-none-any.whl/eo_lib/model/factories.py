import factory
from eo_lib.model.team.models import *

class PersonFactory(factory.Factory):
    class Meta:
        model = Person

class Team_MemberFactory(factory.Factory):
    class Meta:
        model = Team_Member

class Team_MembershipFactory(factory.Factory):
    class Meta:
        model = Team_Membership

class Organizational_RoleFactory(factory.Factory):
    class Meta:
        model = Organizational_Role

class TeamFactory(factory.Factory):
    class Meta:
        model = Team

class Project_TeamFactory(factory.Factory):
    class Meta:
        model = Project_Team

class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

class Organizational_TeamFactory(factory.Factory):
    class Meta:
        model = Organizational_Team

class OrganizationFactory(factory.Factory):
    class Meta:
        model = Organization

