import collections
import re

def lexicalAnalyzer(myString):
    myString = myString.lower()     # case-insensitive -> turns input into lowercase

    keywords = {'if', 'then', 'end if', 'else', 'for', 'read', 'print', 'while', 'end while', 'and', 'or'}
    token_specification = [
        ('TYPE', r'int|float|boolean'),
        ('NUMBER',  r'\d+(\.\d*)?'),                # Integer or decimal number
        ('ASSIGN',  r'='),                          # Assignment operator
        ('END',     r';|end (if|while);'),           # Statement terminator
        ('ID',      r'[A-Za-z0-9]+'),               # Identifiers
        ('OP',      r'[+\-*/]'),                    # Arithmetic operators
        ('NEWLINE', r'\n'),                         # Line endings
        ('SKIP',    r'[ \t]+'),                     # Skip over spaces and tabs
        ('SYNTAX', r'[\(\){}><:]'),                 # syntax
        ('MISMATCH',r'.'),                          # Any other character

    ]
    simple_table = []
    nextToken = ""
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    for match in re.finditer(tok_regex, myString):
        kind = match.lastgroup
        value = match.group(kind)
        if kind == 'NEWLINE':
            pass
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value} unexpected!!')
        else:
            if kind == 'ID':
                if  value in keywords:
                    kind = value
                else:   # add user-defined token into symbol table
                    simple_table.append(value)

            nextToken = kind
            print(f'Token: {value} \t\t Token Type: {kind} \t\t nextToken: {nextToken}')

    print(f' user-defined tokens: {simple_table}')

# lexicalAnalyzer("total = Subtotal1 * 12;")
# lexicalAnalyzer("print (x+y)")

# statements = '''
#     total = subtotal1 * 12;
# '''

statements = '''
    if 5>1:
        {
            if (4>3) and (2 <5) :
                {
                    print 1;
                    print 2;
                }
            else:
                {
                    print (3+1)
                }
            end if;
        }
    end if;
'''


lexicalAnalyzer(statements)


# statements = '''
#     IF quantity THEN
#         total = total + price * quantity;
#         tax = price * 0.05;
#     ENDIF;
# '''
# lexicalAnalyzer(statements)
