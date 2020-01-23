from ply import lex

tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'POWER',
    'SQRT',
    'LPAREN',   
    'RPAREN',
    'ASSIGN',
    'PI',
    'EXP',
    'E',
]

t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_POWER = r'\^'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ASSIGN = r'\='

t_SQRT = r'sqrt'
t_PI = r'pi'
t_EXP = r'exp'
t_E = r'e'

t_ignore = r' '

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print(f'Illegal character: {t.value}')
    t.lexer.skip(1)

lexer = lex.lex()