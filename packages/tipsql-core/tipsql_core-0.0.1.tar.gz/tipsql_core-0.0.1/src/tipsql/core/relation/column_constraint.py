__all__ = ["PrimaryKey", "Index"]


class ColumnTypeConstraint:
    __slots__ = ()


class Index(ColumnTypeConstraint):
    __slots__ = ()


class UniqueIndex(Index):
    __slots__ = ()


class PrimaryKey(UniqueIndex):
    __slots__ = ()


class ForeignKey(ColumnTypeConstraint):
    __slots__ = ()
