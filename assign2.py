# CODE TO MINIMIZE A GIVEN DFA 
'''The input is taken in following way:
    -> All states are represented using strings ex : "A", "B"
    -> The set of alphabet(sigma) contain values "a","b" by default 
    -> The set of all states is stored in a list format:
            set_of_states_Q = ["A","B","C"] 
    -> The set of Final state(s)  is also stored in similar list format
    -> Starting state is a string which belongs to set of states(Q) [Here we have assumed that a dfa 
                                                                        can have only one starting state]
    -> The DFA table is stored in a dictionary format which is as follows:
         DFA_Table = {state: {"a": output_state(for alphabet(a)), "b": output_state(for alphabet b) }}
         for ex:
            DFA_table = {'A':{'a':'B','b':'C'},      
                         'B':{'a':'D','b':'E'},
                         'C':{'a':'D','b':'F'},              
                         'D':{'a':'D','b':'B'},
                         'E':{'a':'E','b':'F'},
                         'F':{'a':'F','b':'E'},
                         'G':{'a':'C','b':'G'},
                            }
             '''

def input_data():
    print('Write the set of states with space between each space: ')
    strng_of_set_of_states = input('here: ')
    set_of_states_Q = []
    set_of_final_states_F = []
    for a in strng_of_set_of_states.split():
        set_of_states_Q.append(a)
    print()
    print('Provide the set of final states: ')
    strng_of_set_of_final_states = input('here: ')
    for a in strng_of_set_of_final_states.split():
        set_of_final_states_F.append(a)
    print()
    print('provide the starting state:  ')
    starting_state = input('here: ')
    print()
    print('Provide the data of DFA table: ')
    strng_DFA_table = input('here: ')
    x = strng_DFA_table.split()
    DFA_table = {}
    curr_key = 0
    for a in range(len(x)):
        if a%3 == 0:
            curr_key = a
            DFA_table[x[a]] = {}
        elif a%3 == 1:
            DFA_table[x[curr_key]]['a']= x[a]
        elif a%3 == 2:
            DFA_table[x[curr_key]]['b']=x[a]
    return DFA_table, starting_state, set_of_states_Q, set_of_final_states_F
'''The above Function(input_data())
    takes data from the user and create everytjing in format specified earlier.
    Procedure to provide data:
        let these be the dummy values we want to put: 
                set_of_states_Q = ['A','B','C','D','E','F','G']
                set_of_final_states_F = ['D','E','F']
                start_state = "A"
        then when function asks for say set_of_states the input should be:  A B C D E F ...
        simialarly we have to do for set of final states and Start state
    Procedure to provide DFA table data:
        let the dummy DFA tabel we want to input is following
                DFA_table = {'A':{'a':'B','b':'C'},      
                             'B':{'a':'D','b':'E'},
                             'C':{'a':'D','b':'F'},              
                             'D':{'a':'D','b':'B'},
                             'E':{'a':'E','b':'F'},
                             'F':{'a':'F','b':'E'},
                             'G':{'a':'C','b':'G'},
                                }
            the input should be provided as: A B C B D E.... The format is like this:
                                                            [(state1) (where we reach after reading symbol "a" from state1) (where we reach after reading symbol "b" from state1)]
        
'''
# transition_function takes state, and alphabet and returns output state
# if alphabet is not provided the function returns a list of output states for each symbol "a" and "b" in same order
def transition_function(state, alphabet=None):
    global DFA_table
    if alphabet == None:
        value_for_all_alphabet = DFA_table[state]
        return value_for_all_alphabet
    else:
        specific_alphabet_value = DFA_table[state][alphabet]
        return specific_alphabet_value

# The traversing function is a recurrsive function which takes starting state as input
# and updares a dummy  list (ls) with all states that are reachable(That means traveling each and every connected input output line in DFA graph) 
ls = []
def traversing(state):
    global DFA_table
    global ls
    if state not in ls:
        ls.append(state)
        curr_state = transition_function(state, alphabet='a' )
        output_state = traversing(curr_state)
        curr_state = transition_function(state, alphabet='b')
        output_state = traversing(curr_state)
    if state in ls:
        return

# The remove_unreachable_state() function calls the traversing() function and then uses the update list of reachable states 
# to remove unreachable states  
def remove_unreachable_state():
    global DFA_table
    global ls
    global set_of_states_Q
    global start_state
    traversing(start_state)
    list_reachable_state = ls
    for a in set_of_states_Q:
        if a not in list_reachable_state:
            del DFA_table[a]
            del set_of_states_Q[set_of_states_Q.index(a)]
    return DFA_table


