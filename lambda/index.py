import logging

def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info("Hello world!")

    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
