from eo_lib.config.base import Entity
from sqlalchemy import Column, Boolean ,ForeignKey, Integer, DateTime, Date, String, Text
from sqlalchemy.orm import relationship
from eo_lib.model.relationship.models import *

class Person(Entity):
	
	"""A human Physical Agent."""
	
	is_instance_of = "person"
	__tablename__  = "person"
	serialize_only = ('name', 'description', )
	type = Column(String(50))

	email = Column(String)

	organization_id = Column(Integer, ForeignKey('organization.id'))
	organization = relationship("Organization", back_populates="people")


	#esta vindo como team .. verifiar o erro
	__mapper_args__ = {
		'polymorphic_identity':'person',
		'polymorphic_on':type
	}

class Team_Member(Person):
	
	
	is_instance_of = "team_member"
	__tablename__  = "team_member"
	serialize_only = ('name', 'description', 'team_memberships.uuid_',
	)

	id = Column(Integer, ForeignKey('person.id'), primary_key=True)

	
	team_memberships = relationship("Team_Membership", back_populates="team_member")


	__mapper_args__ = {
		'polymorphic_identity':'team_member',
	}

class Team_Membership(Entity):
	
	"""A relationship among Team Member and a Team"""
	
	is_instance_of = "team_membership"
	__tablename__  = "team_membership"
	serialize_only = ('name', 'description', 'teams.uuid_',
	)

	teams = relationship("Team", back_populates="team_membership")

	organizational_role_id = Column(Integer, ForeignKey('organizational_role.id'))
	organizational_role = relationship("Organizational_Role", back_populates="team_memberships")
	
	team_member_id = Column(Integer, ForeignKey('team_member.id'))
	team_member = relationship("Team_Member", back_populates="team_memberships")


class Organizational_Role(Entity):
	
	"""A Role that is play by a person in a project"""
	
	is_instance_of = "organizational_role"
	__tablename__  = "organizational_role"
	serialize_only = ('name', 'description', 'team_memberships.uuid_',
	)

	team_memberships = relationship("Team_Membership", back_populates="organizational_role")
	


class Team(Entity):
	
	"""A Team"""
	
	is_instance_of = "team"
	__tablename__  = "team"
	serialize_only = ('name', 'description', )
	type = Column(String(50))


	team_membership_id = Column(Integer, ForeignKey('team_membership.id'))
	team_membership = relationship("Team_Membership", back_populates="teams")

	__mapper_args__ = {
		'polymorphic_identity':'team',
		'polymorphic_on':type
	}

class Project_Team(Team):
	
	"""A Team with a project"""
	
	is_instance_of = "project_team"
	__tablename__  = "project_team"
	serialize_only = ('name', 'description', )
	id = Column(Integer, ForeignKey('team.id'), primary_key=True)


	#project = Column(Integer, ForeignKey('project.id'))

	project_id = Column(Integer, ForeignKey('project.id'))
	project = relationship("Project", back_populates="project_teams")


	__mapper_args__ = {
		'polymorphic_identity':'project_team',
	}

class Project(Entity):
	
	"""A Project"""
	
	is_instance_of = "project"
	__tablename__  = "project"
	serialize_only = ('name', 'description', 'project_teams.uuid_',
	)

	project_teams = relationship("Project_Team", back_populates="project")



class Organizational_Team(Team):
	
	"""A Team without project"""
	
	is_instance_of = "organizational_team"
	__tablename__  = "organizational_team"
	serialize_only = ('name', 'description', )
	id = Column(Integer, ForeignKey('team.id'), primary_key=True)


	#organization = Column(Integer, ForeignKey('organization.id'))


	organization_id = Column(Integer, ForeignKey('organization.id'))
	organization = relationship("Organization", back_populates="organizational_teams")


	__mapper_args__ = {
		'polymorphic_identity':'organizational_team',
	}

class Organization(Entity):
	
	"""A Organization"""
	
	is_instance_of = "organization"
	__tablename__  = "organization"
	serialize_only = ('name', 'description', 'organization_teams.uuid_',
	)

	email = Column(String)

	people = relationship("Person", back_populates="organization")

	organizational_teams = relationship("Organizational_Team", back_populates="organization")
	