def minimizing_dfa(dfa, set_of_final_states_F, set_of_states_Q):
    equivalane_classes = {}
    set_of_nonfinal_states = [a for a in set_of_states_Q if a not in set_of_final_states_F]
    equivalane_classes[0] = []
    equivalane_classes[0].append(set_of_nonfinal_states)
    equivalane_classes[0].append(set_of_final_states_F)
    num = 0
    while True:
        num+=1
        if  num >= 2 and equivalane_classes[num-1] == equivalane_classes[num-2]:
            return equivalane_classes
            break
        else:
            equivalane_classes[num]= []
            new_sets = []
            for a in equivalane_classes[num-1]:
                dummy_list = a.copy()
                pointer2 = 1
                print(equivalane_classes)
                while len(dummy_list)!=0:
                    print(dummy_list, 'dummy_list')
                    print('pointer2', pointer2)
                    if len(dummy_list)>1:
                        pointer1 = 0
                        equivalance = False
                        equivalance_0 = False
                        output1 = transition_function(dummy_list[pointer1],alphabet="a")
                        output2 = transition_function(dummy_list[pointer2],alphabet="a")
                        if output1 != output2:
                            for value in equivalane_classes[num -1]:
                                if output1 in value and output2 in value:
                                    equivalance_0 = True
                            if equivalance_0 == True:
                                output1 = transition_function(dummy_list[pointer1],alphabet="b")
                                output2 = transition_function(dummy_list[pointer2],alphabet="b")
                                if output1 != output2:
                                    for value in equivalane_classes[num -1]:
                                        if output1 in value and output2 in value:
                                            equivalance = True
                                    if equivalance == True:
                                        if len(new_sets) == 0:
                                            new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                            if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                            else:   del dummy_list[pointer2]
                                        else:
                                            pointer1_value_exist = False
                                            for a in new_sets:
                                                if dummy_list[pointer1] in a:
                                                    pointer2_value_exist = True
                                                    a.append(dummy_list[pointer2])
                                                    if pointer2 == len(dummy_list)-1:
                                                        pointer2 = 1
                                                        del dummy_list[pointer1]
                                                        del dummy_list[pointer2-1]
                                                    else: del dummy_list[pointer2]
                                            if pointer1_value_exist == False:
                                                new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                                if pointer2 == len(dummy_list)-1:
                                                    pointer2 = 1
                                                    del dummy_list[pointer1]
                                                    del dummy_list[pointer2-1]
                                                else: del dummy_list[pointer2]
                                    elif equivalance == False:
                                        if pointer2 < len(dummy_list)-1:
                                            pointer2+=1
                                        elif pointer2 == len(dummy_list)-1:
                                            pointer2 = 1
                                            new_sets.append([dummy_list[pointer1]])
                                            del dummy_list[pointer1]
                                        
                                elif output1 == output2:
                                    if len(new_sets) == 0:
                                            new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                            if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                            else: del dummy_list[pointer2]
                                    else:
                                        pointer1_value_exist = False
                                        for a in new_sets:
                                            if dummy_list[pointer1] in a:
                                                pointer1_value_exist = True
                                                a.append(dummy_list[pointer2])
                                                if pointer2 == len(dummy_list)-1:
                                                    pointer2 = 1
                                                    del dummy_list[pointer1]
                                                    del dummy_list[pointer2-1]
                                                else: del dummy_list[pointer2]
                                        if pointer1_value_exist == False:
                                            new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                            if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                            else: del dummy_list[pointer2]
                            elif equivalance_0 == False:
                                if pointer2 < len(dummy_list)-1:
                                    pointer2+=1
                                elif pointer2 == len(dummy_list)-1:
                                    pointer2 = 1
                                    new_sets.append([dummy_list[pointer1]])
                                    del dummy_list[pointer1]
                        elif output1 == output2:
                            output1 = transition_function(dummy_list[pointer1],alphabet="b")
                            output2 = transition_function(dummy_list[pointer2],alphabet="b")
                            if output1 != output2:
                                for value in equivalane_classes[num -1]:
                                    if output1 in value and output2 in value:
                                        equivalance = True
                                if equivalance == True:
                                    if len(new_sets) == 0:
                                        new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                        if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                        else: del dummy_list[pointer2]
                                    else:
                                        pointer1_value_exist = False
                                        for a in new_sets:
                                            if dummy_list[pointer1] in a:
                                                pointer1_value_exist = True
                                                a.append(dummy_list[pointer2])
                                                if pointer2 == len(dummy_list)-1:
                                                    pointer2 = 1
                                                    del dummy_list[pointer1]
                                                    del dummy_list[pointer2-1]
                                                else: del dummy_list[pointer2]
                                        if pointer1_value_exist == False:
                                            new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                            if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                            else:
                                                del dummy_list[pointer2]
                                        
                                elif equivalance == False:
                                    if pointer2 < len(dummy_list)-1:
                                        pointer2+=1
                                    elif pointer2 == len(dummy_list)-1:
                                        pointer2 = 1
                                        new_sets.append([dummy_list[pointer1]])
                                        del dummy_list[pointer1]
                                        
                            elif output1 == output2:
                                if len(new_sets) == 0:
                                    new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                    if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                    else:   del dummy_list[pointer2]
                                else:
                                    pointer1_value_exist = False
                                    for a in new_sets:
                                        if dummy_list[pointer1] in a:
                                            pointer1_value_exist = True
                                            a.append(dummy_list[pointer2])
                                            if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                            else:
                                                del dummy_list[pointer2]
                                    if pointer1_value_exist == False:
                                        new_sets.append([dummy_list[pointer1], dummy_list[pointer2]])
                                        if pointer2 == len(dummy_list)-1:
                                                pointer2 = 1
                                                del dummy_list[pointer1]
                                                del dummy_list[pointer2-1]
                                        else:   del dummy_list[pointer2]
                    elif len(dummy_list)==1:
                        valueexists = False
                        for a in new_sets:
                            if dummy_list[0] in a:
                                valueexists = True
                        if valueexists == False:
                            new_sets.append([dummy_list[0]])
                            del dummy_list[0]
                        else:
                            del dummy_list[0]
            for a in new_sets:
                equivalane_classes[num].append(a)
    return equivalane_classes
