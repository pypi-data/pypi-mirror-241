from typing_extensions import TypedDict
from typing import Optional, List
from beanie import Document, Link, WriteRules
from resources.orm.License import License
from enum import Enum
from resources.orm.Language import Language
from resources.orm.DatasetStats import DatasetStats
from resources.orm.Author import Author
from resources.orm.Conference import Conference
from pydantic import BaseModel


class Status(Enum):
    BROKEN_LINK = 1
    READY = 2


class Hrefs(BaseModel):
    link_source: str
    link_hf: Optional[str] = None
    doi: Optional[str] = None


class Dataset(Document):
    name: str
    languages: List[Link[Language]]
    conference: Optional[Link[Conference]] = None
    hrefs: Hrefs
    year: int
    # Status is an Enum
    status: Status
    overall_dataset_stats: Optional[DatasetStats] = None
    authors: List[Link[Author]]
    license: Optional[Link[License]] = []