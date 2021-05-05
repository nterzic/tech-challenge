# tech-challenge

# Challenge 2

Goal: Retrieve the meta data of an aws ec2 instance and provide a json formatted output.

Assumptions:

- Program is executed on aws ec2 instance
- Program relays on / being an indicator of the endpoint depth.
  In other words, if endpoint endswith /, program assumes there are children endpoints.
  If endpoint does not endwith /, program assumes there are not children endpoints.

# Challenge 3

Goal: Provided inputs are dictionary and a string key. Return back the value based on the string key

Example:

    input_2_obj = {"x":{"y":{"z":"a"}}}
    input_2_key = 'x/y/z'
    result_output = recurisive_get_value(input_2_obj, input_2_key)
    result_output would be "a"
