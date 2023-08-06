import factory
from eo_lib.application.team.application import *

class PersonFactory(factory.Factory):
    class Meta:
        model = ApplicationPerson

class Team_MemberFactory(factory.Factory):
    class Meta:
        model = ApplicationTeam_Member

class Team_MembershipFactory(factory.Factory):
    class Meta:
        model = ApplicationTeam_Membership

class Organizational_RoleFactory(factory.Factory):
    class Meta:
        model = ApplicationOrganizational_Role

class TeamFactory(factory.Factory):
    class Meta:
        model = ApplicationTeam

class Project_TeamFactory(factory.Factory):
    class Meta:
        model = ApplicationProject_Team

class ProjectFactory(factory.Factory):
    class Meta:
        model = ApplicationProject

class Organizational_TeamFactory(factory.Factory):
    class Meta:
        model = ApplicationOrganizational_Team

class OrganizationFactory(factory.Factory):
    class Meta:
        model = ApplicationOrganization

