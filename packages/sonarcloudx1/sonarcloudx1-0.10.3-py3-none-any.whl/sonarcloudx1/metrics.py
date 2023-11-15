import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar

# Represents a software Project
class Metrics(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(Metrics,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_all(self, today=False): 
		metrics = []
		try:
			logging.info("Start function: get_metrics")
			
			metrics = self.sonar.metrics.search_metrics()
			
			
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Metrics")
		
		return metrics['metrics']

	def get_metrics(self, project_key):
		metrics = None
		
		api_endpoint = f'api/metrics/search'
		
		metrics = self.retrive_data (api_endpoint=api_endpoint)
	
		return metrics['metrics']
		
	
	def get_by_project_function(self, project_id,**kwargs):
		
		metrics = []
		function = kwargs["function"]
		
		try:
			logging.info("Start function: get_metrics")
			list_metrics = self.get_metrics(project_id)
			for metric in list_metrics:
				metric['project'] = project_id
				function (data=metric, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				metrics.append (metric)
			
			return metrics
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All get_components_tree")
		return metrics	