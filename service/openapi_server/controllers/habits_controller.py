import flask
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.habit_create_request import HabitCreateRequest  # noqa: E501
from openapi_server.models.habit_response import HabitResponse  # noqa: E501
from openapi_server.models.habit_update_request import HabitUpdateRequest  # noqa: E501
from openapi_server.models.list_habits200_response import ListHabits200Response  # noqa: E501
from openapi_server import util


def create_habit(body):  # noqa: E501
    """Создать привычку

     # noqa: E501

    :param habit_create_request: 
    :type habit_create_request: dict | bytes

    :rtype: Union[HabitResponse, Tuple[HabitResponse, int], Tuple[HabitResponse, int, Dict[str, str]]
    """
    habit_create_request = body
    if flask.request.is_json:
        habit_create_request = HabitCreateRequest.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_habit(habit_id):  # noqa: E501
    """Удалить привычку

     # noqa: E501

    :param habit_id: Публичный идентификатор привычки.
    :type habit_id: str
    :type habit_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_habit(habit_id):  # noqa: E501
    """Получить одну привычку

     # noqa: E501

    :param habit_id: Публичный идентификатор привычки.
    :type habit_id: str
    :type habit_id: str

    :rtype: Union[HabitResponse, Tuple[HabitResponse, int], Tuple[HabitResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_habits(archived=None):  # noqa: E501
    """Получить список привычек текущего пользователя

     # noqa: E501

    :param archived: Включить архивные привычки, если значение равно true.
    :type archived: bool

    :rtype: Union[ListHabits200Response, Tuple[ListHabits200Response, int], Tuple[ListHabits200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_habit(habit_id, body):  # noqa: E501
    """Обновить выбранные поля привычки

     # noqa: E501

    :param habit_id: Публичный идентификатор привычки.
    :type habit_id: str
    :type habit_id: str
    :param habit_update_request: 
    :type habit_update_request: dict | bytes

    :rtype: Union[HabitResponse, Tuple[HabitResponse, int], Tuple[HabitResponse, int, Dict[str, str]]
    """
    habit_update_request = body
    if flask.request.is_json:
        habit_update_request = HabitUpdateRequest.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'
