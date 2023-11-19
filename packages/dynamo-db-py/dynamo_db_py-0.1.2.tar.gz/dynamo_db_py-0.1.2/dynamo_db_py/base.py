import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import decimal
from datetime import datetime
from schema import Schema, Optional, And, Or


class ModelReponse:

    def __init__(self, success=True, transaction=None, item=None):

        self.success = success
        self.transaction = transaction
        self.item = item



class BaseModel:

    dynamo_db_resource = boto3.resource('dynamodb')
    dynamo_db_client = boto3.client('dynamodb')

    table = dynamo_db_resource.Table('')
    composite_key = True
    
    model_schema = {}
    ignore_extra_schema_keys = True
    
    timestamp_tracking = True
    


    @classmethod
    def map_data_types(cls, data):

        dynamo_db_item = {}
        
        for key, value in data.items():

            if isinstance(value, dict):
                dynamo_db_item[key] = {'M': cls.map_data_types(value)}

            elif isinstance(value, list):
                dynamo_db_item[key] = [{'S': str(item)} for item in value]

            elif isinstance(value, int):
                dynamo_db_item[key] = {'N': str(value)}

            elif isinstance(value, float):
                dynamo_db_item[key] = {'N': str(decimal.Decimal(str(value)))}

            else:
                dynamo_db_item[key] = {'S': str(value)}

        return dynamo_db_item


    @classmethod
    def validate_data(cls, data, full_validation=True):

        if full_validation:
            schema = Schema(cls.model_schema, ignore_extra_keys=cls.ignore_extra_schema_keys)
            
        else:
            schema = Schema({Optional(k):v for k,v in cls.model_schema.items()}, ignore_extra_keys=cls.ignore_extra_schema_keys)

        return schema.validate(data)

    
    @classmethod
    def create(cls, raw_data, transaction=False, full_validation=True, batch=None, overwrite=False):

        data = cls.validate_data(raw_data, full_validation=full_validation)

        if cls.timestamp_tracking:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            data['inserted_at'] = timestamp
            data['updated_at'] = timestamp


        if transaction:
            return ModelReponse(
                transaction={
                    'Put': {
                    'Item': cls.map_data_types(data),
                    'TableName': cls.table.table_name
                    }
                }
            )            
        
        elif batch:
            batch.put_item(Item=data)
            return ModelReponse()

        else:
            try:
                cls.table.put_item(
                    Item=data,
                    ConditionExpression=Attr('PK').not_exists() & Attr('SK').not_exists()
                )
                return ModelReponse()

            except cls.dynamo_db_client.exceptions.ConditionalCheckFailedException:
                
                if overwrite:
                    cls.update(raw_data,transaction=transaction, full_validation=full_validation)
                    return ModelReponse()
                
                else:
                    return ModelReponse(success=False)



    @classmethod
    def update(cls, new_data, transaction=False, full_validation=True):

        new_data = cls.validate_data(new_data, full_validation=full_validation)

        if cls.composite_key:
            PK = new_data.pop('PK')
            SK = new_data.pop('SK')
            key = {'PK': PK, 'SK': SK}

        else:
            PK = new_data.pop('PK')
            key = {'PK': PK}

        if cls.timestamp_tracking:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            new_data['updated_at'] = timestamp

        update_expression = 'SET ' + ' ,'.join([f'{key}=:{key}' for key in new_data.keys()])
        expression_attribute_values = {f':{key}':value for key,value in new_data.items()}

        if transaction:
            return ModelReponse(
                transaction={
                    'Update': {
                        'Key': cls.map_data_types(key),
                        'UpdateExpression': update_expression,
                        'ExpressionAttributeValues': cls.map_data_types(expression_attribute_values),
                        'TableName': cls.table.table_name
                    }
                }
            )

        else:
            cls.table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            return ModelReponse()

    
    @classmethod
    def get(cls, PK, SK=None):

        if cls.composite_key and not SK:
            raise Exception('Missing Sort Key')
        
        key = {'PK': PK, 'SK': SK} if cls.composite_key else {'PK': PK}

        item = cls.table.get_item(Key=key)['Item']

        return ModelReponse(item=item)
        

    @classmethod
    def delete(cls, PK, SK=None):

        if cls.composite_key and not SK:
            raise Exception('Missing Sort Key')
        
        key = {'PK': PK, 'SK': SK} if cls.composite_key else {'PK': PK}
        cls.table.delete_item(Key=key)

        return ModelReponse()