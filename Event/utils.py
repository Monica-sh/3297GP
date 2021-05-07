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
    @staticmethod
    def is_infector(public_event, case):
        three_days_before_date_of_symptoms = case.Date_of_Symptoms + datetime.timedelta(days=-3)
        date_of_confirmation = case.Date_of_Confirmation
        return DateUtils.in_between(public_event.date, three_days_before_date_of_symptoms, date_of_confirmation)
    
    @staticmethod
    def is_infected(public_event, case):
        fourteen_days_before_date_of_symptoms = case.Date_of_Symptoms + datetime.timedelta(days=-14)
        two_dys_before_date_of_symptoms = case.Date_of_Symptoms + datetime.timedelta(days=-2)
        return DateUtils.in_between(public_event.date, fourteen_days_before_date_of_symptoms, two_dys_before_date_of_symptoms)


class SSEPersonalEventData:
    '''Pass information to view: personal event + type'''
    def __init__(self, personal_event):
        self.case_number = personal_event.case.Case_Number
        self.event_description = personal_event.description
        type_list = []
        if SSEUtils.is_infector(personal_event.event, personal_event.case):
            type_list.append("Infector")
        if SSEUtils.is_infected(personal_event.event, personal_event.case):
            type_list.append("Infected")
        self.type = ", ".join(type_list)
    
    
    @staticmethod
    def list_convert(personal_data_list):
        return list(map(SSEPersonalEventData, personal_data_list))