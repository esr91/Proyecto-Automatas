cuentaTabs = ""
varMetRet = 0
tokens = ('INT','NO','NUM','ID','FLOAT','DOUBLE','CHAR','COMA','MAS','MENOS','POR','DIVIDE','MODULO',
	'IGUAL','IGUALIG','DIFERENTE','AND','OR','MAYOR','MAYORIG','MENOR','MENORIG',
	'PUNTOCOMA','DOBLEDOSPUNTOS','RETURN','ELSE','COMENTARIOS1','COMENTARIOS2','CCORCH','ACORCH','CPARENT','APARENT','RESERVADOS','FOR','IF','WHILE')

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
t_NO= r'!'
t_COMA= r'\,'
t_DOBLEDOSPUNTOS = r'::'



def t_NUM(t):
	r'\d+'
	return t
def t_RETURN(t):
	r'return'
	return t
	
def t_RESERVADOS (t):
	r'int|double|float|char|void'
	return t
def t_FOR (t):
	r'for'
	return t
def t_WHILE (t):
	r'while'
	return t
def t_IF (t):
	r'if'
	return t
def t_ELSE (t):
	r'else'
	return t
def t_ID (t):
	r'[a-zA-Z][a-zA-Z0-9_]*(((->)|\.)*[a-zA-Z][a-zA-Z0-9_]*)*'
	return t
def t_TAB(t):
	r'[\t]'
def t_COMENTARIOS1(t):
	r'\/\*[^[\*\/]]*\*\/'
def t_COMENTARIOS2(t):
	r'\/\/[^\n]+'
	
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
	'''emoticon : nombreMetodo acorch instrucciones ccorch
	| nombreMetodo acorch instrucciones ccorch emoticon'''
	printNuestro ('\n\n')

#############NOMBREMETODO#########
def p_nombreMetodo(p):
	'''nombreMetodo : RESERVADOS ID APARENT valores CPARENT
	| RESERVADOS ID DOBLEDOSPUNTOS ID APARENT valores CPARENT'''
	printNuestro ('\n***************************************************************************\n')
	if(len(p)==6):printNuestro (p[2]+"("+p[4]+")")
	else:printNuestro (p[4]+"("+p[6]+")")

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
	| if acorch cuerpo ccorch
	| if acorch cuerpo ccorch else instruccion
	| if acorch cuerpo ccorch else acorch cuerpo ccorch
	| while acorch cuerpo ccorch'''

def p_acorch(p):# for, if ,while
	'acorch : ACORCH'
	global cuentaTabs
	cuentaTabs = cuentaTabs+"\t"

def p_ccorch(p):# for, if ,while
	'ccorch : CCORCH'
	global cuentaTabs
	cuentaTabs = cuentaTabs[:-1]
	
def p_instruccion(p): ### Asignaciones o funciones o metodos
	'''instruccion : asignacion PUNTOCOMA 
	| incredecremnto PUNTOCOMA
	| return PUNTOCOMA
	| metodo PUNTOCOMA'''
	
	

##############RETORNO############# llamado a otro metodo
def p_return(p):
	'return : RETURN ID' 
	printNuestro("Devuelve "+p[2])

##############METODO############# llamado a otro metodo
def p_metodo(p):
	'metodo : ID APARENT valores CPARENT'
	printNuestro("Llamado metodo :"+p[1]+"("+p[3]+")")
	
def p_metodoRet(p):
	'metodoRet : ID APARENT valores CPARENT'
	global varMetRet
	p[0]=(p[1]+"("+p[3]+")")
	varMetRet = 1
	


#############IF#########
def p_if(p):
	'if : IF APARENT comparacionRet CPARENT'
	printNuestro("Si ("+p[3]+") entonces:")
#############ELSE#########
def p_else(p):
	'else : ELSE '
	printNuestro("Sino:")
	

#############WHILE#########
def p_while(p):
	'while : WHILE APARENT comparacionRet CPARENT'
	printNuestro("Mientras ("+p[3]+") haga:")



#############FOR#########
#for (asignaciones;comparaciones;cambios) // Puede ser seguido de una linea donde no requiere {} y cuando es de mas de una linea si requiere {}
def p_for(p):
	'for : FOR APARENT	paramFor1	PUNTOCOMA	comparacionesRet	PUNTOCOMA	incredecremntoRet	   CPARENT'
	printNuestro("Para "+p[5]+", "+p[7])
	
	
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
	'''asignacionesRet : asignacion asignacionesRet
	| asignacion'''
	#if (len(p) == 3): p[0] = p[1]+"\n"+cuentaTabs+p[2]
	#elif (len(p) == 2):  p[0] = p[1]

#######ASIGNACION######## 
#def p_asignacionRet(p):
#	'''asignacionRet : ID IGUAL valor
#	| RESERVADOS ID IGUAL valor''' 
#	if (len(p) == 4): p[0] =(p[1]+"<-"+p[3] )
#	elif (len(p) == 5):  p[0] = (p[2]+"<-"+p[4] )

