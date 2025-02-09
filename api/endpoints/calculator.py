from fastapi import APIRouter

from services.calculator_service import CalculatorService

calculator_service = CalculatorService()

calculator_router = APIRouter(prefix='/calculator')
calculator_router.tags = ["Calculator"]


@calculator_router.post('/easy/', response_model=float)
async def process_easy_func(a: float, op: str, b: float):
    result = await calculator_service.calculate(param_1=a, param_2=b, operator=op)
    return result


@calculator_router.post('/hard/', response_model=float)
async def process_hard_func(math_expression: str):
    result = await calculator_service.calculate_complex_expression(expression=math_expression)
    return result
