#!/usr/bin/env python3
"""
    __init__ for models directory
"""
from AirBnB_clone.models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
