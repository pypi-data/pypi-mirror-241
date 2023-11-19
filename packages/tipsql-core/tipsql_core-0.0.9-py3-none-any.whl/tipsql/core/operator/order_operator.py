from tipsql.core.operator.ge_operator import GeOperator
from tipsql.core.operator.gt_operator import GtOperator
from tipsql.core.operator.le_operator import LeOperator
from tipsql.core.operator.lt_operator import LtOperator


class OrderOperator[L, R](
    GeOperator[L, R],
    GtOperator[L, R],
    LeOperator[L, R],
    LtOperator[L, R],
):
    pass
