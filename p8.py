associative_law( A,B,C,Result1,Result2) :-
Result is A+(B+C),
Result is (A+B)+C.

expression1(2,3,4).
expression2(5,6,7).

derive_results :-
expression1(A,B,C),
associative_law(A,B,C,Result1A,Result1A),
expression2(X,Y,Z),
associative_law(A,B,C,Result1B,Result2B),
write('Result of expression 1 using associative law:'),nl,
write('A+(B+C)='),write(Result1A), nl,
write('(A+B)+C='),write(Result2A), nl,
write('Result of Expresion 2 using associative law:'),nl,
write('X+(Y+Z)='),write(Result1B), nl,
write('(X+Y)+Z='),write(Result2B), nl.

associative_law( A,B,C,Result1,Result2) :-
Result is A+(B+C),
Result is (A+B)+C.

expression1(2,3,4).
expression2(5,6,7).

derive_results :-
expression1(A,B,C),
associative_law(A,B,C,Result1A,Result1A),
expression2(X,Y,Z),
associative_law(A,B,C,Result1B,Result2B),
write('Result of expression 1 using associative law:'),nl,
write('A+(B+C)='),write(Result1A), nl,
write('(A+B)+C='),write(Result2A), nl,
write('Result of Expresion 2 using associative law:'),nl,
write('X+(Y+Z)='),write(Result1B), nl,
write('(X+Y)+Z='),write(Result2B), nl.
