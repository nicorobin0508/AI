% Facts: Define males and females in the family
male(john).
male(mike).
male(david).
male(james).
male(kevin).
male(sam).

female(susan).
female(lisa).
female(mary).
female(emma).
female(jane).
female(lucy).

% Facts: Define parent relationships
parent(john, mike).   % john is the parent of mike
parent(john, lisa).
parent(mary, mike).
parent(mary, lisa).
parent(mike, david).
parent(mike, emma).
parent(susan, david).
parent(susan, emma).
parent(lisa, sam).
parent(lisa, lucy).
parent(james, sam).
parent(james, lucy).

% Rules: Family relationships

% Father: A father is a male parent
father(X, Y) :- male(X), parent(X, Y).

% Mother: A mother is a female parent
mother(X, Y) :- female(X), parent(X, Y).

% Grandfather: A grandfather is a male parent of a parent
grandfather(X, Y) :- male(X), parent(X, Z), parent(Z, Y).

% Grandmother: A grandmother is a female parent of a parent
grandmother(X, Y) :- female(X), parent(X, Z), parent(Z, Y).

% Brother: A brother is a male sibling
brother(X, Y) :- male(X), parent(Z, X), parent(Z, Y), X \= Y.

% Sister: A sister is a female sibling
sister(X, Y) :- female(X), parent(Z, X), parent(Z, Y), X \= Y.

% Uncle: An uncle is a male sibling of a parent
uncle(X, Y) :- male(X), brother(X, Z), parent(Z, Y).

% Aunt: An aunt is a female sibling of a parent
aunt(X, Y) :- female(X), sister(X, Z), parent(Z, Y).

% Nephew: A nephew is a male child of a sibling
nephew(X, Y) :- male(X), parent(Z, X), (brother(Z, Y); sister(Z, Y)).

% Niece: A niece is a female child of a sibling
niece(X, Y) :- female(X), parent(Z, X), (brother(Z, Y); sister(Z, Y)).

% Cousin: A cousin is a child of a parent's sibling
cousin(X, Y) :- parent(Z, X), (brother(Z, W); sister(Z, W)), parent(W, Y).
