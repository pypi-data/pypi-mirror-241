from dataclasses import dataclass
from functools import partial
from requests import post, get
from typing import Optional, List, Callable

def variable_value_proposition_todict(variable_prop) -> dict:
    return {
        "id": variable_prop.id,
        "type": variable_prop.__class__.__name__,
        "value": float(variable_prop.value),
        "variables": list(
            map(
                lambda variable: variable.to_dict(),
                variable_prop.variables,
            )
        )
    }

def hash_variable_value_proposition(variable_prop) -> int:
    return hash(
        sum(
            map(
                hash,
                variable_prop.variables
            )
        ) + variable_prop.value + hash(variable_prop.id)
    )

def variable_proposition_todict(variable_prop) -> dict:
    return {
        "id": variable_prop.id,
        "type": variable_prop.__class__.__name__,
        "variables": list(
            map(
                lambda variable: variable.to_dict(),
                variable_prop.variables,
            )
        )
    }

def hash_variable_proposition(variable_prop) -> int:
    return hash(
        sum(
            map(
                hash,
                variable_prop.variables
            )
        ) + hash(variable_prop.id)
    )

@dataclass
class Variable:
    id: str

    def __hash__(self) -> int:
        return hash(self.id)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": "Variable",
        }

@dataclass
class Proposition:
    pass

@dataclass
class AtLeast(Proposition):
    value: int
    variables: List[Proposition]
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash_variable_value_proposition(self)

    def to_dict(self) -> dict:
        return variable_value_proposition_todict(self)

@dataclass
class AtMost(Proposition):
    value: int
    variables: List[Proposition]
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash_variable_value_proposition(self)

    def to_dict(self) -> dict:
        return variable_value_proposition_todict(self)

@dataclass
class And(Proposition):
    variables: List[Proposition]
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash_variable_proposition(self)

    def to_dict(self) -> dict:
        return variable_proposition_todict(self)

@dataclass
class Or(Proposition):
    variables: List[Proposition]
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash_variable_proposition(self)

    def to_dict(self) -> dict:
        return variable_proposition_todict(self)

@dataclass
class Xor(Proposition):
    variables: List[Proposition]
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash_variable_proposition(self)

    def to_dict(self) -> dict:
        return variable_proposition_todict(self)

@dataclass
class XNor(Proposition):
    variables: List[Proposition]
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash_variable_proposition(self)

    def to_dict(self) -> dict:
        return variable_proposition_todict(self)

@dataclass
class Implies(Proposition):
    left:   Proposition
    right:  Proposition
    id: Optional[str] = None

    def __hash__(self) -> int:
        return hash(
            sum([
                hash(self.left),
                hash(self.right),
                hash(self.id),
            ])
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.__class__.__name__,
            "left": self.left.to_dict(),
            "right": self.right.to_dict(),
        }

@dataclass
class Evaluation:
    data: Optional[List[List[str]]]
    error:  Optional[str]
    
class evaluation_composer:

    def __init__(self, backend_url: str):
        assert evaluation_composer.__check_health__(backend_url), f"Backend {backend_url} is not up/healthy"
        self.backend_url = backend_url
    
    @staticmethod
    def __check_health__(backend_url: str): 
        return get(
            f"{backend_url}/health",
        ).status_code == 200

    def __call__(self, propositions: List[Proposition], interpretations: List[dict]) -> Callable[[List[Proposition], dict], Evaluation]:
        try:
            response = post(
                f"{self.backend_url}/evaluate",
                json={
                    "evaluables": list(
                        map(
                            lambda p: p.to_dict(),
                            propositions,
                        )
                    ),
                    "interpretations": interpretations,
                }
            )
            if response.status_code == 200:
                return Evaluation(
                    data=response.json(),
                    error=None,
                )
            else:
                return Evaluation(
                    data=None,
                    error=response.text,
                )
        except Exception as e:
            return Evaluation(
                data=None,
                error=str(e),
            )