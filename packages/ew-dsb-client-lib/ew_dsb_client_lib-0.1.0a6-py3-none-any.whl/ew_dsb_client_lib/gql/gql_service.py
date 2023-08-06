#!/usr/bin/env python3

import os
from typing import Dict
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.websockets import WebsocketsTransport
from py_dotenv import read_dotenv
from ew_dsb_client_lib.gql.entities.headers_entity import Headers

# Read dotenv
dotenv_path = os.path.join(os.path.abspath('./'), '.env')
print(dotenv_path)
read_dotenv(dotenv_path)
DEBUG:bool = (os.getenv('DEBUG', 'False') == 'True')
HTTP_URL:str = os.getenv('HTTP_URL')
WS_URL:str = os.getenv('WS_URL')
LOCAL_HTTP_URL:str = 'http://localhost:3000/graphql'
LOCAL_WS_URL:str = 'ws://localhost:3000/graphql'

class GQLService:
    http_url:str 
    ws_url:str  
    headers:Headers
    http_client: Client
    ws_client: Client

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

        if DEBUG is True:
            self.http_url = LOCAL_HTTP_URL 
            self.ws_url = LOCAL_WS_URL
        else:
            self.http_url = HTTP_URL
            self.ws_url = WS_URL

        print("{} - {} - {}".format(DEBUG, self.http_url, self.ws_url))

        self.headers = Headers( Authorization='' ).to_dict()

        http_transport = AIOHTTPTransport( url=self.http_url, headers=self.headers )
        self.http_client = Client(transport=http_transport, fetch_schema_from_transport=True)

        ws_transport = WebsocketsTransport( url=self.ws_url , init_payload=self.headers )
        self.ws_client = Client(transport=ws_transport, fetch_schema_from_transport=True)

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

        for key, value in self.__dict__.items():
            if key is 'bearer_token':
                self.headers = Headers( Authorization="".join(['Bearer ', value]) ).to_dict()

        http_transport = AIOHTTPTransport( url=self.http_url, headers=self.headers )
        self.http_client = Client(transport=http_transport, fetch_schema_from_transport=True)

        ws_transport = WebsocketsTransport( url=self.ws_url , init_payload=self.headers )
        self.ws_client = Client(transport=ws_transport, fetch_schema_from_transport=True)        
