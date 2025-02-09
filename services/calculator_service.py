from fastapi.exceptions import HTTPException

from sympy import parse_expr
from sympy.core.numbers import zoo, Float


class CalculatorService:
    @staticmethod
    async def calculate(param_1: float, param_2: float, operator: str) -> float:
        match operator:
            case '+':
                return param_1 + param_2
            case '-':
                return param_1 - param_2
            case '*':
                return param_1 * param_2
            case '/':
                if param_2 == 0:
                    raise HTTPException(status_code=400, detail="Division is not possible")
                return param_1 / param_2
            case _:
                raise HTTPException(status_code=400, detail="Incorrect operator")

    @staticmethod
    async def calculate_complex_expression(expression: str) -> float:
        parsed_expr = parse_expr(expression)
        if parsed_expr == zoo:
            raise HTTPException(status_code=400, detail="Division by zero is not possible")

        result = parsed_expr.evalf()
        if type(result) is not Float:
            raise HTTPException(status_code=400, detail="The expression must contain only numbers")

        return float(result)
