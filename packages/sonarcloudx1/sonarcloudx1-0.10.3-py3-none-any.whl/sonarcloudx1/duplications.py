import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar
from sonarcloudx1	import factories

# Represents a software Duplications with function
class Duplications(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(Duplications,self).__init__(personal_access_token=personal_access_token, organization=organization)

	def get_components_tree(self, project_key):
		component = self.sonar.components.get_project_component_and_ancestors(project_key)
		print(component['component']['key'])
		components_tree = self.sonar.components.get_components_tree(component=component['component']['key'],qualifiers="FIL")
		return components_tree	


	def get_components_tree(self, project_key):
		component = None
		
		api_endpoint = f'api/measures/search?component={project_key}&metricKeys=duplicated_lines_density'
		
		component = self.retrive_data (api_endpoint=api_endpoint)
		return component
	
	def get_by_project_function(self, project_id,**kwargs):
		
		function = kwargs["function"]
		measures = []
		try:
			logging.info("Start function: get_components_tree")
			data = self.get_components_tree(project_id)
			if data!=None:
				for measure in data['component']['measures']:
					measure['project'] = project_id
					measures.append(measure)
					function (data=measure, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				
			return measures
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All duplication from a project")
		return measures	

	def get_all(self, today=False): 
		try:
			logging.info("Start function: get_duplications")
			
			project_service = factories.ProjectFactory(personal_access_token=self.personal_access_token, organization=self.organization)
			projects = project_service.get_all()

			list_dict_duplications = []
			
			for project in projects:
				component_tree_return = self.get_components_tree(project['key'])

				
				if component_tree_return['components'] != None:
					for components in component_tree_return['components']:
						print(components['key'])
						component = self.sonar.duplications.get_duplications(components['key'])
						component['project'] = project
						list_dict_duplications.append(component)

			
			return list_dict_duplications

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Duplications")
		

