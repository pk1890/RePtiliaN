
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*/rightPOWERrightMINUSrightFUNCTIONDOUBLE FUNCTION INTEGER NAME POWER RELOPexpressions : expression \n                    | expression ';' expressions\n                    | expression ';'expression : NAME '=' exprexpression : expr RELOP exprexpression : exprexpr : FUNCTION exprexpr : expr '+' exprexpr : expr '-' exprexpr : expr '*' exprexpr : expr '/' exprexpr : expr POWER exprexpr : '(' expr ')'expr : '-' expr %prec MINUSexpr : numbernumber : INTEGER \n              | DOUBLEexpr : NAME"
    
_lr_action_items = {'NAME':([0,5,6,7,11,12,13,14,15,16,17,18,],[3,20,20,20,3,20,20,20,20,20,20,20,]),'FUNCTION':([0,5,6,7,11,12,13,14,15,16,17,18,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'(':([0,5,6,7,11,12,13,14,15,16,17,18,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'-':([0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,],[6,-18,15,6,6,6,-15,-16,-17,6,6,6,6,6,6,6,6,-7,-18,-14,15,15,15,-8,-9,-10,-11,-12,-13,]),'INTEGER':([0,5,6,7,11,12,13,14,15,16,17,18,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'DOUBLE':([0,5,6,7,11,12,13,14,15,16,17,18,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,8,9,10,11,19,20,21,23,24,25,26,27,28,29,30,31,],[0,-1,-18,-6,-15,-16,-17,-3,-7,-18,-14,-2,-4,-5,-8,-9,-10,-11,-12,-13,]),';':([2,3,4,8,9,10,19,20,21,24,25,26,27,28,29,30,31,],[11,-18,-6,-15,-16,-17,-7,-18,-14,-4,-5,-8,-9,-10,-11,-12,-13,]),'=':([3,],[12,]),'RELOP':([3,4,8,9,10,19,20,21,26,27,28,29,30,31,],[-18,13,-15,-16,-17,-7,-18,-14,-8,-9,-10,-11,-12,-13,]),'+':([3,4,8,9,10,19,20,21,22,24,25,26,27,28,29,30,31,],[-18,14,-15,-16,-17,-7,-18,-14,14,14,14,-8,-9,-10,-11,-12,-13,]),'*':([3,4,8,9,10,19,20,21,22,24,25,26,27,28,29,30,31,],[-18,16,-15,-16,-17,-7,-18,-14,16,16,16,16,16,-10,-11,-12,-13,]),'/':([3,4,8,9,10,19,20,21,22,24,25,26,27,28,29,30,31,],[-18,17,-15,-16,-17,-7,-18,-14,17,17,17,17,17,-10,-11,-12,-13,]),'POWER':([3,4,8,9,10,19,20,21,22,24,25,26,27,28,29,30,31,],[-18,18,-15,-16,-17,-7,-18,-14,18,18,18,18,18,18,18,18,-13,]),')':([8,9,10,19,20,21,22,26,27,28,29,30,31,],[-15,-16,-17,-7,-18,-14,31,-8,-9,-10,-11,-12,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,11,],[1,23,]),'expression':([0,11,],[2,2,]),'expr':([0,5,6,7,11,12,13,14,15,16,17,18,],[4,19,21,22,4,24,25,26,27,28,29,30,]),'number':([0,5,6,7,11,12,13,14,15,16,17,18,],[8,8,8,8,8,8,8,8,8,8,8,8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression','expressions',1,'p_expressions','calc.py',95),
  ('expressions -> expression ; expressions','expressions',3,'p_expressions','calc.py',96),
  ('expressions -> expression ;','expressions',2,'p_expressions','calc.py',97),
  ('expression -> NAME = expr','expression',3,'p_expression_assignment','calc.py',100),
  ('expression -> expr RELOP expr','expression',3,'p_expression_relop','calc.py',103),
  ('expression -> expr','expression',1,'p_expression_expr','calc.py',117),
  ('expr -> FUNCTION expr','expr',2,'p_function','calc.py',120),
  ('expr -> expr + expr','expr',3,'p_add','calc.py',123),
  ('expr -> expr - expr','expr',3,'p_sub','calc.py',126),
  ('expr -> expr * expr','expr',3,'p_mul','calc.py',129),
  ('expr -> expr / expr','expr',3,'p_div','calc.py',132),
  ('expr -> expr POWER expr','expr',3,'p_pow','calc.py',135),
  ('expr -> ( expr )','expr',3,'p_parenthesis','calc.py',138),
  ('expr -> - expr','expr',2,'p_minus','calc.py',141),
  ('expr -> number','expr',1,'p_expr_number','calc.py',144),
  ('number -> INTEGER','number',1,'p_number','calc.py',147),
  ('number -> DOUBLE','number',1,'p_number','calc.py',148),
  ('expr -> NAME','expr',1,'p_var','calc.py',151),
]
