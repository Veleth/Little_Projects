from module.lexer import lexer, tokens
from module.interpreter import evaluate
from ply import yacc
#TODO: add grammar rules
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'POWER', 'SQRT'),
    ('right', 'UMINUS')
)

def p_calc(p):
    '''
    calc : expression
         | empty
    '''
    evaluate(p[1])
    

def p_var_assign(p):
    '''
    var_assign : NAME ASSIGN expression
    '''
    p[0] = ('=', p[1], p[3])
    #names[p[1]] = p[3]

def p_expression(p):
    '''
    expression : expression POWER expression
               | expression SQRT expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression PLUS expression
               | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_num(p):
    '''
    expression : INT
               | FLOAT
    '''
    p[0] = p[1]

def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])

def p_expression_uminus(p):
    '''
    expression : MINUS expression %prec UMINUS
    '''
    p[0] = ('-', p[2])

def p_error(p):
    print(f'Syntax error: {p}')

def p_empty(p):
    '''
    empty : 
    '''
    passs

parser = yacc.yacc()