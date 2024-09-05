#!/usr/bin/env python3
"""API authentication module.
"""
import os
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Handles authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines if a path needs authentication.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header from the request.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Fetches the current user from the request.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """Retrieves the value of the SESSION_NAME cookie.
        """
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
