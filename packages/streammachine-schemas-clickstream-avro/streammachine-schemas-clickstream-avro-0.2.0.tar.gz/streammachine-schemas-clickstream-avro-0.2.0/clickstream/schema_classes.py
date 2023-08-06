import json
import os.path
import decimal
import datetime
import six
from avrogen.dict_wrapper import DictWrapper
from avrogen import avrojson
from avro import schema as avro_schema
if six.PY3:    from avro.schema import SchemaFromJSONData as make_avsc_object
    
else:
    from avro.schema import make_avsc_object
    


def __read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()

def __get_names_and_schema(file_name):
    names = avro_schema.Names()
    schema = make_avsc_object(json.loads(__read_file(file_name)), names)
    return names, schema

__NAMES, SCHEMA = __get_names_and_schema(os.path.join(os.path.dirname(__file__), "schema.avsc"))
__SCHEMAS = {}
def get_schema_type(fullname):
    return __SCHEMAS.get(fullname)
__SCHEMAS = dict((n.fullname.lstrip("."), n) for n in six.itervalues(__NAMES.names))


class SchemaClasses(object):
    
    
    pass
    class io(object):
        class streammachine(object):
            class public_schemas(object):
                class clickstream(object):
                    
                    class ClickstreamEventClass(DictWrapper):
                        
                        """
                        
                        """
                        
                        
                        RECORD_SCHEMA = get_schema_type("io.streammachine.public_schemas.clickstream.ClickstreamEvent")
                        
                        
                        def __init__(self, inner_dict=None):
                            super(SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass, self).__init__(inner_dict)
                            if inner_dict is None:
                                self.strmMeta = SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass()
                                self.producerSessionId = str()
                                self.url = str()
                                self.eventType = str()
                                self.referrer = str()
                                self.userAgent = str()
                                self.conversion = int()
                                self.customer = SchemaClasses.io.streammachine.public_schemas.clickstream.CustomerClass()
                                self.abTests = list()
                        
                        
                        @property
                        def strmMeta(self):
                            """
                            :rtype: SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass
                            """
                            return self._inner_dict.get('strmMeta')
                        
                        @strmMeta.setter
                        def strmMeta(self, value):
                            #"""
                            #:param SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass value:
                            #"""
                            self._inner_dict['strmMeta'] = value
                        
                        
                        @property
                        def producerSessionId(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('producerSessionId')
                        
                        @producerSessionId.setter
                        def producerSessionId(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['producerSessionId'] = value
                        
                        
                        @property
                        def url(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('url')
                        
                        @url.setter
                        def url(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['url'] = value
                        
                        
                        @property
                        def eventType(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('eventType')
                        
                        @eventType.setter
                        def eventType(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['eventType'] = value
                        
                        
                        @property
                        def referrer(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('referrer')
                        
                        @referrer.setter
                        def referrer(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['referrer'] = value
                        
                        
                        @property
                        def userAgent(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('userAgent')
                        
                        @userAgent.setter
                        def userAgent(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['userAgent'] = value
                        
                        
                        @property
                        def conversion(self):
                            """
                            :rtype: int
                            """
                            return self._inner_dict.get('conversion')
                        
                        @conversion.setter
                        def conversion(self, value):
                            #"""
                            #:param int value:
                            #"""
                            self._inner_dict['conversion'] = value
                        
                        
                        @property
                        def customer(self):
                            """
                            :rtype: SchemaClasses.io.streammachine.public_schemas.clickstream.CustomerClass
                            """
                            return self._inner_dict.get('customer')
                        
                        @customer.setter
                        def customer(self, value):
                            #"""
                            #:param SchemaClasses.io.streammachine.public_schemas.clickstream.CustomerClass value:
                            #"""
                            self._inner_dict['customer'] = value
                        
                        
                        @property
                        def abTests(self):
                            """
                            :rtype: list[str]
                            """
                            return self._inner_dict.get('abTests')
                        
                        @abTests.setter
                        def abTests(self, value):
                            #"""
                            #:param list[str] value:
                            #"""
                            self._inner_dict['abTests'] = value
                        
                        
                    class CustomerClass(DictWrapper):
                        
                        """
                        
                        """
                        
                        
                        RECORD_SCHEMA = get_schema_type("io.streammachine.public_schemas.clickstream.Customer")
                        
                        
                        def __init__(self, inner_dict=None):
                            super(SchemaClasses.io.streammachine.public_schemas.clickstream.CustomerClass, self).__init__(inner_dict)
                            if inner_dict is None:
                                self.id = str()
                        
                        
                        @property
                        def id(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('id')
                        
                        @id.setter
                        def id(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['id'] = value
                        
                        
                    class StrmMetaClass(DictWrapper):
                        
                        """
                        
                        """
                        
                        
                        RECORD_SCHEMA = get_schema_type("io.streammachine.public_schemas.clickstream.StrmMeta")
                        
                        
                        def __init__(self, inner_dict=None):
                            super(SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass, self).__init__(inner_dict)
                            if inner_dict is None:
                                self.schemaId = str()
                                self.nonce = int()
                                self.timestamp = int()
                                self.keyLink = SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass.RECORD_SCHEMA.fields[3].default
                                self.billingId = SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass.RECORD_SCHEMA.fields[4].default
                                self.consentLevels = list()
                        
                        
                        @property
                        def schemaId(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('schemaId')
                        
                        @schemaId.setter
                        def schemaId(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['schemaId'] = value
                        
                        
                        @property
                        def nonce(self):
                            """
                            :rtype: int
                            """
                            return self._inner_dict.get('nonce')
                        
                        @nonce.setter
                        def nonce(self, value):
                            #"""
                            #:param int value:
                            #"""
                            self._inner_dict['nonce'] = value
                        
                        
                        @property
                        def timestamp(self):
                            """
                            :rtype: int
                            """
                            return self._inner_dict.get('timestamp')
                        
                        @timestamp.setter
                        def timestamp(self, value):
                            #"""
                            #:param int value:
                            #"""
                            self._inner_dict['timestamp'] = value
                        
                        
                        @property
                        def keyLink(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('keyLink')
                        
                        @keyLink.setter
                        def keyLink(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['keyLink'] = value
                        
                        
                        @property
                        def billingId(self):
                            """
                            :rtype: str
                            """
                            return self._inner_dict.get('billingId')
                        
                        @billingId.setter
                        def billingId(self, value):
                            #"""
                            #:param str value:
                            #"""
                            self._inner_dict['billingId'] = value
                        
                        
                        @property
                        def consentLevels(self):
                            """
                            :rtype: list[int]
                            """
                            return self._inner_dict.get('consentLevels')
                        
                        @consentLevels.setter
                        def consentLevels(self, value):
                            #"""
                            #:param list[int] value:
                            #"""
                            self._inner_dict['consentLevels'] = value
                        
                        
                    pass
                    
__SCHEMA_TYPES = {
'io.streammachine.public_schemas.clickstream.ClickstreamEvent': SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass,
    'io.streammachine.public_schemas.clickstream.Customer': SchemaClasses.io.streammachine.public_schemas.clickstream.CustomerClass,
    'io.streammachine.public_schemas.clickstream.StrmMeta': SchemaClasses.io.streammachine.public_schemas.clickstream.StrmMetaClass,
    
}
_json_converter = avrojson.AvroJsonConverter(use_logical_types=False, schema_types=__SCHEMA_TYPES)

# Stream Machine additions
from streammachine.schemas.common import StreamMachineEvent

def get_strm_schema_id(self) -> str:
    return self.strmMeta.schemaId

def get_strm_schema(self):
    return self.RECORD_SCHEMA

def get_strm_schema_type(self):
    return "avro"

setattr(SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass, "get_strm_schema_id", get_strm_schema_id)
setattr(SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass, "get_strm_schema", get_strm_schema)
setattr(SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass, "get_strm_schema_type", get_strm_schema_type)

# TODO this needs some python guru-ism
# Currently the generated class does not implement the abstract base class
# StreamMachineEvent
# Maybe start here
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
# this code leads to a stack overflow when instantiating an instance
# SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass = type('SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass', (SchemaClasses.io.streammachine.public_schemas.clickstream.ClickstreamEventClass, StreamMachineEvent,), dict())
