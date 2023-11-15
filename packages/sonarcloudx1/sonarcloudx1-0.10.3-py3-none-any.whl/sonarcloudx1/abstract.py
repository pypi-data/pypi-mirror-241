from abc import ABC
from sonarqube import SonarQubeClient

import requests

class AbstractSonar(ABC):

    def __init__(self, personal_access_token, organization):
        self.personal_access_token = personal_access_token
        self.sonar_url = 'https://sonarcloud.io/'
        self.organization = organization
        self.sonar = SonarQubeClient(sonarqube_url=self.sonar_url, token=personal_access_token)
    
    def retrive_data (self, api_endpoint):
        url = self.sonar_url
        auth_token = self.personal_access_token
        headers = {
    		'Authorization': f'Bearer {auth_token}',
    		'Content-Type': 'application/json',
		}
        url = f'{url}{api_endpoint}'
        
        response =  requests.get(url, headers=headers)
        if response.status_code == 200:
            return  response.json()

    