# enter the set of states in this list as strings
set_of_states_Q = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
# enter set of final states in the list below as stings
set_of_final_states_F = ['q3', 'q4', 'q5']
# enter the starting state below
start_state = "q0"
# enter the dfa data below:
DFA_table = {'q0':{'a':'q1','b':'q2'},      
             'q1':{'a':'q3','b':'q4'},
             'q2':{'a':'q3','b':'q5'},              
             'q3':{'a':'q3','b':'q1'},
             'q4':{'a':'q4','b':'q5'},
             'q5':{'a':'q5','b':'q4'},
             'q6':{'a':'q2','b':'q6'},
                     }