# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

from .docset import Docset

from typing import List, Optional

from . import docset

__all__ = ["DocsetListResponse"]

class DocsetListResponse(BaseModel):
    docsets: List[Docset]

    next: Optional[str] = None
    """URL to get the next page of results.

    Not present when there are no further results.
    """