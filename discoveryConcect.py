import getpass
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import DiscoveryV2 
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

class Discovery:
    
    def connect():
        authenticator = IAMAuthenticator('81Bo-kKlAVYWBHpAmwJBcVES8vqLM9d7RO6RPrVfnRS0')
        discovery = DiscoveryV2(
            version='2023-03-31',
            authenticator=authenticator
        )

        discovery.set_disable_ssl_verification(True)
        discovery.set_service_url('https://api.us-south.discovery.watson.cloud.ibm.com/instances/df4065c0-d420-4a44-94f8-bc92b9a2f4cc')

        #results=discovery.list_projects()
        #ccu_project=discovery.get_project(project_id="12e10755-8c6e-47c3-8f31-0a9fa4eb291d")
        #collections=discovery.list_collections(project_id="12e10755-8c6e-47c3-8f31-0a9fa4eb291d")

        return discovery

    def getQuery(prompt,discovery):
        result=discovery.query(
            project_id='5007d298-ec25-497e-ac9d-fd058a095ebc',
            natural_language_query= prompt,
            ).get_result()
        return result
       

    def getDocuments(prompt,discovery):
       #response = discovery.get_project(project_id="12e10755-8c6e-47c3-8f31-0a9fa4eb291d")
        response=Discovery.getQuery(prompt,discovery)
        print(response)

    def callDiscDocument(prompt):
       discovery=Discovery.connect()
       documents=Discovery.getDocuments(prompt,discovery)
       return documents

    
    
## try:
        
    ##except ApiException as ex:
       ## print "Method failed with status code " + str(ex.code) + ": " + ex.message
    




