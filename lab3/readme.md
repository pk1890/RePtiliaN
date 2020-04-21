# Calculator and simple rpn language
## Calculator
run `python calc.py`, and type your calculation:
```
> a = 3; b = 5; (2**a + 3*5+sin(b))
22.04107572533686
> sin(a)**2 + cos(a)**2
0.9999999999999999
> 
```

## Simple rpn language

You can run `python rpn_calc.py` and type interactively:
```
> int a = 5
> int b = 2
> b a ^ b -
30
> for(int i = 1; i < 5; i = i 1 +){i 2 ^;}
1
4
9
16
> 
```

Or type `python rpn_calc.py <file>`:

```
python rpn_calc.py factorial.scr
...
python rpn_calc.py primes.scr
...
```

## Example: factorial

### Code:

```
{
    int n = 0;
    int i = 0;
    int res = 0;

    string text = "!";

    def factorial = {
        if(n < 0){
            -1;
        };
        res = 1;
        for(i = 1; i <= n; i = i 1 +){
            res = res i *;
        };
        n toString text + " = " + res toString +;
    };
    
    n = 5;
    run factorial;

    n = 10;
    run factorial;
}
```

As we see in line ` n toString text + " = " + res toString +;` the `+` operator is overloaded, but strongly typed.

### Result
```
....\lab3> py .\rpn_calc.py .\factorial.scr
5! = 120
10! = 3628800
```

### AST of code:

To see AST of loaded program uncomment every line with `# UNCOMMENT TO SEE AST`

```
('BLOCK',
 [('BLOCK',
   [('DECLARATION', 'INT', 'n', ('INT', 0)),
    ('BLOCK',
     [('DECLARATION', 'INT', 'i', ('INT', 0)),
      ('BLOCK',
       [('DECLARATION', 'INT', 'res', ('INT', 0)),
        ('BLOCK',
         [('DECLARATION', 'STRING', 'text', ('EXPR', [('STRING', '!')])),
          ('BLOCK',
           [('DEF',
             'factorial',
             ('BLOCK',
              [('BLOCK',
                [('IF',
                  ('BOOLEAN',
                   ('RELATION',
                    ('EXPR', [('NAME', 'n')]),
                    '<',
                    ('EXPR', [('INT', 0)]))),
                  ('BLOCK',
                   [('BLOCK',
                     [('PRINTLN',
                       ('EXPR', [('BINOP', '-'), ('EXPR', [('INT', 1)])]))])])),
                 ('BLOCK',
                  [('ASSIGNMENT', 'res', ('INT', 1)),
                   ('BLOCK',
                    [('FOR',
                      ('ASSIGNMENT', 'i', ('INT', 1)),
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
                       [('BLOCK',
                         [('ASSIGNMENT',
                           'res',
                           ('EXPR',
                            [('NAME', 'res'),
                             ('EXPR',
                              [('NAME', 'i'),
                               ('EXPR', [('BINOP', '*')])])]))])])),
                     ('BLOCK',
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
                                         [('BINOP',
                                           '+')])])])])])])])])]))])])])])])),
            ('BLOCK',
             [('ASSIGNMENT', 'n', ('INT', 5)),
              ('BLOCK',
               [('RUN', 'factorial'),
                ('BLOCK',
                 [('ASSIGNMENT', 'n', ('INT', 10)),
                  ('BLOCK', [('RUN', 'factorial')])])])])])])])])])])
```