import json
import decimalencoder
import todoList


def translate(event, context):
    # create a response
    print("##### Parámetros ##### \n\r")
    print(json.dumps(event['pathParameters'], indent=4))
    translation = str(
        todoList.get_translate(
            event['pathParameters']['id'],
            event['pathParameters']['language']
        )
    )
    print("##### Traducción ##### \n\r")
    if translation:
        response = {
            "statusCode": 200,
            "body": json.dumps(translation,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
