import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories

# Represents a software Project Analyses
class ProjectAnalyses(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(ProjectAnalyses,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_projectanalyses(self, project_key):
		return self.sonar.project_analyses.search_project_analyses_and_events(project=project_key)

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_projectanalyses")
			
			project_service = factories.Project(personal_access_token=self.personal_access_token,organization=self.organization)
			projects = project_service.get_all()
			projectanalyses = []
			
			for project in projects:
				projectanalyses_return = self.get_projectanalyses(project['key'])
				projectanalyses_return['project'] = project
				projectanalyses.append(projectanalyses_return)

			return projectanalyses

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Project Analyses")
		
	def get_project_analyses(self, project_key):
		project_analyses = None
		
		api_endpoint = f'api/project_analyses/search?project={project_key}'
		
		project_analyses = self.retrive_data (api_endpoint=api_endpoint)
	
		return project_analyses['analyses']
		
	
	def get_by_project_function(self, project_id,**kwargs):
		
		project_analyses = []
		function = kwargs["function"]
		
		try:
			logging.info("Start function: get_project_analyses")
			list_project_analyses = self.get_project_analyses(project_id)
			for analyse in list_project_analyses:
				analyse['project'] = project_id
				function (data=analyse, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				project_analyses.append (analyse)
			
			return project_analyses
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All get_project_analyses")
		return project_analyses	
