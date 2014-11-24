cuentaTabs = ""
tokens = ('INT','NUM','ID','FLOAT','DOUBLE','CHAR','COMA','MAS','MENOS','POR','DIVIDE','MODULO',
	'IGUAL','IGUALIG','DIFERENTE','AND','OR','MAYOR','MAYORIG','MENOR','MENORIG',
	'PUNTOCOMA','CCORCH','TAB','ACORCH','CPARENT','APARENT','RESERVADOS','FOR','IF')

t_MAS    = r'\+'
t_MENOS   = r'-'
t_POR   = r'\*'
t_DIVIDE  = r'/'
t_MODULO  = r'\%'
t_IGUAL  = r'='
t_APARENT  = r'\('
t_CPARENT  = r'\)'
t_ACORCH  = r'\{'
t_CCORCH  = r'\}'
t_MAYOR= r'\>' 
t_MENOR= r'\<' 
t_PUNTOCOMA= r'\;' 
t_MENORIG= r'\<='
t_MAYORIG= r'\>='
t_DIFERENTE= r'!='
t_IGUALIG= r'=='
t_AND= r'&&'
t_OR= r'\|\|'



def t_NUM(t):
	r'\d+'
	return t
	
def t_RESERVADOS (t):
	r'int|double|float|char'
	return t
def t_FOR (t):
	r'for'
	return t
def t_IF (t):
	r'if'
	return t
def t_ID (t):
	r'[a-zA_Z][a-zA-Z0-9_]*'	
	return t
t_COMA  = r'\,'
def t_TAB(t):
	r'[\t]'
	#return t
	#printNuestro ('\t', end ="")
	
def printNuestro(t):
	print (cuentaTabs, end = "")
	print (t)




'''def t_BOCA(t):
    r'\(|\)|D|O|P'
    if t.value == 'D':
        t.value = 'feliz'
    elif t.value == 'O':
        t.value = 'sorprendido'
    return t
'''

t_ignore = " "

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
 

    
def t_error(t):
    printNuestro("Emoción mal definida '%s'" % t.value[0])
    t.lexer.skip(1)
    

import ply.lex as lex
lex.lex()


#parser
'''
def p_emoticonsincejas(p):
    'emoticon : OJOS BOCA'
    printNuestro (p[2])

def p_emoticonconcejas(p):
    'emoticon : CEJAS OJOS BOCA'
    printNuestro (p[3])
'''	

#############MAIN#########
def p_main(p):
	'emoticon : instrucciones'
	printNuestro ('\n')
#############CUERPO#########
def p_cuerpo(p):
	'''cuerpo : instrucciones
	| instrucciones instrucciones
	| empty'''
	
#############INSTRUCCIONES#########Este presenta conflictos
def p_instrucciones(p):
	'''instrucciones : instruccion instrucciones 
	| instruccioncuerpo instrucciones
	| instruccion
	| instruccioncuerpo'''
#############INSTRUCCION#########
def p_instruccioncuerpo(p):# for, if ,while
	'''instruccioncuerpo : for acorch cuerpo ccorch
	| if acorch cuerpo ccorch'''
	printNuestro ("}")

def p_acorch(p):# for, if ,while
	'acorch : ACORCH'
	global cuentaTabs
	cuentaTabs = cuentaTabs+"\t"
	#printNuestro ('*'+cuentaTabs+'*')

def p_ccorch(p):# for, if ,while
	'ccorch : CCORCH'
	global cuentaTabs
	cuentaTabs = cuentaTabs[:-1]
	#printNuestro ('*'+cuentaTabs+'*')
	
def p_instruccion(p): ### Asignaciones o funciones o metodos
	'''instruccion : asignacion PUNTOCOMA '''
	


#############IF#########
def p_if(p):
	'if : IF APARENT comparacionRet CPARENT'
	printNuestro("Si "+p[3]+"{")



#############FOR#########
#for (asignaciones;comparaciones;cambios) // Puede ser seguido de una linea donde no requiere {} y cuando es de mas de una linea si requiere {}
def p_for(p):
	'for : FOR APARENT	paramFor1	PUNTOCOMA	comparacionesRet	PUNTOCOMA	paramFor3	   CPARENT'
	printNuestro (p[3])
	printNuestro("Para "+p[5]+", "+p[7]+"{")
	
	
##########PARAMFOR1######
# Recibe el primer parametro del for que puede ser asignaciones o vacia en caso de que las var a usar ya hayan sido declaradas
#def p_parFor1(p):
#	'''paramFor1 : asignaciones
#	| empty'''
#	if p[1] == 'empty': '''Aqui como es vacia no deberia de imprimir nada '''
def p_parFor1(p):
	'''paramFor1 : asignacionesRet
	| empty'''
	p[0] = p[1]
	
######ASIGNACIONES####### 
# En caso del for permite varias asignaciones en su primer parametro 
def p_asignacionesRet(p):
	'''asignacionesRet : asignacionRet asignacionesRet
	| asignacionRet'''
	if (len(p) == 3): p[0] = p[1]+"\n"+cuentaTabs+p[2]
	elif (len(p) == 2):  p[0] = p[1]

