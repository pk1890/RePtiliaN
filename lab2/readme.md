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
> a = 5
> b = 2
> b a ^ b -
30
> for(i = 1; i < 5; i = i 1 +){i 2 ^;}
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

