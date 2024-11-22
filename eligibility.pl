:- use_module(library(csv)).

% Load data from the CSV file into the Prolog database
load_data :-
    csv_read_file('data.csv', Rows, [functor(student), arity(3)]),
    maplist(assert, Rows).

% Scholarship eligibility rule
eligible_for_scholarship(Student_ID) :-
    student(Student_ID, Attendance, CGPA),
    Attendance >= 75,
    CGPA >= 9.0.

% Exam permission rule
permitted_for_exam(Student_ID) :-
    student(Student_ID, Attendance, _),
    Attendance >= 75.



