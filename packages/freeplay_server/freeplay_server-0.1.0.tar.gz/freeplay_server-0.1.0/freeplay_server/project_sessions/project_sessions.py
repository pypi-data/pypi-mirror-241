from _decimal import Decimal
from datetime import datetime
from typing import Optional, Union


# This class exposes shared logic used by SqlAlchemy (ORM) and Record based (raw SQL) model types.
# Though simple calculation, it's important we have the same definition of costs, counts, and latency
# across both model types.
class ProjectSessionCalculator:
    @staticmethod
    def calculate_costs(
            prompt_token_cost: Optional[Union[float, Decimal]],
            response_token_cost: Optional[Union[float, Decimal]]
    ) -> Optional[Decimal]:
        if prompt_token_cost and response_token_cost:
            return Decimal(prompt_token_cost) + Decimal(response_token_cost)
        else:
            return None

    @staticmethod
    def calculate_latency(start_time: Optional[datetime], end_time: Optional[datetime]) -> Optional[Decimal]:
        if end_time and start_time:
            return Decimal(str((end_time - start_time).total_seconds()))
        else:
            return None
