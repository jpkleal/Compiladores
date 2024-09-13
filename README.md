# Final Project For UFABC Compilers Discipline

This repo contains the final project for the compilers discipline by João Pedro Kayano Leal.
The project description can be found [here](Projeto.pdf) and the functional requirements [here](Checklist.pdf).

## About The Language

The language can be compiled to python 3 and c. 

### General Format

Declaration bloc, followed by variables to be used, and a commands' bloc.

```
programa

    declare a,b,c,d.

    bloc

fimprog.
```

### Functions:

| Function                                       |                         Parameters                         |                                                                Description |
|------------------------------------------------|:----------------------------------------------------------:|---------------------------------------------------------------------------:|
| escreva(foo).                                  |                     foo -> Expression                      |                                      print the value of a given expression |
| leia(foo:bar).                                 |              foo -> Variable<br/>bar -> Type               |           read a value for a variable, can receive a type for the variable |
| foo := bar                                     |           foo -> Variable<br/>bar -> Expression            |                                        assign an expression for a variable |
| se (foo)<br/>entao bloc1<br/>senao bloc2 fimse | foo -> Expression<br/> bloc1 and bloc2 -> Command sequence | if conditional, depending on the expression executes either bloc1 or bloc2 |
| equanto (foo)<br/>faca bloc<br/>fimfaca        |      foo -> Expression<br/> bloc -> Command sequence       |                          while conditional, executes bloc while expression |
| faca bloc<br/>fimfaca<br/>equanto (foo)        |      foo -> Expression<br/> bloc -> Command sequence       |     do-while conditional, executes a bloc, at least once, while expression |

### Variables

Variables can be named anything starting with a letter and followed by other letters or numbers.

During compilation the compiler will assign and type for each variable, check if they are being declared and not used, 
check if they are being used without an initial value and if they are being declared more than once. 
When reading a variable from user input the programmer can define a type for the variable if the compiler can't assign one based on previous operations.

Types:
- Numerical (NUM)
- Text (TEXTO)
- Boolean (BOOL)

### Expressions

Expression are sequences of values (vars, texts, nums or booleans) and operations (arithmetical, relational or logical).
During compilation, it will check if operations are valid (e.g. you can't multiply two texts or sum a num to a text).
It will also evaluate the expression as good as it can.


## Building and Executing

### Building the grammar
The project is made using the antlr tool and can be built using
```shell 
java -jar antlr-4.13.2-complete.jar IsiLanguage.g4 -o core -package core
```
By default, this repo stores the grammar already built

### Run
The project is made using python 3.10.12.
All libraries need can be installed thru pip using 
```shell
pip install -r requirements.txt
```

The compiler alone can be executed in the [compiler.py](compiler.py) file.
Or in the rest api powered by flask on [main.py](main.py)