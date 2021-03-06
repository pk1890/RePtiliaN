

import sys
import math
import time

sys.path.insert(0, "../..")

keywords = ('IF', 'WHILE', 'FOR', 'DEF', 'RUN')

tokens = (
    'NAME', 'INTEGER', 'DOUBLE', 'FUNCTION', 'RELOP', "BINOP"
) + keywords


def t_RELOP(t):
    r'!=|==|<=|>=|<|>'
    return t


def t_BINOP(t):
    r'-|\+|\*|/|\^'
    return t

literals = ['=', '(', ')', ';', '}', '{']

functions=['cos','sin','exp','sqrt','log', 'tan', 'ln', 'floor']

# Tokens

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'

    if t.value in functions:
        t.type="FUNCTION"
    if t.value.upper() in keywords:
        t.type = t.value.upper()

    return t

def t_FUNCTION(t):
    r'cos|sin|tan|exp|sqrt|log|ln|floor'

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

variables = {}

def p_block(tokens):
    """block : '{' program '}'
             | statement 
       program : statement ';' program
               | statement ';'"""

    stmts = []
    for token in tokens[1:]:
        if token in ('{', '}', ';'):
            continue
        stmts.append(token)
    tokens[0] = ("BLOCK", stmts)


def p_statement_expr(tokens):
    """statement : expr"""
    tokens[0] = ("PRINTLN", tokens[1])

def p_statement_relation(tokens):
    """statement : relation"""
    tokens[0] = ("PRINTLN", tokens[1])

def p_statement_fundef(tokens):
    """statement : DEF NAME '=' block"""
    tokens[0] = ("DEF", tokens[2], tokens[4])
def p_statement_run(tokens):
    """statement : RUN NAME"""
    tokens[0] = ("RUN", tokens[2])

def p_statement_cond(tokens):
    """statement : IF '(' relation ')' block """
    relation = tokens[3]
    block = tokens[5]
    tokens[0] = ("IF", relation, block)

def p_statement_while(tokens):
    """statement : WHILE '(' relation ')' block """
    relation = tokens[3]
    block = tokens[5]
    tokens[0] = ("WHILE", relation, block)
def p_statement_for(tokens):
    """statement : FOR '(' statement ';' relation ';' statement ')' block """
    statement1 = tokens[3]
    relation = tokens[5]
    statement2 = tokens[7]
    block = tokens[9]
    tokens[0] = ("FOR", statement1, relation, statement2, block)

def p_relation(tokens):
    """relation : expr RELOP expr"""
    tokens[0] = ("RELATION", tokens[1], tokens[2], tokens[3])

def p_statement_assignment(tokens):
    """statement : NAME '=' expr"""
    name = tokens[1]
    value = tokens[3]
    tokens[0] = ("ASSIGNMENT", name, value)

def p_expr(tokens):
    """expr : name
            | number
            | name expr
            | number expr
            | sinop expr
            | binop expr
            | sinop 
            | binop """

    elems = tokens[1:]
    tokens[0] = ("EXPR", elems)


def p_sinop(tokens):
    """sinop : FUNCTION"""
    tokens[0] = ("SINOP", tokens[1])

def p_binop(tokens):
    """binop : BINOP"""
    tokens[0] = ("BINOP", tokens[1])

def p_var(tokens):
    "name : NAME"
    tokens[0] = ("NAME", tokens[1])

def p_number(tokens):
    """number : INTEGER
            | DOUBLE"""
    tokens[0] = ("NUMBER", tokens[1])


parser = yacc.yacc()
# s = input("> ")
# lexer.input(s)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)


def execute(statement):
    # print(statement)
    if statement[0] == "BLOCK":
        [execute(stmt) for stmt in statement[1]]
    elif statement[0] == "ASSIGNMENT":
        val = execute(statement[2]) 
        if val is not None:
            variables[statement[1]] = ("VAR", val) 
    elif statement[0] == "DEF":
        val = statement[2] 
        if val is not None:
            variables[statement[1]] = ("FUN", ("BLOCK", val)) 
    elif statement[0] == "RUN":
            try:
                type_, val = variables[statement[1]]
                if type_ == "FUN":
                    execute(val[1])
                elif type_ == "VAR":
                    print(f"'{statement[1]}' is a variable, not a function")
                    return
                else:
                    print(f"Unknown type of '{statement[1]}'")
            except LookupError:
                print(f"Undefined function:'{statement[1]}'")
                return

    elif statement[0] == "PRINTLN":
        print(execute(statement[1]))
    elif statement[0] == "IF":
        if execute(statement[1]):
            execute(statement[2])
    elif statement[0] == "WHILE":
        while execute(statement[1]):
            execute(statement[2])
    elif statement[0] == "FOR":
        execute(statement[1])
        while execute(statement[2]):
            execute(statement[4])
            execute(statement[3])
    elif statement[0] == "RELATION":
        if statement[2] == "==":
            return (execute(statement[1]) == execute(statement[3]))
        if statement[2] == "<":
            return (execute(statement[1]) < execute(statement[3]))
        if statement[2] == ">":
            return (execute(statement[1]) > execute(statement[3]))
        if statement[2] == "<=":
            return (execute(statement[1]) <= execute(statement[3]))
        if statement[2] == ">=":
            return (execute(statement[1]) >= execute(statement[3]))
        if statement[2] == "!=":
            return (execute(statement[1]) != execute(statement[3]))
    elif statement[0] == "EXPR":
        stack = []
        calc_expr(statement[1], stack)
        if len(stack) == 1:
            r = stack.pop()
            # print("Poping" )
            # print(r)
            return r
        else:
            print(f"Invalid stack state: {stack}")


def calc_expr(expression, stack):
    # print(stack)
    for expr in expression:
        # print(expr)
        if expr[0] == "NUMBER":
            stack.append(expr[1])
        elif expr[0] == "NAME":
            try:
                type_, val = variables[expr[1]]
                if type_ == "VAR":
                    stack.append(val)
                elif type_ == "FUN":
                    print(f"'{expr[1]}' is a function, not variable")
                    return
                else:
                    print(f"Unknown type of '{expr[1]}'")
            except LookupError:
                print(f"Undefined variable:'{expr[1]}'")
                return
        elif expr[0] == "BINOP":
            arg1 = stack.pop()
            arg2 = stack.pop()
            if expr[1] == "+":
                res = arg2 + arg1
            if expr[1] == "-":
                res = arg2 - arg1
            if expr[1] == "*":
                res = arg2 * arg1
            if expr[1] == "/":
                res = arg2 / arg1
            if expr[1] == "^":
                res = arg2 ** arg1
            stack.append(res)
        elif expr[0] == "SINOP":
            fn = None
            if expr[1] == 'log':
                fn = lambda x: math.log(x, 10)
            elif expr[1] == 'ln':
                fn = math.log
            else:
                fn = getattr(math, expr[1])
            stack.append(fn(stack.pop()))
        elif expr[0] == "EXPR":
            calc_expr(expr[1], stack)



if len(sys.argv) == 2:
        try:
            data = open(sys.argv[1]).read()
            program = yacc.parse(data)
            if program:
                execute(program)
        except FileNotFoundError:
            print(f"Unable to open file '{sys.argv[1]}'")
else:
    while True:
        try:
            s = input("> ")
        except (KeyboardInterrupt, EOFError):
            break
        if not s:
            continue
        program = yacc.parse(s)
        if program:
            execute(program)

