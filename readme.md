# RePtiliaN - simple interpretable RPN language

RePtiliaN is a interpretable RPN language developed during the course of compilation theory at AGH UST. The newest version exists in `labX` catalouge with greatest X number.

## Overview
You can run `python reptilian.py` and type interactively:
```
> int a = 5;
> int b = 2;
> print b a ^ b -;
30
> for(int i = 1; i < 5; i = i 1 +){print i 2 ^;};
1
4
9
16
> 
```

Or type `python reptilian.py <file>`:

```
python reptilian.py factorial.scr
...
python reptilian.py primes.scr
...
```

### Strongly typed

```
> int a = 3;
> float b = 5.0;
> string c = "Ala ma kota";
> float d = 4 toFloat;
> print a;
3
> print b;
5.0
> print c;
Ala ma kota
> print d;
4.0
> a = 5;
> print a;
5
> a = 6.0;
Traceback (most recent call last):
  File ".\rpn_calc.py", line 442, in <module>
    execute(program)
  File ".\rpn_calc.py", line 257, in execute
    [execute(stmt) for stmt in statement[1]]
  File ".\rpn_calc.py", line 257, in <listcomp>
    [execute(stmt) for stmt in statement[1]]
  File ".\rpn_calc.py", line 276, in execute
    raise(ValueError("Cannot assign %s to %s" % (val[0],  variables[statement[1]][0])))
ValueError: Cannot assign FLOAT to INT
```

```
> int a = "Ala ma kota";
Traceback (most recent call last):
  File ".\rpn_calc.py", line 442, in <module>
    execute(program)
  File ".\rpn_calc.py", line 257, in execute
    [execute(stmt) for stmt in statement[1]]
  File ".\rpn_calc.py", line 257, in <listcomp>
    [execute(stmt) for stmt in statement[1]]
  File ".\rpn_calc.py", line 266, in execute
    raise(ValueError("Cannot assign %s to %s" % (val[0], statement[1])))
ValueError: Cannot assign STRING to INT
```

## Overloaded operators
```
> print "Ala " "ma" "Kota" + +;
Ala maKota
> print 2 3 +;
5
> print 2.0 3.0 +;
5.0
> print "Ala " "ma " + 2 3 ^ toString + " kotów" +;
Ala ma 8 kotów
>
```

## Scopes and shadowing
```
int a = 5;
print a;
{
    int b = 2;
    int a = 1000;
    print b;

    {
        print a;
    }
}
print a;
print b;
```
### Result:
```
\lab4> py .\reptilian.py .\locality_and_shadowing.scr
5
2
1000
5
Variable b not declared
```

## Function declaration
```
int g = 42;

def addTwo(int a, int b){
    a b +;
};

def addGlobal(int a){
    a g +;
};

print run addTwo(2, 2);
print run addGlobal(8);
```
### Result:
```
\lab4> py .\reptilian.py .\function.scr
4
50
```
## Examples

### Factorial

#### Code:

```
def factorial (int n) {
    string text = "!";
    int res = 1;
    if(n < 0){
        print "VALUE LESS THAN ZERO";
        res = 0;
    };
    for(int i = 1; i <= n; i = i 1 +){
        res = res i *;
    };
    print n toString text + " = " + res toString +;
};

for(int i = 3; i <= 6; i = i 1 +){
    run factorial(i);
};

```

As we see in line ` n toString text + " = " + res toString +;` the `+` operator is overloaded, but strongly typed.

#### Result
```
......\lab4> py .\reptilian.py .\factorial.scr
3! = 6
4! = 24
5! = 120
6! = 720
```

### Primes

#### Code:

```
def primes(int n){
    int i = 2;
    int isPrime = 1;
    while(i < n){
        if(n i / floor i * == n){
            isPrime = 0;
        };
        i = i 1 +;
    };
    isPrime;
};


def printPrimes (int n) {
    for(int i = 1; i < n; i = i 1 +){
        if(run primes(i) == 1){
            print i;
        };
    };
};

run printPrimes(100);

```
As we see we can use result of an function directly in if statement.

#### Result
```
......\lab4> py .\reptilian.py .\primes.scr
1
2
3
5
7
11
13
17
19
.
.
.
```

## AST of code:

To see AST of loaded program uncomment every line with `# UNCOMMENT TO SEE AST`
Here shown AST of factorial example

```
('PROGRAM',
 [('DEF',
   'factorial',
   ('BLOCK',
    ('PROGRAM',
     [('DECLARATION', 'STRING', 'text', ('EXPR', [('STRING', '!')])),
      ('PROGRAM',
       [('DECLARATION', 'INT', 'res', ('INT', 1)),
        ('PROGRAM',
         [('IF',
           ('BOOLEAN',
            ('RELATION', ('EXPR', [('NAME', 'n')]), '<', ('INT', 0))),
           ('BLOCK',
            ('PROGRAM',
             [('PRINTLN', ('EXPR', [('STRING', 'VALUE LESS THAN ZERO')])),
              ('PROGRAM', [('ASSIGNMENT', 'res', ('INT', 0))])]))),
          ('PROGRAM',
           [('FOR',
             ('DECLARATION', 'INT', 'i', ('INT', 1)),
             ('BOOLEAN',
              ('RELATION',
               ('EXPR', [('NAME', 'i')]),
               '<=',
               ('EXPR', [('NAME', 'n')]))),
             ('ASSIGNMENT',
              'i',
              ('EXPR',
               [('NAME', 'i'),
                ('EXPR', [('INT', 1), ('EXPR', [('BINOP', '+')])])])),
             ('BLOCK',
              ('PROGRAM',
               [('ASSIGNMENT',
                 'res',
                 ('EXPR',
                  [('NAME', 'res'),
                   ('EXPR', [('NAME', 'i'), ('EXPR', [('BINOP', '*')])])]))]))),
            ('PROGRAM',
             [('PRINTLN',
               ('EXPR',
                [('NAME', 'n'),
                 ('EXPR',
                  [('SINOP', 'toString'),
                   ('EXPR',
                    [('NAME', 'text'),
                     ('EXPR',
                      [('BINOP', '+'),
                       ('EXPR',
                        [('STRING', ' = '),
                         ('EXPR',
                          [('BINOP', '+'),
                           ('EXPR',
                            [('NAME', 'res'),
                             ('EXPR',
                              [('SINOP', 'toString'),
                               ('EXPR',
                                [('BINOP', '+')])])])])])])])])]))])])])])])),
   [('INT', 'n')]),
  ('PROGRAM',
   [('FOR',
     ('DECLARATION', 'INT', 'i', ('INT', 3)),
     ('BOOLEAN', ('RELATION', ('EXPR', [('NAME', 'i')]), '<=', ('INT', 6))),
     ('ASSIGNMENT',
      'i',
      ('EXPR',
       [('NAME', 'i'), ('EXPR', [('INT', 1), ('EXPR', [('BINOP', '+')])])])),
     ('BLOCK',
      ('PROGRAM', [('RUN', 'factorial', [('EXPR', [('NAME', 'i')])])])))])])
```