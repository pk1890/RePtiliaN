

import sys
import math

sys.path.insert(0, "../..")

tokens = (
    'NAME', 'INTEGER', 'DOUBLE', 'FUNCTION', 'POWER', 'RELOP'
)

t_POWER = r'\*\*'

def t_RELOP(t):
    r'<|>|!=|==|<=|>='
    return t

literals = ['=', '+', '-', '*', '/', '(', ')', ';']

functions=['cos','sin','exp','sqrt','log']

# Tokens

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'

    if t.value in functions:

        t.type="FUNCTION"

    return t

def t_FUNCTION(t):
    r'cos|sin|tan|exp|sqrt|log|ln'
    fn = None
    if t.value == 'log':
        fn = lambda x: math.log(x, 10)
    elif t.value == 'ln':
        fn = math.log
    else:
        fn = getattr(math, t.value)
    t.value = (t.value, fn)

    return t


def t_DOUBLE(t):

    r'\d*\.\d+|\d+\.'

    t.value = float(t.value)

    return t



def t_INTEGER(t):

    r'\d+'

    t.value = int(t.value)

    return t

t_ignore = r"[ \t]"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):

    print("Illegal character '%s'" % t.value[0])

    t.lexer.skip(1)

# Build the lexer

import ply.lex as lex

lexer = lex.lex()

import ply.yacc as yacc


precedence = (
    ("left", "+", "-"),
    ("left", "*", "/"),
    ("right", "POWER"),
    ("right", "MINUS"),
    ("right", "FUNCTION"),
)

variables = {}

def p_expressions(tokens):
    """expressions : expression 
                    | expression ';' expressions
                    | expression ';'"""
    pass
def p_expression_assignment(tokens):
    """expression : NAME '=' expr"""
    variables[tokens[1]] = tokens[3]
def p_expression_relop(tokens):
    """expression : expr RELOP expr"""
    if tokens[2] == "==":
        print(tokens[1] == tokens[3])
    elif tokens[2] == "<":
        print(tokens[1] < tokens[3])
    elif tokens[2] == ">":
        print(tokens[1] > tokens[3])
    elif tokens[2] == "<=":
        print(tokens[1] <= tokens[3])
    elif tokens[2] == ">=":
        print(tokens[1] >= tokens[3])
    elif tokens[2] == "!=":
        print(tokens[1] != tokens[3])
def p_expression_expr(tokens):
    """expression : expr"""
    print(tokens[1])
def p_function(tokens):
    """expr : FUNCTION expr"""
    tokens[0] = tokens[1][1](tokens[2])
def p_add(tokens):
    """expr : expr '+' expr"""
    tokens[0] = tokens[1] + tokens[3]
def p_sub(tokens):
    """expr : expr '-' expr"""
    tokens[0] = tokens[1] - tokens[3]
def p_mul(tokens):
    """expr : expr '*' expr"""
    tokens[0] = tokens[1] * tokens[3]
def p_div(tokens):
    """expr : expr '/' expr"""
    tokens[0] = tokens[1] / tokens[3]
def p_pow(tokens):
    """expr : expr POWER expr"""
    tokens[0] = tokens[1] ** tokens[3]
def p_parenthesis(tokens):
    """expr : '(' expr ')'"""
    tokens[0] = tokens[2]
def p_minus(tokens):
    """expr : '-' expr %prec MINUS"""
    tokens[0] = -tokens[2]
def p_expr_number(tokens):
    """expr : number"""
    tokens[0] = tokens[1] 
def p_number(tokens):
    """number : INTEGER 
              | DOUBLE"""
    tokens[0] = tokens[1]
def p_var(tokens):
    "expr : NAME"
    try:
        tokens[0] = variables[tokens[1]]
    except LookupError:
        print("Undefined variable '%s'" % tokens[1])
        tokens[0] = 0



parser = yacc.yacc()

while True:
    try:
        s = input("> ")
    except (KeyboardInterrupt, EOFError):
        break
    if not s:
        continue
    yacc.parse(s)


# def test(a):

#     lexer.input(a)

#     while True:
#         tok = lexer.token()
#         if not tok: 
#             break      # No more input
#         print(tok)

# # test("sin")

# # test("sinus")

# # test("1sin")

# test("ssss4 +2 **6=")