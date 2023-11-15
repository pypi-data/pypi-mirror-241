import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories

# Represents a software Project Links
class ProjectLinks(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(ProjectLinks,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_projectlinks(self, project_key):
		return self.sonar.project_links.search_project_links(project_key)

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_projectlinks")
			
			project_service = factories.Project(personal_access_token=self.personal_access_token,organization = self.organization)
			projects = project_service.get_all()
			projectlinks = []
			
			for project in projects:
				projectlinks_return = self.get_projectlinks(project['key'])
				projectlinks_return['project'] = project
				projectlinks.append(projectlinks_return)

			return projectlinks

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Project Links")
		
	def get_project_links(self, project_key):
		project_links = None
		
		api_endpoint = f'api/project_links/search?projectKey={project_key}'
		
		project_links = self.retrive_data (api_endpoint=api_endpoint)
	
		return project_links['links']
		
	
	def get_by_project_function(self, project_id,**kwargs):
		
		project_links = []
		function = kwargs["function"]
		
		try:
			logging.info("Start function: get_project_links")
			list_project_links = self.get_project_links(project_id)
			for link in list_project_links:
				link['project'] = project_id
				function (data=link, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				project_links.append(link)
			
			return project_links
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All get_components_tree")
		return project_links	
		
