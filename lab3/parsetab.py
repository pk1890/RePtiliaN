
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftORNORleftANDNANDNAME FUNCTION RELOP BINOP IF WHILE FOR DEF RUN AND OR NOR NAND INT FLOAT STRING BOOLEAN INT_T FLOAT_T STRING_Tblock : '{' program '}'\n             | statement \n       program : statement ';' program\n               | statement ';'statement : exprstatement : booleanstatement : DEF NAME '=' blockstatement : RUN NAMEstatement : IF '(' boolean ')' block statement : WHILE '(' boolean ')' block statement : FOR '(' statement ';' boolean ';' statement ')' block boolean : relation\n               | BOOLEAN\n               | boolean logicop booleanlogicop : AND \n               | OR\n               | NAND\n               | NORrelation : expr RELOP exprtypename : INT\n                | FLOAT\n                | STRINGrvalue : expr\n              | boolean\n              | numberstatement : typename NAME '=' rvaluestatement : NAME '=' rvalueexpr : name\n            | number\n            | string\n            | name expr\n            | number expr\n            | string expr\n            | sinop expr\n            | binop expr\n            | sinop \n            | binop sinop : FUNCTIONbinop : BINOPname : NAMEstring : STRING_Tinteger : INT_Tfloat : FLOAT_Tnumber : float \n              | integer"
    
