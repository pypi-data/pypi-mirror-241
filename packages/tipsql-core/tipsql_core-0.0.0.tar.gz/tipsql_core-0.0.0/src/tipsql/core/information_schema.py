from dataclasses import dataclass


@dataclass
class Table:
    table_catalog: str
    schema_name: str
    table_name: str
    table_type: str
    columns: list["Column"]
    comment: str | None

    @property
    def class_name(self) -> str:
        from inflection import camelize, singularize

        return singularize(camelize(self.table_name))

    @property
    def name(self) -> str:
        return self.table_name

    @property
    def type(self) -> str:
        return self.table_type

    @property
    def database_name(self) -> str:
        return self.table_catalog


@dataclass
class Column:
    column_name: str
    column_default: str | None
    ordinal_position: int
    comment: str | None
    is_nullable: bool
    data_type: str
    python_type: str
    character_maximum_length: int | None
    character_octet_length: int | None
    numeric_precision: int | None
    numeric_precision_radix: int | None
    numeric_scale: int | None
    datetime_precision: int | None

    @property
    def name(self) -> str:
        return self.column_name
