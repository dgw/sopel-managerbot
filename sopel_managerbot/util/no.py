"""Utilities for getting "no" answers.

Part of sopel-managerbot

Copyright (c) 2025 dgw, technobabbl.es

Licensed under the Eiffel Forum License 2.
"""
from __future__ import annotations

import requests


def get_no() -> str:
    """Get a "no" answer from no-as-a-service."""
    response = requests.get('https://naas.isalman.dev/no')

    if response.status_code != 200:
        raise RuntimeError(f'Failed to get no: {response.status_code}')

    return response.json()['reason']
