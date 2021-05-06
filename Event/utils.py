# this is used to get info from apiEndpoints
import json
import requests
from django.utils.http import quote
import datetime

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


class SSEUtils:
    '''tools for SSE find'''
    def __init__(self, public_event):
        self.event = public_event
    
    def is_infector(case):
        three_days_before_date_of_symptoms = case.Date_of_Symptoms + datetime.timedelta(days=-3)
        date_of_confirmation = case.Date_of_Confirmation
        return DateUtils.in_between(three_days_before_date_of_symptoms, date_of_confirmation)
    
    def is_infected(case):
        fourteen_days_before_date_of_symptoms = case.Date_of_Symptoms + datetime.timedelta(days=-14)
        two_dys_before_date_of_symptoms = case.Date_of_Symptoms + datetime.timedelta(days=-2)
        return DateUtils.in_between(fourteen_days_before_date_of_symptoms, two_dys_before_date_of_symptoms)