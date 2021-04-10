
def lambda_handler(event, context):
    # Get first name and last name from event object
    first_name = event.get('first_name', None)
    last_name = event.get('last_name', None)
    
    # If the parameters exist in the event object
    if first_name is not None and last_name is not None:
        
        # Buid the output by concatenating first name and last name
        output = '{} {}'.format(first_name, last_name)
        
        # Return response
        return {
            'statusCode': 200,
            'output': output
        }
    
    # If the parameters do not exist return status code 400
    else:
        return {
            'statusCode': 400,
            'output': 'Bad Request: Missing Parameters'
        }
        