_lr_action_items = {'{':([0,56,67,68,76,],[2,2,2,2,2,]),'DEF':([0,2,43,52,56,67,68,74,76,],[6,6,6,6,6,6,6,6,6,]),'RUN':([0,2,43,52,56,67,68,74,76,],[8,8,8,8,8,8,8,8,8,]),'IF':([0,2,43,52,56,67,68,74,76,],[9,9,9,9,9,9,9,9,9,]),'WHILE':([0,2,43,52,56,67,68,74,76,],[10,10,10,10,10,10,10,10,10,]),'FOR':([0,2,43,52,56,67,68,74,76,],[11,11,11,11,11,11,11,11,11,]),'NAME':([0,2,6,7,8,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,32,33,34,35,36,37,39,41,42,43,46,52,56,60,64,67,68,69,74,76,],[7,7,38,-40,40,44,46,46,46,46,46,-20,-21,-22,-44,-45,-41,-38,-39,-43,-42,46,46,-15,-16,-17,-18,46,46,46,7,-40,7,7,46,46,7,7,46,7,7,]),'BOOLEAN':([0,2,33,34,35,36,37,39,41,42,43,52,56,64,67,68,69,74,76,],[19,19,19,-15,-16,-17,-18,19,19,19,19,19,19,19,19,19,19,19,19,]),'INT':([0,2,43,52,56,67,68,74,76,],[20,20,20,20,20,20,20,20,20,]),'FLOAT':([0,2,43,52,56,67,68,74,76,],[21,21,21,21,21,21,21,21,21,]),'STRING':([0,2,43,52,56,67,68,74,76,],[22,22,22,22,22,22,22,22,22,]),'STRING_T':([0,2,7,13,14,15,16,17,23,24,25,26,27,28,29,32,33,34,35,36,37,39,41,42,43,46,52,56,60,64,67,68,69,74,76,],[25,25,-40,25,25,25,25,25,-44,-45,-41,-38,-39,-43,-42,25,25,-15,-16,-17,-18,25,25,25,25,-40,25,25,25,25,25,25,25,25,25,]),'FUNCTION':([0,2,7,13,14,15,16,17,23,24,25,26,27,28,29,32,33,34,35,36,37,39,41,42,43,46,52,56,60,64,67,68,69,74,76,],[26,26,-40,26,26,26,26,26,-44,-45,-41,-38,-39,-43,-42,26,26,-15,-16,-17,-18,26,26,26,26,-40,26,26,26,26,26,26,26,26,26,]),'BINOP':([0,2,7,13,14,15,16,17,23,24,25,26,27,28,29,32,33,34,35,36,37,39,41,42,43,46,52,56,60,64,67,68,69,74,76,],[27,27,-40,27,27,27,27,27,-44,-45,-41,-38,-39,-43,-42,27,27,-15,-16,-17,-18,27,27,27,27,-40,27,27,27,27,27,27,27,27,27,]),'FLOAT_T':([0,2,7,13,14,15,16,17,23,24,25,26,27,28,29,32,33,34,35,36,37,39,41,42,43,46,52,56,60,64,67,68,69,74,76,],[28,28,-40,28,28,28,28,28,-44,-45,-41,-38,-39,-43,-42,28,28,-15,-16,-17,-18,28,28,28,28,-40,28,28,28,28,28,28,28,28,28,]),'INT_T':([0,2,7,13,14,15,16,17,23,24,25,26,27,28,29,32,33,34,35,36,37,39,41,42,43,46,52,56,60,64,67,68,69,74,76,],[29,29,-40,29,29,29,29,29,-44,-45,-41,-38,-39,-43,-42,29,29,-15,-16,-17,-18,29,29,29,29,-40,29,29,29,29,29,29,29,29,29,]),'$end':([1,3,4,5,7,13,14,15,16,17,18,19,23,24,25,26,27,28,29,40,45,46,47,48,49,50,51,53,54,57,58,59,60,66,70,71,72,77,],[0,-2,-5,-6,-40,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,-8,-31,-40,-32,-33,-34,-35,-1,-19,-14,-27,-23,-24,-25,-7,-26,-9,-10,-11,]),';':([3,4,5,7,13,14,15,16,17,18,19,23,24,25,26,27,28,29,31,40,45,46,47,48,49,50,51,53,54,57,58,59,60,63,66,70,71,72,73,77,],[-2,-5,-6,-40,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,52,-8,-31,-40,-32,-33,-34,-35,-1,-19,-14,-27,-23,-24,-25,69,-7,-26,-9,-10,74,-11,]),')':([3,4,5,7,13,14,15,16,17,18,19,23,24,25,26,27,28,29,40,45,46,47,48,49,50,51,53,54,57,58,59,60,61,62,66,70,71,72,75,77,],[-2,-5,-6,-40,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,-8,-31,-40,-32,-33,-34,-35,-1,-19,-14,-27,-23,-24,-25,67,68,-7,-26,-9,-10,76,-11,]),'RELOP':([4,7,13,14,15,16,17,23,24,25,26,27,28,29,45,46,47,48,49,50,55,58,60,],[32,-40,-28,-29,-30,-36,-37,-44,-45,-41,-38,-39,-43,-42,-31,-40,-32,-33,-34,-35,32,32,-29,]),'AND':([5,13,14,15,16,17,18,19,23,24,25,26,27,28,29,45,46,47,48,49,50,53,54,59,61,62,73,],[34,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,-31,-40,-32,-33,-34,-35,-19,34,34,34,34,34,]),'OR':([5,13,14,15,16,17,18,19,23,24,25,26,27,28,29,45,46,47,48,49,50,53,54,59,61,62,73,],[35,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,-31,-40,-32,-33,-34,-35,-19,35,35,35,35,35,]),'NAND':([5,13,14,15,16,17,18,19,23,24,25,26,27,28,29,45,46,47,48,49,50,53,54,59,61,62,73,],[36,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,-31,-40,-32,-33,-34,-35,-19,36,36,36,36,36,]),'NOR':([5,13,14,15,16,17,18,19,23,24,25,26,27,28,29,45,46,47,48,49,50,53,54,59,61,62,73,],[37,-28,-29,-30,-36,-37,-12,-13,-44,-45,-41,-38,-39,-43,-42,-31,-40,-32,-33,-34,-35,-19,37,37,37,37,37,]),'=':([7,38,44,],[39,56,64,]),'(':([9,10,11,],[41,42,43,]),'}':([30,52,65,],[51,-4,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'block':([0,56,67,68,76,],[1,66,71,72,77,]),'statement':([0,2,43,52,56,67,68,74,76,],[3,31,63,31,3,3,3,75,3,]),'expr':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[4,4,45,47,48,49,50,53,55,58,55,55,4,4,4,47,58,4,4,55,4,4,]),'boolean':([0,2,33,39,41,42,43,52,56,64,67,68,69,74,76,],[5,5,54,59,61,62,5,5,5,59,5,5,73,5,5,]),'typename':([0,2,43,52,56,67,68,74,76,],[12,12,12,12,12,12,12,12,12,]),'name':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'number':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[14,14,14,14,14,14,14,14,14,60,14,14,14,14,14,14,60,14,14,14,14,14,]),'string':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'sinop':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'binop':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'relation':([0,2,33,39,41,42,43,52,56,64,67,68,69,74,76,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'float':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'integer':([0,2,13,14,15,16,17,32,33,39,41,42,43,52,56,60,64,67,68,69,74,76,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'program':([2,52,],[30,65,]),'logicop':([5,54,59,61,62,73,],[33,33,33,33,33,33,]),'rvalue':([39,64,],[57,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> block","S'",1,None,None,None),
  ('block -> { program }','block',3,'p_block','rpn_calc.py',109),
  ('block -> statement','block',1,'p_block','rpn_calc.py',110),
  ('program -> statement ; program','program',3,'p_block','rpn_calc.py',111),
  ('program -> statement ;','program',2,'p_block','rpn_calc.py',112),
  ('statement -> expr','statement',1,'p_statement_expr','rpn_calc.py',123),
  ('statement -> boolean','statement',1,'p_statement_relation','rpn_calc.py',127),
  ('statement -> DEF NAME = block','statement',4,'p_statement_fundef','rpn_calc.py',131),
  ('statement -> RUN NAME','statement',2,'p_statement_run','rpn_calc.py',134),
  ('statement -> IF ( boolean ) block','statement',5,'p_statement_cond','rpn_calc.py',138),
  ('statement -> WHILE ( boolean ) block','statement',5,'p_statement_while','rpn_calc.py',144),
  ('statement -> FOR ( statement ; boolean ; statement ) block','statement',9,'p_statement_for','rpn_calc.py',149),
  ('boolean -> relation','boolean',1,'p_boolean','rpn_calc.py',157),
  ('boolean -> BOOLEAN','boolean',1,'p_boolean','rpn_calc.py',158),
  ('boolean -> boolean logicop boolean','boolean',3,'p_boolean','rpn_calc.py',159),
  ('logicop -> AND','logicop',1,'p_logicop','rpn_calc.py',163),
  ('logicop -> OR','logicop',1,'p_logicop','rpn_calc.py',164),
  ('logicop -> NAND','logicop',1,'p_logicop','rpn_calc.py',165),
  ('logicop -> NOR','logicop',1,'p_logicop','rpn_calc.py',166),
  ('relation -> expr RELOP expr','relation',3,'p_relation','rpn_calc.py',171),
  ('typename -> INT','typename',1,'p_typename','rpn_calc.py',175),
  ('typename -> FLOAT','typename',1,'p_typename','rpn_calc.py',176),
  ('typename -> STRING','typename',1,'p_typename','rpn_calc.py',177),
  ('rvalue -> expr','rvalue',1,'p_rvalue','rpn_calc.py',181),
  ('rvalue -> boolean','rvalue',1,'p_rvalue','rpn_calc.py',182),
  ('rvalue -> number','rvalue',1,'p_rvalue','rpn_calc.py',183),
  ('statement -> typename NAME = rvalue','statement',4,'p_declaration','rpn_calc.py',187),
  ('statement -> NAME = rvalue','statement',3,'p_statement_assignment','rpn_calc.py',191),
  ('expr -> name','expr',1,'p_expr','rpn_calc.py',199),
  ('expr -> number','expr',1,'p_expr','rpn_calc.py',200),
  ('expr -> string','expr',1,'p_expr','rpn_calc.py',201),
  ('expr -> name expr','expr',2,'p_expr','rpn_calc.py',202),
  ('expr -> number expr','expr',2,'p_expr','rpn_calc.py',203),
  ('expr -> string expr','expr',2,'p_expr','rpn_calc.py',204),
  ('expr -> sinop expr','expr',2,'p_expr','rpn_calc.py',205),
  ('expr -> binop expr','expr',2,'p_expr','rpn_calc.py',206),
  ('expr -> sinop','expr',1,'p_expr','rpn_calc.py',207),
  ('expr -> binop','expr',1,'p_expr','rpn_calc.py',208),
  ('sinop -> FUNCTION','sinop',1,'p_sinop','rpn_calc.py',215),
  ('binop -> BINOP','binop',1,'p_binop','rpn_calc.py',219),
  ('name -> NAME','name',1,'p_var','rpn_calc.py',223),
  ('string -> STRING_T','string',1,'p_string','rpn_calc.py',227),
  ('integer -> INT_T','integer',1,'p_integer','rpn_calc.py',231),
  ('float -> FLOAT_T','float',1,'p_float','rpn_calc.py',235),
  ('number -> float','number',1,'p_number','rpn_calc.py',239),
  ('number -> integer','number',1,'p_number','rpn_calc.py',240),
]
