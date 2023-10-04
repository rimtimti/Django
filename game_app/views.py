import random
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

MIN_NUMBER = 0
MAX_NUMBER = 100
CUBE_MIN = 1
CUBE_MAX = 6


def eagle(request):
    game_list = ["орел", "решка"]
    response = random.choice(game_list)
    logger.info(f"Монета выпала стороной: {response}")
    return HttpResponse(response)


def cube(request):
    cube_value = random.randint(CUBE_MIN, CUBE_MAX)
    logger.info(f"Кубик выпал стороной: {cube_value}")
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    logger.info(f"Случайное число от {MIN_NUMBER} до {MAX_NUMBER}: {number}")
    return HttpResponse(number)
