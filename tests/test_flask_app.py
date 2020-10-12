from src_app.app import sum_list_range
import json
import pytest

expected_payload = json.loads("""{"total": 50000005000000}""")
test_invalid_output = json.loads("""{"total": 10000001000000}""")
test_sum_list_range_total = [125250]


def test_index(client):
    assert True


# test unprovisioned url
def test_home_page_url(client):
    res = client.get('/')
    assert res.status_code == 404


# test valid route
def test_valid_route(client):
    res = client.get('/total')
    assert res.status_code == 200


# test total output
@pytest.mark.parametrize("expected_output", expected_payload)
def test_total(app, client, expected_output):
    response = client.get('/total')
    expected = expected_payload
    assert expected == json.loads(response.get_data(as_text=True))


# test invalid output
@pytest.mark.parametrize("unexpected_output", test_invalid_output)
def test_total(app, client, unexpected_output):
    response = client.get('/total')
    expected = test_invalid_output
    assert expected != json.loads(response.get_data(as_text=True))


# test app function
@pytest.mark.parametrize("expected_output", test_sum_list_range_total)
def test_sum_range(expected_output):
    numbers_to_add = list(range(501))
    actual_output = sum_list_range(numbers_to_add, numbers_to_add[0], numbers_to_add[-1])
    assert actual_output == expected_output
