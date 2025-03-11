#!/usr/bin/env python
# encoding: utf-8

"""
ConfFileModel.py

Insecure Keyring Backend configuration file data model.

author  : stefan schablowski
contact : stefan.schablowski@desmodyne.com
created : 2025-03-11
"""


from pathlib import Path

# https://pypi.org/project/pydantic
from pydantic import BaseModel, ConfigDict


# -----------------------------------------------------------------------------
# public types

class ConfFileModel(BaseModel):
    """
    Pydantic model that defines configuration file attributes.
    """

    model_config = ConfigDict(extra='forbid')
    path_to_log_file:  Path
