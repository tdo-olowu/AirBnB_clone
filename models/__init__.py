#!/usr/bin/python3
"""initialiser for this package"""


from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
