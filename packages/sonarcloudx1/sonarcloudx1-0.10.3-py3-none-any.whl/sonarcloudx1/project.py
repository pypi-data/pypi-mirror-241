import logging
logging.basicConfig(level=logging.INFO)
from sonarcloudx1.abstract import AbstractSonar

# Represents a software Project
class Project(AbstractSonar):

	def __init__(self,personal_access_token, organization):
		super(Project,self).__init__(personal_access_token=personal_access_token, organization=organization)

	def get_qnt_paginas(self):

		try:
			logging.info("Start function: get_projects_qnt_paginas")
			result = self.sonar.projects.search_projects(organization=self.organization)
			quant = result['paging']['total']/100 #100 é o atributo ps DEFAULT. ps = número de elementos por página.
			quant = int(quant) + 1
			return quant

		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__)

	logging.info("Retrieve quantidade de paginas")				
		
	def get_all_function(self, today=False, **kwargs): 
		
		result = []
		
		try:
			
			function = kwargs["function"]

			for pagina in range(0, self.get_qnt_paginas()): #Resolvendo o problema de paginação
				projetos = self.sonar.projects.search_projects(organization=self.organization, p=pagina)
				for project in projetos['components']:
					result.append(project)
					if function is not None:
						function (data=project, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Projects")
		return result	

	def get_all(self, today=False): 

		try:
			
			logging.info("Start function: get_projects")
			
			saida = []
			
			for pagina in range(0, self.get_qnt_paginas()): #Resolvendo o problema de paginação
				projetos = self.sonar.projects.search_projects(organization=self.organization, p=pagina)
				saida.append(projetos['components'])

			
		except Exception as e: 
			logging.error("OS error: {0}".format(e))
			logging.error(e.__dict__) 

		logging.info("Retrieve All Projects")
		
		return saida	


