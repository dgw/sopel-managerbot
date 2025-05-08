"""Utilities for getting "yes" answers.

Part of sopel-managerbot

Copyright (c) 2025 dgw, technobabbl.es

Licensed under the Eiffel Forum License 2.
"""
from __future__ import annotations

import requests


def get_yes() -> str:
    """Get a "yes" answer from yes-as-a-service."""
    response = requests.get('https://yes-as-a-service.onrender.com/yes')

    if response.status_code != 200:
        raise RuntimeError(f'Failed to get yes: {response.status_code}')

    return response.json()['yes']
