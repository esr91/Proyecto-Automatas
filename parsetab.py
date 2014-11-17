
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\x95a\xbe\xb6\xb0\xfc\xe7\xb3K0R\xcb\xd1\x02H\x05'
    
_lr_action_items = {'IGUAL':([9,],[16,]),'ACORCH':([29,],[30,]),'COMA':([8,],[15,]),'APARENT':([1,],[6,]),'ID':([0,4,6,13,15,16,17,20,24,25,],[2,8,9,9,8,20,22,-7,26,27,]),'PUNTOCOMA':([6,7,8,10,11,12,13,18,19,20,21,23,26,],[-19,14,-16,17,-4,-3,-6,-5,-15,-7,-8,25,-9,]),'CCORCH':([30,],[31,]),'$end':([2,3,5,14,29,31,],[-18,0,-17,-11,-1,-2,]),'MENOR':([22,],[24,]),'FOR':([0,],[1,]),'CPARENT':([27,28,],[-10,29,]),'RESERVADOS':([0,],[4,]),'NUM':([0,],[5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comparacionRet':([17,],[21,]),'paramFor3':([25,],[28,]),'empty':([6,],[11,]),'paramFor1':([6,],[10,]),'comparacionesRet':([17,],[23,]),'asignaciones':([6,13,],[12,18,]),'asignacion':([6,13,],[13,13,]),'emoticon':([0,],[3,]),'ids':([4,15,],[7,19,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> emoticon","S'",1,None,None,None),
  ('emoticon -> FOR APARENT paramFor1 PUNTOCOMA comparacionesRet PUNTOCOMA paramFor3 CPARENT','emoticon',8,'p_for','BreteFinal',79),
  ('emoticon -> FOR APARENT paramFor1 PUNTOCOMA comparacionesRet PUNTOCOMA paramFor3 CPARENT ACORCH CCORCH','emoticon',10,'p_forMultilinea','BreteFinal',83),
  ('paramFor1 -> asignaciones','paramFor1',1,'p_parFor1','BreteFinal',89),
  ('paramFor1 -> empty','paramFor1',1,'p_parFor1','BreteFinal',90),
  ('asignaciones -> asignacion asignaciones','asignaciones',2,'p_asignaciones','BreteFinal',96),
  ('asignaciones -> asignacion','asignaciones',1,'p_asignaciones','BreteFinal',97),
  ('asignacion -> ID IGUAL ID','asignacion',3,'p_asignacion','BreteFinal',105),
  ('comparacionesRet -> comparacionRet','comparacionesRet',1,'p_comparacionesRet','BreteFinal',112),
  ('comparacionRet -> ID MENOR ID','comparacionRet',3,'p_comparacionRet','BreteFinal',120),
  ('paramFor3 -> ID','paramFor3',1,'p_parFor3','BreteFinal',129),
  ('emoticon -> RESERVADOS ids PUNTOCOMA','emoticon',3,'p_declaracion','BreteFinal',133),
  ('pReservadas -> INT','pReservadas',1,'p_reservados','BreteFinal',139),
  ('pReservadas -> DOUBLE','pReservadas',1,'p_reservados','BreteFinal',140),
  ('pReservadas -> FLOAT','pReservadas',1,'p_reservados','BreteFinal',141),
  ('ids -> ID COMA ids','ids',3,'p_ids','BreteFinal',147),
  ('ids -> ID','ids',1,'p_ids2','BreteFinal',152),
  ('emoticon -> NUM','emoticon',1,'p_prueba1','BreteFinal',162),
  ('emoticon -> ID','emoticon',1,'p_prueba2','BreteFinal',166),
  ('empty -> <empty>','empty',0,'p_empty','BreteFinal',170),
]
