# Денис Полунин, 27 когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
from data import orders_body


def get_order_track_number():
    track_number = sender_stand_request.post_new_order(orders_body)
    return track_number.json()["track"]

def test_order_create_and_track():
    track_number = get_order_track_number()
    get_response = sender_stand_request.get_order_within_track_number(track_number)
    assert get_response.status_code == 200
