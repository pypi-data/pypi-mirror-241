from tipsql.core.relation.table import Table
from tipsql.core.relation.temporary_table import NamedTemporaryTable

type SelectableRelation = Table | NamedTemporaryTable
"""
A type alias for a selectable relation.
"""

type InsertableRelation = Table
"""
A type alias for an insertable relation.
"""
