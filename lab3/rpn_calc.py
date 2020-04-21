

import sys
import math
import time
import pprint

sys.path.insert(0, "../..")

typenames = ("INT_T", "FLOAT_T", "STRING_T")
types=  ("INT", "FLOAT", "STRING", "BOOLEAN")
keywords = ('IF', 'WHILE', 'FOR', 'DEF', 'RUN') + ('AND', 'OR', 'NOR', 'NAND') + types

tokens = (
    'NAME', 'FUNCTION', 'RELOP', "BINOP"
) + keywords + typenames


def t_RELOP(t):
    r'!=|==|<=|>=|<|>'
    return t


def t_BINOP(t):
    r'-|\+|\*|/|\^'
    return t

literals = ['=', '(', ')', ';', '}', '{']

functions=['cos','sin','exp','sqrt','log', 'tan', 'ln', 'floor', 'toFloat', 'toInt', 'toString']

# Tokens


def t_STRING_T(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'

    if t.value in functions:
        t.type="FUNCTION"
    if t.value.upper() in keywords:
        t.type = t.value.upper()
    if t.value == "true":
        t.type = "BOOLEAN"
        t.value = True
    elif t.value == "false":
        t.type = "BOOLEAN"
        t.value = False

    return t

def t_FUNCTION(t):
    r'cos|sin|tan|exp|sqrt|log|ln|floor'

    return t


def t_FLOAT_T(t):

    r'\d*\.\d+|\d+\.'

    t.value = float(t.value)
    return t


def t_INT_T(t):

    r'\d+'

    t.value = int(t.value)


    return t

t_ignore = r"[ ]"

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
    ("left", "OR", "NOR"),
    ("left", "AND", "NAND"),
)


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
    """statement : boolean"""
    tokens[0] = ("PRINTLN", tokens[1])

def p_statement_fundef(tokens):
    """statement : DEF NAME '=' block"""
    tokens[0] = ("DEF", tokens[2], tokens[4])
def p_statement_run(tokens):
    """statement : RUN NAME"""
    tokens[0] = ("RUN", tokens[2])

def p_statement_cond(tokens):
    """statement : IF '(' boolean ')' block """
    relation = tokens[3]
    block = tokens[5]
    tokens[0] = ("IF", relation, block)

def p_statement_while(tokens):
    """statement : WHILE '(' boolean ')' block """
    relation = tokens[3]
    block = tokens[5]
    tokens[0] = ("WHILE", relation, block)
def p_statement_for(tokens):
    """statement : FOR '(' statement ';' boolean ';' statement ')' block """
    statement1 = tokens[3]
    relation = tokens[5]
    statement2 = tokens[7]
    block = tokens[9]
    tokens[0] = ("FOR", statement1, relation, statement2, block)

def p_boolean(tokens):
    """boolean : relation
               | BOOLEAN
               | boolean logicop boolean"""
    tokens[0] = tuple(["BOOLEAN"]) + tuple(tokens[1:])

def p_logicop(tokens):
    """logicop : AND 
               | OR
               | NAND
               | NOR"""
            
    tokens[0] = ("LOGICOP", tokens[1].upper())

def p_relation(tokens):
    """relation : expr RELOP expr"""
    tokens[0] = ("RELATION", tokens[1], tokens[2], tokens[3])

def p_typename(tokens):
    """typename : INT
                | FLOAT
                | STRING"""
    tokens[0] = tokens[1].upper()

def p_rvalue(tokens):
    """rvalue : expr
              | boolean
              | number"""
    tokens[0] = tokens[1]

def p_declaration(tokens):
    """statement : typename NAME '=' rvalue"""
    tokens[0] = ("DECLARATION", tokens[1], tokens[2], tokens[4])

def p_statement_assignment(tokens):
    """statement : NAME '=' rvalue"""
    name = tokens[1]
    value = tokens[3]
    tokens[0] = ("ASSIGNMENT", name, value)



