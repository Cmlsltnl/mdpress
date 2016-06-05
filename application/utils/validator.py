#!/usr/bin/env python
# encoding: utf-8
import re

from voluptuous import All, Length, Schema, Invalid


def validate_email(email):
    """Validate email."""
    if not re.match(r"[^@]{5,16}@[^@]{2,10}\.[^@]{3,5}", email):
        raise Invalid("This email is invalid.")
    return email


user_schema = Schema({
    'email': validate_email,
    'username': All(basestring, Length(min=5, max=16)),
    'password': All(basestring, Length(min=8, max=16))
})

post_schema = Schema({
    'title': All(basestring, Length(max=100)),
    'excerpt': All(basestring, Length(max=100)),
    'content': basestring,
    'user': int,
    'categories': basestring,
    'tags': basestring,
    'status': basestring
})
