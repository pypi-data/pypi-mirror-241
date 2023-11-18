from beanie import Document
from typing import Optional
from resources.orm.DatasetStats import DatasetStats


# TODO: Integrate Python Library for ISO 639-1


class Language(Document):
    name: str
    iso_code: str
    language_stats: Optional[DatasetStats] = None
