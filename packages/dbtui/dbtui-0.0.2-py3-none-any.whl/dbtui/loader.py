from dbtui.schemas import Column, Schema, Table


class SchemaLoader:

    def __init__(self, url: str) -> None:
        self.url = url

    def load(self) -> Schema:
        return Schema(
            name="default",
            tables=[
                Table(name="users", columns=[
                    Column(name="username", coltype="string"),
                    Column(name="email", coltype="string"),
                ])
            ],
        )

