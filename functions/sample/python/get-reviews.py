#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator("9-LTFnBHCA9EK8YpdvjGraFP0gtX9366prWjkxM07zof")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://dd861025-429b-4710-b356-73157a090dbc-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_find(
                db='reviews',
                selector={'dealership': {'$eq': int(dict['dealerID'])}},
            ).get_result()
    try:
        # result_by_filter=my_database.get_query_result(selector,raw_result=True)
        result= {
            'headers': {'Content-Type':'application/json'},
            'body': {'data':response}
            }
        return result
    except:
        return {
            'statusCode': 404,
            'message': 'Something went wrong'
            }