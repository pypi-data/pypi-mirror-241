import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories

# Represents a software Project Branches
class ProjectBranches(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(ProjectBranches,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_projectbranches(self, project_key):
		return self.sonar.project_branches.search_project_branches(project=project_key)

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_projectbranches")
			
			project_service = factories.Project(personal_access_token=self.personal_access_token, organization=self.organization)
			projects = project_service.get_all()
			projectbranches = []
			
			for project in projects:
				projectbranches_return = self.get_projectbranches(project['key'])
				projectbranches_return['project'] = project
				projectbranches.append(projectbranches_return)

			return projectbranches

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Project Branches")
		
	def get_project_branches(self, project_key):
		project_branches = None
		
		api_endpoint = f'api/project_branches/list?project={project_key}'
		
		project_branches = self.retrive_data (api_endpoint=api_endpoint)
	
		return project_branches['branches']
		
	
	def get_by_project_function(self, project_id,**kwargs):
		
		project_branches = []
		function = kwargs["function"]
		
		try:
			logging.info("Start function: get_project_branches")
			list_project_branches = self.get_project_branches(project_id)
			for branche in list_project_branches:
				branche['project'] = project_id
				function (data=branche, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				project_branches.append (branche)
			
			return project_branches
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All get_project_branches")
		return project_branches			
