# Problem solving algorithm

- Let `EQ` represent a list of the equations of interest.
- Let `v(EQ)` represent the variables in the equations of EQ.

01. Parse the question to identify all VOI (variables of interest).
02. [Optional] Identify the context of the problem.
03. Filter equation set to include only those equations with variables
    consistent with the list of VOI.
04. Calculate v(EQ). Remove the VOI. Return to step 1 if non-empty.
05. If the number of equations in EQ is greater than one, use context to 
    break the tie.
06. Verify context of the remaining equation. If this doesn't work, start 
    over --- something is seriously wrong!
07. Parse the question to identify the unknown and record the given data,
    whether explicit or implicit. 
08. Solve it and prosper!