def create_dfa_table(equivalance_classes):
    global set_of_final_states_F
    global DFA_table
    global start_state
    new_set_minimum_states = equivalance_classes[len(equivalance_classes)-1].copy()
    set_of_final_new_states_F = []
    new_start_state = ""
    for a in new_set_minimum_states:
        for b in set_of_final_states_F:
            if b in a:
                a_already_there = False
                for x in set_of_final_new_states_F:
                    if a == x:
                        a_already_there = True
                if a_already_there == False:
                    set_of_final_new_states_F.append(list_to_string(a))
            if start_state in a and start_state not in new_start_state:
                new_start_state+= list_to_string(a)
    minimized_DFA_table = {}
    for a in new_set_minimum_states:
        minimized_DFA_table[list_to_string(a)] = {}
        output_a = transition_function(a[0], alphabet="a")
        output_b = transition_function(a[0], alphabet="b")
        for b in new_set_minimum_states:
            if output_a in b:
                minimized_DFA_table[list_to_string(a)]['a'] = list_to_string(b)
        for b in new_set_minimum_states:
            if output_b in b:
                minimized_DFA_table[list_to_string(a)]['b'] = list_to_string(b)
    
        
    return minimized_DFA_table, set_of_final_new_states_F, new_set_minimum_states, new_start_state
#helper functions:
def list_to_string(list):
    strng = ""
    strng+="{"
    for a in list:
        if list.index(a) != len(list)-1:
            strng+= str(a)
            strng+= ","
        else:
            strng+= str(a)
    strng+= "}"
    return strng
def print_dictionary(dict):
    for a,b in dict.items():
        print(a," : ", b)
def input_data():
    print('Write the set of states with space between each space: ')
    strng_of_set_of_states = input('here: ')
    set_of_states_Q = []
    set_of_final_states_F = []
    for a in strng_of_set_of_states.split():
        set_of_states_Q.append(a)
    print()
    print('Provide the set of final states: ')
    strng_of_set_of_final_states = input('here: ')
    for a in strng_of_set_of_final_states.split():
        set_of_final_states_F.append(a)
    print()
    print('provide the starting state:  ')
    starting_state = input('here: ')
    print()
    print('Provide the data of DFA table: ')
    strng_DFA_table = input('here: ')
    x = strng_DFA_table.split()
    DFA_table = {}
    curr_key = 0
    for a in range(len(x)):
        if a%3 == 0:
            curr_key = a
            DFA_table[x[a]] = {}
        elif a%3 == 1:
            DFA_table[x[curr_key]]['a']= x[a]
        elif a%3 == 2:
            DFA_table[x[curr_key]]['b']=x[a]
    return DFA_table, starting_state, set_of_states_Q, set_of_final_states_F
            
DFA_table, start_state, set_of_states_Q, set_of_final_states_F = input_data()
#making things more presentable
print()
print('DFA table given: ')
print_dictionary(DFA_table)
print('------------------------------------------------')
print()
DFA_table = remove_unreachable_state()
print('DFA table with unreachable states removed: ')
print_dictionary(DFA_table)
print('------------------------------------------------')
print()
equivalance_classes= minimizing_dfa(DFA_table, set_of_final_states_F, set_of_states_Q)
print('equivalance classes formed during minimization process:  ')
print_dictionary(equivalance_classes)
print('------------------------------------------------')
print()
print('New DFA table formed after minimization:  ')
a,b,c,d = create_dfa_table(equivalance_classes)
print_dictionary(a)
print('------------------------------------------------')
print()
print('set of all minimized states:')
print(c)
print('------------------------------------------------')
print()
print('Set of new final states:  ')
print(b)
print('------------------------------------------------')
print()
print('Starting state of new dfa', d)
print('------------------------------------------------')
print()
