import unittest

from flask import json

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.habit_create_request import HabitCreateRequest  # noqa: E501
from openapi_server.models.habit_response import HabitResponse  # noqa: E501
from openapi_server.models.habit_update_request import HabitUpdateRequest  # noqa: E501
from openapi_server.models.list_habits200_response import ListHabits200Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHabitsController(BaseTestCase):
    """HabitsController integration test stubs"""

    def test_create_habit(self):
        """Test case for create_habit

        Создать привычку
        """
        habit_create_request = {"name":"Пить воду","description":"Выпивать восемь стаканов в день.","frequency":"daily","targetPerWeek":1}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits',
            method='POST',
            headers=headers,
            data=json.dumps(habit_create_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_habit(self):
        """Test case for delete_habit

        Удалить привычку
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits/{habit_id}'.format(habit_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_habit(self):
        """Test case for get_habit

        Получить одну привычку
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits/{habit_id}'.format(habit_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_habits(self):
        """Test case for list_habits

        Получить список привычек текущего пользователя
        """
        query_string = [('archived', False)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_habit(self):
        """Test case for update_habit

        Обновить выбранные поля привычки
        """
        habit_update_request = {"name":"name","description":"description","frequency":"daily","targetPerWeek":1,"archived":True}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits/{habit_id}'.format(habit_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='PATCH',
            headers=headers,
            data=json.dumps(habit_update_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
