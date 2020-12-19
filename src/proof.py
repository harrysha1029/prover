from typing import List

from src.logic import And, Forall, Formula, Implies, substitute

# ======= Proof Steps =====================
# These all need to return a list of new goals


def split_on_and(goal: And, context) -> List[Formula]:
    """
    Student enters "split AND statement",
    we return two new goals as a try_step sorta thing
    """
    # assert isinstance(goal, And)
    return [goal.left_formula, goal.right_formula]


def assume_antecedent(goal: Implies, context):
    # TODO somehow the antecendent needs to be added to a context.
    context.append(goal.left_formula)
    return [goal.right_formula]


def pick_arbitrary(goal: Forall, variable: str, context):
    return [substitute(goal.variable, variable, goal.inner_formula)]


# def show_exists(goal: Forall, variable: str, context):
#     return [substitute(goal.variable, variable, goal.inner_formula)]
