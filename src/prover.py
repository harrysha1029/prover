"""
Goal: prove for all n, if n is even, n^2 is even
    Pick arbitrary integer n
Goal: prove n is even implies n^2 is even.
    Assume n is even
Goal: prove n^2 is even
    Use definition of even number
Goal: prove exists k where n^2 = 2k
    Let j be such that n = 2j, (because n is even we know j exists)
    Have n^2
        = (2j)^2
        = 4j^2
        = 2(2j^2)mypy
    Pick k = 2j^2
"""
from typing import List

from src.logic import Exists, Forall, Formula, Implies
from src.proof import assume_antecedent, pick_arbitrary, split_on_and


def Equals(a, b):
    return True


def IsEven(n):
    return Exists("k", Equals("n^2", "2k"))


# Squared("n"))
# SQUARED_EVEN = Formula("for an arbitrary n, if n is even, n^2 is even")
SQUARED_EVEN = Forall("n", Implies(IsEven("n"), IsEven("n^2")))


def try_step(goal: Formula, student_input) -> List[Formula]:
    if student_input == "and":
        # cast(And, goal)
        return split_on_and(goal, [])

    if student_input == "forall":
        # cast(And, goal)
        return pick_arbitrary(goal, "n", [])
    return []


def prover(theorem=SQUARED_EVEN) -> None:
    # context = {}  # n: int, arbitrary, even
    # goals = [Formulae()]
    goals = [theorem]
    while goals:
        for goal in goals:
            print(f"Goal: prove {goal}")
        student_input = input(">> ")
        # context += understand(parse(input()))
        new_goals = []
        for goal in goals:
            new_goals += try_step(goal, student_input)
        goals = new_goals

    print("We did it!")
