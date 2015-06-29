# Problem solving algorithm

01. Let EQ represent a list of the equations of interest. Let v(EQ) 
    represent the variables in the equations of EQ.
02. Parse the question to identify all VOI (variables of interest).
03. [Optional] Identify the context of the problem.
04. Filter equation set to include only those equations with variables
    consistent with the list of VOI.
05. Calculate v(EQ). Remove the VOI. Return to step 2 if non-empty.
06. If the number of equations in EQ is greater than one, use context to 
    break the tie.
07. Verify context of the remaining equation. If this doesn't check, start 
    over --- something is seriously wrong!
08. Parse the question to identify the unknown and record the given data,
    whether explicit or implicit. 
09. Solve it and prosper!
