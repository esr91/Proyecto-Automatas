tokens = ('INT','NUM','ID','FLOAT','DOUBLE','COMA','NUMBER',
    'MAS','MENOS','POR','DIVIDE','IGUAL',
    'LPAREN','MAYOR','MENOR','RPAREN','PUNTOCOMA','CCORCH','EMPTY','ACORCH','CPARENT','APARENT','RESERVADOS','FOR')

t_MAS    = r'\+'
t_MENOS   = r'-'
t_POR   = r'\*'
t_DIVIDE  = r'/'
t_IGUAL  = r'='
t_APARENT  = r'\('
t_CPARENT  = r'\)'
t_ACORCH  = r'\{'
t_CCORCH  = r'\}'
t_MAYOR= r'\>' 
t_MENOR= r'\<' 
t_PUNTOCOMA= r'\;' 



def t_NUM(t):
	r'\d+'
	return t
	

def t_RESERVADOS (t):
	r'int|double|float'
	return t
def t_FOR (t):
	r'for'
	return t
def t_ID (t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'	
	return t
	
	return t
t_COMA  = r'\,'



'''def t_BOCA(t):
    r'\(|\)|D|O|P'
    if t.value == 'D':
        t.value = 'feliz'
    elif t.value == 'O':
        t.value = 'sorprendido'
    return t
'''

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
 

    
def t_error(t):
    print("Emoción mal definida '%s'" % t.value[0])
    t.lexer.skip(1)
    

import ply.lex as lex
lex.lex()


#parser
'''
def p_emoticonsincejas(p):
    'emoticon : OJOS BOCA'
    print (p[2])

def p_emoticonconcejas(p):
    'emoticon : CEJAS OJOS BOCA'
    print (p[3])
'''	
#############FOR#########
#for (asignaciones;comparaciones;cambios) // Puede ser seguido de una linea donde no requiere {} y cuando es de mas de una linea si requiere {}
def p_for(p):
	'emoticon : FOR APARENT	paramFor1	PUNTOCOMA	comparacionesRet	PUNTOCOMA	paramFor3	   CPARENT '
	print("Mientras",p[5],"hacemos:")
	
def p_forMultilinea(p):
	'emoticon : FOR APARENT	paramFor1	PUNTOCOMA	comparacionesRet	PUNTOCOMA	paramFor3	   CPARENT ACORCH CCORCH'
	print("esto es un for multilinea")
	
##########PARAMFOR1######
# Recibe el primer parametro del for que puede ser asignaciones o vacia en caso de que las var a usar ya hayan sido declaradas
def p_parFor1(p):
	'''paramFor1 : asignaciones
	| empty'''
	if p[1] == 'empty': '''Aqui como es vacia no deberia de imprimir nada '''
	
######ASIGNACIONES####### 
# En caso del for permite varias asignaciones en su primer parametro 
def p_asignaciones(p):
	'''asignaciones : asignacion asignaciones
	| asignacion'''

#######ASIGNACION######## 
# Permite declarar una variable y darle una otra variable como valor
# Permite declarar una variable y darle un numero como valor
# Permite darle a una variable ya declarada una nueva variable como valor 
# Permite darle a una variable ya declarada un numero como valor
def p_asignacion(p):
	'asignacion : ID IGUAL ID'
	print (p[1],"->",p[3] )
	
#######COMPARACIONES######## 
# Recibe el primer parametro del for que puede ser asignaciones o vacia en caso de que las var a usar ya hayan sido declaradas
# Recibe 1 o mas comparaciones	
def p_comparacionesRet(p):	#Estas devuelven lo quese debe imprimir para hacerlo en la misma linea de mi padre
	'comparacionesRet : comparacionRet'
	#if (len(p) == 3):
	p[0] = p[1]
	#elif (len(p) == 2):
	#	p[0] = p[1] 
	
#######COMPARACION######ESTAN LAS QUE IMPRIMEN EN SI MISMAS Y LAS QUE IMPRIMEN EN SUS PADRES
def p_comparacionRet(p):#DEVUELVE A SU PAADRE QUE IMPRIMIR
	'comparacionRet : ID MENOR ID'
	#P[0] = "hace la compa"
'''
######OPBOOLEANO#########
def p_opbooleano(p):
	'opbooleano : MENOR' #|MENORIG|MAYOR|MAYORIG|IGUAA|DIFERENTEDE'''
	#p[0] = 'menor que'
	
def p_parFor3(p):
	'paramFor3 : ID'
	print ("parametro 3 for")
	
def p_declaracion(p):
	'emoticon : RESERVADOS ids PUNTOCOMA'
	print ("%s declarados:" %p[1])
	print (p[2])
	print ("\n")
	
def p_reservados(p):
	''' pReservadas : INT
					| DOUBLE
					| FLOAT'''
	if p[1] == 'int'  : p[0] = 'int'
	elif p[1] == 'double': p[0] = 'double'
	elif p[1] == 'float': p[0] = 'float'
	
def p_ids(p):
	'ids : ID COMA ids'
	p[0]=p[1]+p[3]
	'''print ("imprimo desde ids 3")'''
		
def p_ids2(p):
	'ids : ID'
	'''print ("imprimo desde ids 1")'''
	p[0] = p[1]


'''
def p_id(p):
	'emoticon : ID'
'''
def p_prueba1(p):
    'emoticon : NUM'
    print ("NUM:%s"%p[1])

def p_prueba2(p):
	'emoticon : ID'
	p[0]=1

def p_empty(p):
	'empty :'
	p[0]='empty'
	pass
	
    
	
def p_error(p):
    if p:
        print("Error de sintaxis en '%s'" % p.value)
    else:
        print(">.> Revise su funcion >.>")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('> ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
