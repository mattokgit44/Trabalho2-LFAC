import sys

def is_accepting(state,accept_states):
    return state in accept_states

def process_input(input_string, states, input_alphabet, stack_alphabet, transitions, start_state, start_symbol, accept_states):
    stack = [start_symbol]
    state = start_state

    print(stack)

    for char in input_string:
        current_symbol = stack[-1]
        print(state, char, current_symbol)
        if (state, char, current_symbol) in transitions:
            new_state, new_symbol = transitions[(state, char, current_symbol)]
            stack.pop()
            print(new_state, new_symbol)

            if new_symbol != 'epsilon':
                stack.extend(list(new_symbol))

            state = new_state
        else:
            return False
    return is_accepting(state, accept_states) and len(stack) == 1 and stack[0] == start_symbol
if __name__ == "__main__":

    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 
              'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 
              'q12', 'q13', 'q14', 'q15', 'q16', 
              'q17', 'q18', 'q19', 'q20', 'q21', 
              'q22', 'q23', 'q24'}
    
    input_alphabet = {'(', ')', '*', '+', '-', '/',
                       '=', 'd', 'i', 'm', 'n', 'u',
                        '$', 'E', 'F', 'S', 'T', 'V'}
    
    stack_alphabet = {'0', '1', '2', '3', '4', '5', '6', 
                      '7', '8', '9', '10', '11', '12', 
                      '13', '14', '15', '16', '17', '18', 
                      '19', '21', '22', '23', '24', '(', 
                      ')', '*', '+', '-', '/', '=', 'd', 
                      'i', 'm', 'n', 'u', '$', 'E', 'F', 
                      'S', 'T', 'V'}
    
    transitions = {('q0', '(', '0'): ('q1', '1('),
                   ('q0', 'i', '0'): ('q7', '7i'),
                   ('q0', 'n', '0'): ('q8', '8n'),
                   ('q0', 'E', '0'): ('q2', '2E'),
                   ('q0', 'F', '0'): ('q3', '3F'),
                   ('q0', 'S', '0'): ('q4', '4S'),
                   ('q0', 'T', '0'): ('q5', '5T'),
                   ('q0', 'V', '0'): ('q6', '6V'),
                   ('q1', '(', '1'): ('q1', '1('),
                   ('q0', 'b', 'A'): ('q1', 'epsilon'),
                   ('q1', 'b', 'A'): ('q1', 'epsilon'),
                   ('q1', 'epsilon', '$'): ('q1', 'epsilon')}
    start_state = 'q0'
    start_symbol = '0'
    accept_states = {'q2', 'q3', 'q4', 'q5', 'q6', 'q10', 'q16', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24'}

    if len(sys.argv) < 2:
        raise IOError("Use "+sys.argv[0] + " file.exp")
    else:
        aux = sys.argv[1].split('.')
        if aux[-1] != 'exp':
            raise IOError("Not a .exp file!")
        data = open(sys.argv[1])

        input_string = data.read()
        input_string = input_string.strip()

    print('Testing:', input_string)
    if process_input(input_string, states, input_alphabet, stack_alphabet, transitions, start_state, start_symbol, accept_states):
        print("Accepted")
    else:
        print("Rejected")