def p_asignacion(p):
	'''asignacion : ID IGUAL valor
	| RESERVADOS ID IGUAL valor
	| ids IGUAL ids
	| ID POR ID IGUAL valor
	| ID POR ID IGUAL ID metodoRet'''
	if (len(p) == 4): 
		printNuestro (p[1]+"<-"+p[3] )
	elif (len(p) == 5):  
		printNuestro (p[2]+"<-"+p[4] )
	elif (len(p) == 6):  
		printNuestro (p[1]+'*'+p[3]+"<-"+p[5] )
	elif (len(p) == 7):  
		printNuestro (p[1]+'*'+p[3]+"<-"+p[5]+" "+p[6] )
	
	
#######COMPARACIONES######## 
# Recibe el primer parametro del for que puede ser asignaciones o vacia en caso de que las var a usar ya hayan sido declaradas
# Recibe 1 o mas comparaciones	
def p_comparacionesRet(p):	#Estas devuelven lo quese debe imprimir para hacerlo en la misma linea de mi padre
	'comparacionesRet : comparacionRet'
	p[0] = p[1]
	
#######COMPARACION######ESTAN LAS QUE IMPRIMEN EN SI MISMAS Y LAS QUE IMPRIMEN EN SUS PADRES
def p_comparacionRet(p):#DEVUELVE A SU PAADRE QUE IMPRIMIR
	'''comparacionRet : APARENT comparacionRet CPARENT
	| APARENT valor opbooleano valor CPARENT
	| comparacionRet opbooleano comparacionRet
	| metodoRet	
	| valor
	| NO comparacionRet'''
	global varMetRet
	if (p[1] == '(') : 
		if(len(p) == 6) : p[0] = ('('+p[2]+p[3]+p[4]+')')
		else : p[0] = ('('+p[2]+')')
	elif(p[1]=='!') : p[0] = ("no booleano de:"+p[2])
	elif(varMetRet == 1): 
		
		p[0] = p[1]
		varMetRet = 0
	elif(len(p) == 2) : p[0] = '('+p[1]+')'
	else : p[0] = (p[1]+p[2]+p[3])
	
#######CAMBIO"INCREMENTO DECREMENTO"######
def p_incredecremntoRet(p):
	'''incredecremntoRet : ID MAS MAS
	| MAS MAS ID
	| MENOS MENOS ID
	| ID MENOS MENOS'''
	if(p[1] == '+') : p[0] =("se incrementa "+p[3])
	elif (p[3] == '+') :p[0] =("se incrementa "+p[1])
	elif (p[1] == '-') :p[0] =("se decrementa "+p[3])
	elif (p[3] == '-') :p[0] =("se decrementa "+p[1])

def p_incredecremnto(p):
	'''incredecremnto : ID MAS MAS
	| MAS MAS ID
	| MENOS MENOS ID
	| ID MENOS MENOS'''
	if(p[1] == '+') : printNuestro("se incrementa "+p[3])
	elif (p[3] == '+') :printNuestro("Se incrementa "+p[1])
	elif (p[1] == '-') :printNuestro("Se decrementa "+p[3])
	elif (p[3] == '-') :printNuestro("Se decrementa "+p[1])

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
	p[0]=p[1]
		
######VALORES#########
def p_valores(p):
	''' valores : valor COMA valores 
	| valor
	| empty'''
	if(len(p)==2):p[0]= p[1]
	else: p[0] = p[1]+','+p[3]

######VALOR#########
def p_valor(p):
	'''valor : NUM
	| ID
	| APARENT valor CPARENT
	| valor oper valor
	| incredecremntoRet'''
	if((len(p))==2): 
		p[0] = p[1]
	elif(p[1]=='(') : 
		p[0] = p[2]
	else : 
		p[0] = '('+p[1]+p[2]+p[3]+')'
	

	
#def p_reservados(p):
#	''' pReservadas : INT
#					| DOUBLE
#					| FLOAT'''
#	if p[1] == 'int'  : p[0] = 'int'
#	elif p[1] == 'double': p[0] = 'double'
#	elif p[1] == 'float': p[0] = 'float'
	
def p_ids(p):
	'ids : ID ids'
	p[0]=p[1]+p[3]
		
def p_ids2(p):
	'ids : ID'
	p[0] = p[1]




def p_empty(p):
	'empty :'
	p[0]=""
	pass
	

	
	
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
