:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_parameters)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_files)).
:- consult('eligibility.pl').

% Load data on startup
:- initialization(load_data).

% Start the HTTP server
start_server(Port) :-
    http_server(http_dispatch, [port(Port)]).

% Define HTTP handlers
:- http_handler(root(scholarship), check_scholarship, []).
:- http_handler(root(exam), check_exam, []).
:- http_handler(root(.), serve_files, [prefix]).

% Serve static files
serve_files(Request) :-
    http_reply_from_files('.', [], Request).

% Scholarship API endpoint
check_scholarship(Request) :-
    http_parameters(Request, [student_id(Student_ID, [number])]),
    ( eligible_for_scholarship(Student_ID)
      -> Reply = json{student_id: Student_ID, scholarship: "Eligible"}
      ;  Reply = json{student_id: Student_ID, scholarship: "Not Eligible"}
    ),
    reply_json(Reply).

% Exam API endpoint
check_exam(Request) :-
    http_parameters(Request, [student_id(Student_ID, [number])]),
    ( permitted_for_exam(Student_ID)
      -> Reply = json{student_id: Student_ID, exam: "Permitted"}
      ;  Reply = json{student_id: Student_ID, exam: "Not Permitted"}
    ),
    reply_json(Reply).
