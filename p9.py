% Define relationships
batsman(sachin).
wk(dhoni).
footballer(ronaldo).

% Define general rules
cricketer(X) :- batsman(X).
cricketer(X) :- wk(X).
not_cricketer(X) :- footballer(X).
