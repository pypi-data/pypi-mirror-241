import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories
import requests

# Represents a software Components
class ComponentsTree(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(ComponentsTree,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_components_tree(self, project_key):
		component = None
		
		api_endpoint = f'api/components/tree?component={project_key}'
		
		component = self.retrive_data (api_endpoint=api_endpoint)
	
		return component['components']
		
	
	def get_by_project_function(self, project_id,**kwargs):
		
		components_tree = []
		function = kwargs["function"]
		
		try:
			logging.info("Start function: get_components_tree")
			components = self.get_components_tree(project_id)
			for component in components:
				component['project'] = project_id
				function (data=component, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				components_tree.append (component)
			
			return components_tree
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All get_components_tree")
		return components_tree	

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_components_tree")
			
			project_service = factories.ProjectFactory(personal_access_token=self.personal_access_token, organization = self.organization)
			projects = project_service.get_all()
			components_tree = []
			
			for project in projects:
				component_tree_return = self.get_components_tree(project['key'])
				component_tree_return['project'] = project
				components_tree.append(component_tree_return)
			
			return components_tree

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Components Tree")
		
		
