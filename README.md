# prover
By Harry Sha and Tyler Yep

# TODO
- Write out a sample proof for:
    - Non-mathy proof
    - Support for contradiction
    - Support for induction

# Proof writing section interface
All assumptions
Goal:
- Close to natural proof language in English
- Easy mode vs advanced mode
- Suggestions
    - "try induction! try arbitrary!"
- Auto solve in the background
- Should be able to prove everything in CS103

# Plan
- Backend first (all the proof logic) 
    - Logic
        - How are we going to model FOL statements and proofs? 
        - Proof checker (is this proof a valid proof for this statement)
    - Get simple 103 proofs like "Forall n is even => n^2 is even"
    - Should be able to print out first order logic formulas

# Logic

`Variable` and `Formula` are both classes

Formulas:
S T -> 
- for_all(n, S)
- exists(n, S)
- and(S, T)
    - maybe this: S and T


Theorem: "Forall n is even => n^2 is even"
n = Var()
for_all(
    n, 
    implies(
        even(n), even(square(n))
    ),
)

First proof: (103)

Pick arbitrary n. Assume n is even, we'll show that n^2 is even. 
As $n$ is even, there is some $k$ such that $$n = 2k$$. Then $n^2 = 4k^2 = 2(2k^2)$. 
Therefore there is some natural number $s$ namely (2k^2) such that $n^2 = 2s$ 
Thus $n^2$ is even.

Take 2: (lean)
It suffices to show that for an arbitrary n, if n is even, n^2 is even
Pick arbitrary n
It suffices to show that n is even implies n^2 is even. 
Assume n is even
It suffices to show n^2 is even 
If suffices to show exists k where n^2 = 2k
Because n is even, we have j = 2n
Pick k = (2j^2).

We found k so we're done!!



Take 3 (lean version)
Goal: prove for an arbitrary n, if n is even, n^2 is even
    Pick arbitrary n
Goal: prove n is even implies n^2 is even. 
    Assume n is even
Goal: prove n^2 is even 
Goal: prove exists k where n^2 = 2k
    Let j be such that n = 2j, (because n is even we know j exists)
    Pick k = 2j^2
Goal: show n^2 = 2k
    Simplifier:
        n = 2j
        n^2 = (2j)^2
        n^2 = 4j^2
        n^2 = 2 (2j^2)
        n^2 = 2k


Take 4: (more-student-oriented)

## Working interactive proof 

```
Goal: prove for an arbitrary n, if n is even, n^2 is even
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
        = 2(2j^2)
    Pick k = 2j^2
```






```python
import arithmetic
import set_theory 


def interactive_prover(theorem):
    context = {} # n: int, arbitrary, even
    goals = [Formulae()]

    while not goals: # or empty
        print(f"Goal: prove {goal}")
        stuff = parse(input())
        context += stuff
        for goal in goals:
            goal.try_step()

```


## Sample AND proof
```
Goal: prove for an arbitrary n, if n is even, n^2 is even
    Pick arbitrary integer n
Goal: prove n is even AND n^2 is even. 
    Split on and:
    Goal: prove n is even
        sorry

    Goal: prove n^2 is even
        sorry
```







```python
def check_proof(proof, theorem, context={}):
    pass
```






Equality by... substitute, by_transitivity, etc
Finite number of possible actions (PickArbitrary, Assume, Have?, UseDefinition)


- Use Wolfram Alpha or some related package to ensure the rearranging step is true
- Goals are automatically added as the student types (or hard mode, we leave the student to write the new goal as well), and are included in the final output.
- Save to Pdf outputs the english 


Very verbose proof language
Parsed into structure


Equals(x, x)
```python
# def equals

def evaluate(S):
    pass


def is_even(n): 
    return exists(k, equals(2-k, n))


def proof(thm, assumptions):
    n = PickArbitraryNum()
    n_is_even = Assume(even, n) # exists(k, equals(n, 2-k))
    k, f = get_example_from_existential(n_is_even) # f = equals(n, 2-k)
    f = apply_to_both_sides(square, f) # equals(n^2, (2k)^2)
    g = rewrite(f) # g = equals(n^2, 2(2-k^2))
    h = existential_introduction('a', 2-k^2, g) #h = exists(a, equals(n^2, a))
    i = implies_intro(n_is_even, h)
    forall_intro("n", i)

    if we can get to exists(k, even(square(n)))
    
    can_be_written_as_even(k-2)

pick arbitrary n
assume even(n)
    math
    conclude n^2 is even
    
    even(n) => even(n^2)  # implication introduction

forall n (even(n) => even(n^2)) # forall intro





n = Var(arbitrary=True, even=True)
# Bad - Might be too verbose + want to use even outside of this var
```
```python
class Var:
    def __init__(**kwargs):
        if "even" in kwargs:
            pass

```



for_all(lambda n: even(n) == even(n-2))
function == implication :)

