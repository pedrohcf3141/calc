import os
import tempfile

import pytest

from edukalculadora import app as create_app


@pytest.fixture
def client():
    client = create_app.test_client()
    return client

def test_home_status_code_ok(client):

    resp = client.get('/')
    assert 200 == resp.status_code

def test_home_status_code_ok(client):

    resp = client.get('/')
    assert 200 == resp.status_code