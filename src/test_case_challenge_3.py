
from challenge_3 import recurisive_get_value

def test_give_examples():

    # Test valid example input 1
    input_1_obj = {"a":{"b":{"c":"d"}}}
    input_1_key = 'a/b/c'
    assert recurisive_get_value(input_1_obj, input_1_key) == "d"

    # Test valid example input 2
    input_2_obj = {"x":{"y":{"z":"a"}}}
    input_2_key = 'x/y/z'
    assert recurisive_get_value(input_2_obj, input_2_key) == "a"

    ## Test valid example input 1
    input_1_obj = {"a":{"b":{"c":"d"}}}
    input_1_key = 'a'
    assert recurisive_get_value(input_1_obj, input_1_key) == {"b":{"c":"d"}}

def test_with_aws_metadata():

    meta_dict = {'meta-data': {'services': {'domain': u'amazonaws.com', 'partition': u'aws'}, 'hibernation': {'configured': u'false'}, 'instance-type': u't2.micro', 'instance-id': u'i-00dba24feb0aaba12', 'local-hostname': u'ip-172-31-89-19.ec2.internal', 'network': {'interfaces': {'macs': {'12:dc:4b:8c:6d:31': {'local-hostname': u'ip-172-31-89-19.ec2.internal', 'security-groups': u'launch-wizard-1', 'public-hostname': u'ec2-3-86-177-10.compute-1.amazonaws.com', 'vpc-ipv4-cidr-blocks': u'172.31.0.0/16', 'subnet-id': u'subnet-07ac93bb37bed78ea', 'public-ipv4s': u'3.86.177.10', 'interface-id': u'eni-0d92028f0482d8aca', 'mac': u'12:dc:4b:8c:6d:31', 'security-group-ids': u'sg-0bb6eeb5d2bfbad8d', 'vpc-ipv4-cidr-block': u'172.31.0.0/16', 'owner-id': u'307124635785', 'local-ipv4s': u'172.31.89.19', 'subnet-ipv4-cidr-block': u'172.31.80.0/20', 'vpc-id': u'vpc-04c3c696408eb91bf', 'device-number': u'0', 'ipv4-associations': {'3.86.177.10': u'172.31.89.19'}}}}}, 'hostname': u'ip-172-31-89-19.ec2.internal', 'ami-id': u'ami-0742b4e673072066f', 'instance-action': u'none', 'events': {'maintenance': {'scheduled': u'[]', 'history': u'[]'}}, 'profile': u'default-hvm', 'reservation-id': u'r-052763d5b8edef1b5', 'security-groups': u'launch-wizard-1', 'instance-life-cycle': u'on-demand', 'identity-credentials': {'ec2': {'info': u'{\n  "Code" : "Success",\n  "LastUpdated" : "2021-04-26T09:05:32Z",\n  "AccountId" : "307124635785"\n}', 'security-credentials': {'ec2-instance': u'{\n  "Code" : "Success",\n  "LastUpdated" : "2021-04-26T09:05:09Z",\n  "Type" : "AWS-HMAC",\n  "AccessKeyId" : "DUMMY_VAL_AccessKeyId",\n  "SecretAccessKey" : "DUMMY_VAL_SecretAccessKey",\n  "Token" : "DUMMY_VAL_Token",\n  "Expiration" : "2021-04-26T15:29:27Z"\n}'}}}, 'metrics': {'vhostmd': u'<?xml version="1.0" encoding="UTF-8"?>'}, 'mac': u'12:dc:4b:8c:6d:31', 'public-ipv4': u'3.86.177.10', 'ami-manifest-path': u'(unknown)', 'local-ipv4': u'172.31.89.19', 'placement': {'region': u'us-east-1', 'availability-zone': u'us-east-1d', 'availability-zone-id': u'use1-az2'}, 'ami-launch-index': u'0', 'public-hostname': u'ec2-3-86-177-10.compute-1.amazonaws.com', 'public-keys': {'0=challenge': 'Invalid Endpoint -- meta-data/public-keys/0=challenge. HTTP Status code -- 404'}, 'block-device-mapping': {'ami': u'/dev/xvda', 'root': u'/dev/xvda'}}}
    
    # Test 1
    endpoint_key_1 = "meta-data/events/maintenance/history"
    assert recurisive_get_value(meta_dict, endpoint_key_1) == '[]'

    # Test 2
    endpoint_key_1 = "meta-data/services/domain"
    assert recurisive_get_value(meta_dict, endpoint_key_1) == 'amazonaws.com'

def test_wrong_input():
    _input = ['a','n']
    assert recurisive_get_value(_input, 's') == None

