from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, List, Literal, Tuple

from src.logic import And, Formula, Implies, Or, Var

InferenceRule = Callable[[List[Formula]], List[Formula]]


def AndIntro(formulas: List[Formula]) -> List[Formula]:
    assert len(formulas) == 2
    return [And(*formulas)]


def AndElim(formulas: List[Formula]) -> List[Formula]:
    assert len(formulas) == 1
    return [formulas[0].left_formula, formulas[0].right_formula]


def Assume(formulas: List[Formula]) -> List[Formula]:
    assert len(formulas) == 1
    return [formulas[0]]


def ImpliesIntro(formulas: List[Formula]) -> List[Formula]:
    assert len(formulas) == 2
    return [Implies(*formulas)]


def ImpliesElim(formulas: List[Formula]) -> List[Formula]:
    assert len(formulas) == 2
    if formulas[0] == formulas[1].left_formula:
        return [formulas[1].right_formula]

    raise Exception("modus not ponens :(")


@dataclass
class FitchLine:
    formula: List[Formula]
    rule: InferenceRule
    lines_applied_to: List[int]
    indent_level: int


@dataclass
class FitchProof:
    theorem: Formula
    lines: List[FitchLine]


def check_fitch_proof(proof: FitchProof) -> bool:
    stack = []  # Contain (level, line_number)
    curr_level = 0
    for line_number, line in enumerate(proof.lines):
        active_lines = [l for _, l in stack]
        if not all(used_line in active_lines for used_line in line.lines_applied_to):
            print(
                "Tried to use a line from the future or a line \
                 from an incorrect indent level"
            )
            return False

        if line.rule == Assume:
            used_formulas = [line.formula]
            curr_level += 1
            if (
                line_number > 0
                and line.indent_level != 1 + proof.lines[line_number - 1].indent_level
            ):
                return False

        elif line.rule == ImpliesIntro:
            this_assumption_level_stack = [(x, y) for x, y in stack if x == curr_level]
            used_formulas = [
                proof.lines[this_assumption_level_stack[0][1]].formula,
                proof.lines[line.lines_applied_to[0]].formula,
            ]
            curr_level -= 1
            stack = [(x, y) for x, y in stack if x <= curr_level]
            if line.indent_level != proof.lines[line_number - 1].indent_level - 1:
                return False

        else:
            used_formulas = [proof.lines[i].formula for i in line.lines_applied_to]

        if line.formula not in line.rule(used_formulas):

            print(line.rule)
            print((line.formula), (line.rule(used_formulas)))
            print("Invalid application of rule")
            return False

        stack.append((curr_level, line_number))

    return (
        proof.lines[-1].formula == proof.theorem and proof.lines[-1].indent_level == 0
    )


def main():
    THEOREM_1 = Implies(And(Var("a"), Var("b")), And("a", "b"))
    proof = [
        FitchLine(And(Var("a"), Var("b")), Assume, [], 1),
        FitchLine(Var("a"), AndElim, [0], 1),
        FitchLine(Var("b"), AndElim, [0], 1),
        FitchLine(And(Var("a"), Var("b")), AndIntro, [1, 2], 1),
        FitchLine(THEOREM_1, ImpliesIntro, [3], 0),
    ]

    THEOREM_2 = Implies(And(Implies(Var("a"), Var("b")), Var("a")), Var("b"))
    proof2 = [
        FitchLine(And(Implies(Var("a"), Var("b")), Var("a")), Assume, [], 1),
        FitchLine(Var("a"), AndElim, [0], 1),
        FitchLine(Implies(Var("a"), Var("b")), AndElim, [0], 1),
        FitchLine(Var("b"), ImpliesElim, [1, 2], 1),
        FitchLine(THEOREM_2, ImpliesIntro, [3], 0),
    ]
    # print(THEOREM_2)
    print(check_fitch_proof(FitchProof(THEOREM_1, proof)))
    print(check_fitch_proof(FitchProof(THEOREM_2, proof2)))
