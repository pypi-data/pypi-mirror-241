from tipsql.core.query.condition import Condition, ExprCondition
from tipsql.core.query.expression import Expression
from tipsql.core.relation.trait import SelectableRelation


class ConditionContext[*Ts, T: SelectableRelation]:
    __slots__ = ()

    def __call__(self, expr: Expression[*Ts, T]) -> Condition[*Ts, T]:
        return ExprCondition(expr)
