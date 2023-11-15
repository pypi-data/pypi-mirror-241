import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar

# Represents a software Project
class SupportedProgramingLanguages(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(SupportedProgramingLanguages,self).__init__(personal_access_token=personal_access_token, organization=organization)						


	def get_all(self, today=False): 


		try:			
			logging.info("Start function: get_projects")			
			            
			supported_programming_languages = self.sonar.languages.get_supported_programming_languages()

			if today == False:
				fazer_nada = 2
			
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Projects")
		
		return supported_programming_languages['languages']

	def get_supported_programing_languages(self, project_key):
		supported_programing_languages = None
		
		api_endpoint = f'api/languages/list'
		
		supported_programing_languages = self.retrive_data (api_endpoint=api_endpoint)
	
		return supported_programing_languages['languages']
		
	
	def get_by_project_function(self, project_id,**kwargs):
		
		spls = []
		function = kwargs["function"]
		
		try:
			logging.info("Start function: get_supported_programing_languages")
			list_spl = self.get_supported_programing_languages(project_id)
			for spl in list_spl:
				spl['project'] = project_id
				function (data=spl, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				spls.append (spl)
			
			return spls
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All get_components_tree")
		return spls	