def p_expr(tokens):
    """expr : name
            | number
            | string
            | name expr
            | number expr
            | string expr
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

def p_string(tokens):
    """string : STRING_T"""
    tokens[0] = ("STRING", str(tokens[1]))

def p_integer(tokens):
    """integer : INT_T"""
    tokens[0] = ("INT", tokens[1])

def p_float(tokens):
    """float : FLOAT_T"""
    tokens[0] = ("FLOAT", tokens[1])

def p_number(tokens):
    """number : float 
              | integer"""
    tokens[0] = tokens[1]

parser = yacc.yacc()
# s = input("> ")
# lexer.input(s)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)


def execute(statement):
   
    if statement[0] == "BLOCK":
        [execute(stmt) for stmt in statement[1]]    
    elif statement[0] == "DECLARATION":
        val = execute(statement[3]) 
        if val is not None:
            if statement[2] in variables.keys():
                raise(ValueError("variable already assigned"))
            else:

                if statement[1] != val[0]:
                    raise(ValueError("Cannot assign %s to %s" % (val[0], statement[1])))

                variables[statement[2]] = val 
                # print("assigned %s = %s" % (statement[2], val))
    elif statement[0] == "ASSIGNMENT":
        val = execute(statement[2]) 
        if val is not None:
            if statement[1] not in variables.keys():
                raise(ValueError("%s not declared" % (statement[1])))
            if val[0] != variables[statement[1]][0]:
                raise(ValueError("Cannot assign %s to %s" % (val[0],  variables[statement[1]][0])))


            variables[statement[1]] = val 
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
        print(execute(statement[1])[1])
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
    elif statement[0] == "BOOLEAN":
        if len(statement) == 2:
            if(statement[1] in [True, False]):
                return statement[1]
            return execute(statement[1])
        if statement[2][1] == "OR":
            return (execute(statement[1]) or execute(statement[3]))
        if statement[2][1] == "AND":
            return (execute(statement[1]) and execute(statement[3]))
        if statement[2][1] == "NOR":
            return not (execute(statement[1]) or execute(statement[3]))
        if statement[2][1] == "NAND":
            return not (execute(statement[1]) and execute(statement[3]))
    elif statement[0] in types:
        return statement
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
        # print(expr[0])
        if expr[0] in types:
            stack.append(expr)
            # print(stack)
        elif expr[0] == "NAME":
            try:
                type_, val = variables[expr[1]]
                if type_ in types:
                    stack.append((type_, val))
                elif type_ == "FUN":
                    print(f"'{expr[1]}' is a function, not variable")
                    return
                else:
                    print(f"Unknown type of '{expr[1]}'")
            except LookupError:
                print(f"Undefined variable:'{expr[1]}'")
                return
        elif expr[0] == "BINOP":
            type1, arg1 = stack.pop()
            type2, arg2 = stack.pop()

            if type1 != type2:
                raise(ValueError("%s does not match type with %s" % (type1, type2)))

            restype = None
            if expr[1] == "+":
                res = arg2 + arg1
            if expr[1] == "-":
                res = arg2 - arg1
            if expr[1] == "*":
                res = arg2 * arg1
            if expr[1] == "/":
                res = arg2 / arg1
                restype = "FLOAT"
            if expr[1] == "^":
                res = arg2 ** arg1
            if restype == None:
                restype = type1
            
            stack.append((restype, res))

        elif expr[0] == "SINOP":
            fn = None
            rettype = "FLOAT"
            if expr[1] == 'log':
                fn = lambda x: math.log(x, 10)
            elif expr[1] == 'ln':
                fn = math.log
            elif expr[1] == 'floor':
                fn = math.floor
                rettype = "INT"
            elif expr[1] == 'toFloat':
                fn = lambda x: float(x)
                rettype = "FLOAT"
            elif expr[1] == 'toInt':
                rettype = "INT"
                fn = lambda x: int(x)
            elif expr[1] == 'toString':
                rettype = "STRING"
                fn = lambda x: str(x)
            else:
                fn = getattr(math, expr[1])
            stack.append((rettype, fn(stack.pop()[1])))
        elif expr[0] == "EXPR":
            calc_expr(expr[1], stack)



if len(sys.argv) == 2:
        try:
            data = open(sys.argv[1]).read()
            program = yacc.parse(data)
            # pprint.pprint(program) # UNCOMMENT TO SEE AST
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
        # pprint.pprint(program) # UNCOMMENT TO SEE AST
        if program:
            execute(program)

