# Basic calculator

This is a calculator project for basic math functions.<br />
Implemented methods:<br />
* addition
* subtraction
* multiplication
* division
* n'th root
* reset memory

# Installation

```
pip install basic-math-calculator

from basic_math_calculator.calculator import Calculator
```


# Usage

Result is stored and overwritten in memory until reset() method is ran.

Calculation methods can take either one or two arguments (in addition to self).<br />
If only one arguments is given calculations will be performed with memory value (latest result), otherwise calculations will be performed between two arguments and memory value will be overwritten.

For example:

	>>> calc = Calculator()
	>>> calc.addition(4, 5)
	9
	>>> calc.addition(10)
	19
	>>> calc.multiplication(2)
	38
	>>> calc.multiplication(2, 5)
	10
	>>> calc.reset()
	0

# TestCase
```
python -m unittest test_calculator.py
```

# License

This project is licensed under the terms of the **MIT** [license](https://choosealicense.com/licenses/mit/)
