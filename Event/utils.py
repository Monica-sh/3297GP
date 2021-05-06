# this is used to get info from apiEndpoints
import json
import requests
from django.utils.http import quote

class DateUtils:
    @staticmethod
    def in_between(this_date, start, end):
        return this_date >= start and this_date <= end


class APIBuilder:
    'Build API Query string'
    def build_api(self):
        '''
        location: a location name string
        This function return a built API query string
        '''
        apiEndpoint = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch'
        qencode = self.location
        return apiEndpoint + "?q=" + qencode

    def __init__(self, location):
        self.location = location
        self.apiString = self.build_api()


class APISender:
    'Send API Query string'
    @staticmethod
    def send_request(api_builder):
        apiQuery = api_builder.apiString
        r = requests.get(apiQuery)
        if r.status_code == 200:
            return True, r.json()
        else:
            return False, None