#######ASIGNACION######## 
def p_asignacionRet(p):
	'''asignacionRet : ID IGUAL valor
	| RESERVADOS ID IGUAL valor''' 
	if (len(p) == 4): p[0] =(p[1]+"<-"+p[3] )
	elif (len(p) == 5):  p[0] = (p[2]+"<-"+p[4] )

def p_asignacion(p):
	'''asignacion : ID IGUAL valor
	| RESERVADOS ID IGUAL valor''' 
	if (len(p) == 4): 
		printNuestro (p[1]+"<-"+p[3] )
	elif (len(p) == 5):  
		printNuestro (p[2]+"<-"+p[4] )
	
#######COMPARACIONES######## 
# Recibe el primer parametro del for que puede ser asignaciones o vacia en caso de que las var a usar ya hayan sido declaradas
# Recibe 1 o mas comparaciones	
def p_comparacionesRet(p):	#Estas devuelven lo quese debe imprimir para hacerlo en la misma linea de mi padre
	'comparacionesRet : comparacionRet'
	p[0] = p[1]
	
#######COMPARACION######ESTAN LAS QUE IMPRIMEN EN SI MISMAS Y LAS QUE IMPRIMEN EN SUS PADRES
def p_comparacionRet(p):#DEVUELVE A SU PAADRE QUE IMPRIMIR
	'comparacionRet : valor opbooleano valor'
	p[0] = (p[1]+p[2]+p[3])
	
#######CAMBIO"INCREMENTO DECREMENTO"######
def p_incredecremntoRet(p):
	'''paramFor3 : ID MAS MAS
	| MAS MAS ID
	| MENOS MENOS ID
	| ID MENOS MENOS'''
	if(p[1] == '+') : p[0] =("se incrementa "+p[3])
	elif (p[3] == '+') :p[0] =("se incrementa "+p[1])
	elif (p[1] == '-') :p[0] =("se decrementa "+p[3])
	elif (p[3] == '-') :p[0] =("se decrementa "+p[1])

######OPBOOLEANO#########
def p_opbooleano(p):
	'''opbooleano : MENOR
	| MENORIG
	| MAYOR
	| MAYORIG
	| IGUALIG
	| DIFERENTE 
	| AND
	| OR'''
	if(p[1]== '<') : p[0] = " menor que "
	elif(p[1]== "<=") : p[0] = " menor o igual que "
	elif(p[1]== ">") : p[0] = " mayor que "
	elif(p[1]== ">=") : p[0] = " mayor o igual que "
	elif(p[1]== "==") : p[0] = " igual que "
	elif(p[1]== "!=") : p[0] = " diferente de "
	elif(p[1]== "&&") : p[0] = " y "
	elif(p[1]== "||") : p[0] = " o "

	
######OPERADOR#########
def p_oper(p):
	'''oper : MAS
	| MENOS
	| POR
	| DIVIDE
	| MODULO'''
	
	
######VALOR#########
def p_valor(p):
	'''valor : NUM
	| ID
	| APARENT valor CPARENT
	| valor oper valor'''
	p[0] = p[1]
	
def p_parFor3(p):
	'paramFor3 : ID'
	printNuestro ("parametro 3 for")
	
def p_declaracion(p):
	'emoticon : RESERVADOS ids PUNTOCOMA'
	printNuestro ("%s declarados:" %p[1])
	printNuestro (p[2])
	printNuestro ("\n")
	
#def p_reservados(p):
#	''' pReservadas : INT
#					| DOUBLE
#					| FLOAT'''
#	if p[1] == 'int'  : p[0] = 'int'
#	elif p[1] == 'double': p[0] = 'double'
#	elif p[1] == 'float': p[0] = 'float'
	
def p_ids(p):
	'ids : ID COMA ids'
	p[0]=p[1]+p[3]
	'''printNuestro ("imprimo desde ids 3")'''
		
def p_ids2(p):
	'ids : ID'
	'''printNuestro ("imprimo desde ids 1")'''
	p[0] = p[1]


'''
def p_id(p):
	'emoticon : ID'
'''
def p_prueba1(p):
    'emoticon : NUM'
    printNuestro ("NUM:%s"%p[1])

def p_prueba2(p):
	'emoticon : ID'

def p_empty(p):
	'empty :'
	p[0]=""
	pass
	
#def p_tab(p):
#	'''tab : TAB tab
#	| TAB
#	| '''
#	if (len(p) == 3): print ('\t')
#	elif (len(p)== 2) : printNuestro ('\t')
	
	
def p_error(p):
    if p:
        printNuestro("Error de sintaxis en '%s'" % p.value)
    else:
        printNuestro(">.> Revise su funcion >.>")

import ply.yacc as yacc
yacc.yacc()

f = open('pruebasParaBreteFinal.txt', 'r')
#print (f.read())
print ('\n')
f.seek(0)
#while 1:
	#s = input('> ')
s = f.read()

yacc.parse(s)
