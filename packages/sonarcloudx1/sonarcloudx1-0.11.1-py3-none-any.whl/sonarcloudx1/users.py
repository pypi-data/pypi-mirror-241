import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar

# Represents a software Project
class Users(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(Users,self).__init__(personal_access_token=personal_access_token,organization=organization)
	
	def get_by_project_function(self, project_id,**kwargs):
		function = kwargs["function"]
		users = []
		data = self.sonar.users.search_users()
		for user in data['users']:
			users.append(user)
			function (data=user, topic=kwargs["topic"], extra_data=kwargs["extra_data"])		
		
		return users

	def get_all(self, today=False): 
		users = []
		try:
			logging.info("Start function: get_users")
			
			result = list(self.sonar.users.search_users())
			
			for user in result['users']:
				users.append(user)
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Users")
		
		return users	
