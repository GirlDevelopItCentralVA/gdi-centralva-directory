import json
from pathlib import Path

from schema import Schema, Optional

from tasks import render_site

HERE = Path('.')
SCHEMA = Schema({
    'name': str,
    Optional('twitter'): str,
    Optional('email'): str,
    Optional('personal'): lambda v: v.startswith('http'),
    Optional('github'): str,
    Optional('linkedin'): lambda v: not v.startswith('http'),
})


def validate(path):
    source_path = HERE / path
    for file_path in source_path.glob('*.json'):
        with file_path.open() as fp:
            SCHEMA.validate(json.load(fp))


def test_people():
    validate('people')


def test_site_renders():
    assert render_site()
