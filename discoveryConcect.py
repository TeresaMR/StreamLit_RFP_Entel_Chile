import getpass
from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import DiscoveryV2
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class Discovery:
    def connect():
        authenticator = IAMAuthenticator('hYTrs6vDuY3edE0Xm614cgtnsIKIRyCQGGPokwfAcSu8')
        discovery = DiscoveryV2(
            version='2023-03-31',
            authenticator=authenticator
        )

        discovery.set_disable_ssl_verification(True)
        discovery.set_service_url('https://api.us-south.discovery.watson.cloud.ibm.com/instances/c0369220-e484-47ee-8217-f6023f5ac1e0')

        #results=discovery.list_projects()
        #ccu_project=discovery.get_project(project_id="12e10755-8c6e-47c3-8f31-0a9fa4eb291d")
        #collections=discovery.list_collections(project_id="12e10755-8c6e-47c3-8f31-0a9fa4eb291d")

        return discovery


    def getDocuments(discovery):
        response = discovery.get_project(project_id="12e10755-8c6e-47c3-8f31-0a9fa4eb291d")

        if response.get_status_code() == 200 or response.get_status_code() == 201 or response.get_status_code() == 202 or response.get_status_code() == 203:
           print("hay contenido")
           print(response.get_result())
           return response.get_result()
        elif response.get_status_code() == 204:
          print("no trae contenido")
          return response.get_status_code()

    def callDiscDocument():
       discovery=Discovery.connect()
       documents=Discovery.getDocuments(discovery)
       return documents

    
    
## try:
        
    ##except ApiException as ex:
       ## print "Method failed with status code " + str(ex.code) + ": " + ex.message
    




