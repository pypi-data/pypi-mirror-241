from datetime import datetime
from typing import List

from protean import BaseAggregate, BaseRepository
from protean.fields import DateTime, Integer, String


class Person(BaseAggregate):
    first_name = String(max_length=50, required=True)
    last_name = String(max_length=50, required=True)
    age = Integer(default=21)
    created_at = DateTime(default=datetime.now())


class PersonRepository(BaseRepository):
    def find_adults(self, age: int = 21) -> List[Person]:
        pass  # FIXME Implement filter method


class User(BaseAggregate):
    email = String(max_length=255, required=True, unique=True)
    password = String(max_length=3026)
