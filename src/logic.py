class Formula:
    """ Goal == Formula """

    def __repr__(self) -> str:
        del self
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        return str(self) == str(other)


class Var(Formula):
    def __init__(self, str):
        self.str = str

    def __repr__(self):
        return self.str


class Or(Formula):
    def __init__(self, left_formula, right_formula) -> None:
        self.left_formula = left_formula
        self.right_formula = right_formula

    def __repr__(self) -> str:
        return f"({self.left_formula} | {self.right_formula})"


class Implies(Formula):
    def __init__(self, left_formula, right_formula) -> None:
        self.left_formula = left_formula
        self.right_formula = right_formula

    def __repr__(self) -> str:
        return f"({self.left_formula} => {self.right_formula})"


class And(Formula):
    def __init__(self, left_formula, right_formula) -> None:
        self.left_formula = left_formula
        self.right_formula = right_formula

    def __repr__(self) -> str:
        return f"({self.left_formula} & {self.right_formula})"


class Forall(Formula):
    def __init__(self, variable, inner_formula) -> None:
        self.variable = variable
        self.inner_formula = inner_formula

    def __repr__(self) -> str:
        return f"(Forall {self.variable}. ({self.inner_formula}))"


class Exists(Formula):
    def __init__(self, variable, inner_formula) -> None:
        self.variable = variable
        self.inner_formula = inner_formula

    def __repr__(self) -> str:
        return f"(Exists {self.variable}. ({self.inner_formula}))"


def substitute(old_variable: str, new_variable: str, formula: Formula):
    # TODO this does nothing for now
    return formula
