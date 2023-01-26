import json
import decimalencoder
import todoList


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    print("##### Parámtros ##### \n\r")
    print(json.dumps(event['pathParameters'], indent=4))
    translation = str(
        todoList.get_translate(
            item['text'], event['pathParameters']['language']
        )
    )
    item["text"] = translation
    print("##### Traducció ##### \n\r")
    print(
        json.dumps(
            item["text"], cls=decimalencoder.DecimalEncoder, indent=4
        )
    )
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
