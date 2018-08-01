def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    # basic case 
    if not (states or days) or len(states) == 0 or type(days) != int:
        return False
    while days > 0:
        next_states = [0 for x in range(len(states))]
        states = [0] + states + [0]
        for pos in xrange(1, len(states)-1):
            if states[pos-1] == states[pos+1]:
                next_states[pos-1] = 0
            else:
                next_states[pos-1] = 1
        states = next_states
        days -= 1 
    print states