# Puan PV SDK Python
An SDK for connecting to a Puan PV backend.

# Example
```python
from puan_pv_sdk_python import PropKey, And, Or, Variable, evaluation_composer

evaluate = evaluation_composer("http://localhost:8080")

keys = evaluate(
    propositions=[
        And(
            variables=[
                Or(
                    variables=[
                        Variable(id='a'),
                        Variable(id='b')
                    ]
                ),
                Variable(id='c')
            ]
        ),
        And(
            variables=[
                Variable(id='a'),
                Variable(id='b')
            ]
        ),
    ], 
    interpretations=[
        {"a": 1, "b": 1, "c": 1},
        {"a": 1, "b": 1, "c": 0},
        {"a": 1, "b": 0, "c": 1},
    ],
).data
```