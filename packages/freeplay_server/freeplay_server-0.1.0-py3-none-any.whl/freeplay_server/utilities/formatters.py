from _decimal import Decimal

MIN_DISPLAYABLE_COST_IN_DOLLARS = '0.00001'
# Render to 5 decimal points
COST_QUANTIZATION_FACTOR = Decimal('0.00001')

# How many decimal points after "." to render for latency values
LATENCY_QUANTIZATION_FACTOR = Decimal('0.01')


def format_decimal_dollars(decimal_value: Decimal) -> str:
    if decimal_value < Decimal(MIN_DISPLAYABLE_COST_IN_DOLLARS):
        return f'< ${MIN_DISPLAYABLE_COST_IN_DOLLARS}'
    else:
        rounded_decimal = decimal_value.quantize(COST_QUANTIZATION_FACTOR)
        return f"${rounded_decimal}"


def format_latency(decimal_latency: Decimal) -> str:
    rounded_decimal = decimal_latency.quantize(LATENCY_QUANTIZATION_FACTOR)
    return f"{rounded_decimal}s"
