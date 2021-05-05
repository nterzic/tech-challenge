import requests
import json 
from challenge_3 import recurisive_get_value

class AwsMetaData():

    def __init__(self):
        self.base_url = "http://169.254.169.254"
        self.token = None

    def _get_token(self):

        get_token_url = '{}/latest/api/token'.format(self.base_url)
        headers = {"X-aws-ec2-metadata-token-ttl-seconds": "21600"}
        resp = requests.put(get_token_url, headers=headers)
        if resp.status_code != 200:
            raise Exception('Unable to rertrive api token {}/latest/api/token. Error -- {}'.format(self.base_url, resp.status_code))

        self.token = resp.content.decode("utf-8")
        return self.token

    def get_specific_metadata_key(self, endpoint_key):

        if self.token is None:
            self._get_token()
        
        get_specific_metadata_value_url = "{}/latest/{}".format(self.base_url, endpoint_key)
        # print("calling --- ", get_specific_metadata_value_url)
        headers = {"X-aws-ec2-metadata-token": self.token}
        resp = requests.get(get_specific_metadata_value_url, headers=headers)

        if resp.status_code == 200:
            current_meta_val = resp.content.decode('utf-8') if isinstance(resp.content, bytes) else resp.content
            return (resp.status_code, current_meta_val)
        else:
            msg = "Invalid Endpoint -- {}. HTTP Status code -- {}".format(endpoint_key, resp.status_code)
            return (resp.status_code, msg)

    
    def recursive_get_all_endpoints(self, endpoint_arr):
        
        res = {}
        for endpoint_str in endpoint_arr:

            resp = self.get_specific_metadata_key(endpoint_str)
            response_value = resp[1]
            keys = endpoint_str.split('/')
            keys = list(filter(lambda x: x != "", keys))  # filter out any empty strings
            all_children_endpoints = []

            # Handling json case, since json format would break logic of getting all_children_endpoints 
            try:
                json.loads(response_value)
            except:
                all_children_endpoints = response_value.split('\n')
            
            # endpoints ending with /, indicates in most cases children endpoints
            if endpoint_str.endswith('/'):
                if len(all_children_endpoints):
                    new_endpoints = ["{0:s}/{1:s}".format(endpoint_str.rstrip('/'), el) for el in all_children_endpoints]
                    keys = list(filter(lambda x: x != "", keys))  # filter out any empty strings
                    res[keys[-1]] = self.recursive_get_all_endpoints(new_endpoints)
                else:
                    res[keys[-1]] = response_value
                
            else:
                if len(keys):
                    res[keys[-1]] = response_value
                else:    
                    res[endpoint_str] = response_value
        
        return res
        
            
    def get_all_meta_info(self, endpoint=['meta-data/']):
        
        if not isinstance(endpoint, str) and not isinstance(endpoint, list):
            raise ValueError("Endpoint param needs to be either str or list. \nProvided input endpoint was {} which is of {}".format(endpoint, type(endpoint)))
        if isinstance(endpoint, str):
            endpoint = [endpoint]
        
        all_meta_data_info_json = json.dumps(self.recursive_get_all_endpoints(endpoint))
        return all_meta_data_info_json


if __name__ == '__main__':
    aws_meta_obj = AwsMetaData()
    endpoint_key = "meta-data/events/maintenance/history"
    specific_meta_data_key = aws_meta_obj.get_specific_metadata_key(endpoint_key)[1]
    print("response for meta key {} -- {}".format(endpoint_key, specific_meta_data_key))
    print("----------"*5)
    meta_json = aws_meta_obj.get_all_meta_info()
    print("JSON OUTPUT --", meta_json, type(meta_json))

    print("#####################"*5)
    # TESTING Challenge 3
    # which is also retrieving data key individually, but post actual metadata request
    # This could be used if want to cache entire metadata json, and then retrieve keys many times, instead of making request calls for every single specific endpoint
    print("TESTING challenge 3")
    print("---------------------"*5)
    meta_dict = json.loads(meta_json)
    print(recurisive_get_value(meta_dict, 'meta-data/events/maintenance/history'))
    print("---------------------"*5)
    print(recurisive_get_value(meta_dict, 'meta-data/network/interfaces'))
    print("---------------------"*5)

    
    



