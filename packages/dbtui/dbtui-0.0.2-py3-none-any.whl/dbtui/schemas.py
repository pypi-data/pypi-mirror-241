from pydantic import BaseModel


class Column(BaseModel):
    name: str
    coltype: str


class Table(BaseModel):
    name: str
    columns: list[Column]


class Schema(BaseModel):
    name: str
    tables: list[Table]

