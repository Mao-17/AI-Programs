% solving with the breadth first search algorithm

bfs_search :-
                !,
                writeln("Selected Breadth First Search"),
                write("Please Enter Starting City: "),nl,
                read(Start_city),
                write("Please Enter Destination City: "),nl,
                read(Dest_city),
                solve_bfs(Start_city, Dest_city).




solve_bfs(Start_city,Dest_city):-
                    get_heuristic(Start_city,Dest_city, H_val),
                    vertex(Start_city, nil, H_val, Current_city),
                    Finished=[],
                    pq_insert(Current_city, [] ,Started ),
                    bfs(Started, Finished, Dest_city).



bfs(Started,_,_) :-
                                  Started = [],
                                  write("Destination city cannot be reached from the starting city.").

bfs(Started, Finished, Dest_city) :- 
                                                delete_priority_queue(Current_vertex, Started,_),
                                                vertex(State, _, _,Current_vertex),
                                                State = Dest_city,
                                                write("Path: "),nl,
                                                print_bfs_path(Current_vertex,Finished,Path),
                                                write("Cost:  "),
                                                find_cost(Path,Best_cost),
                                                write(Best_cost), nl.

bfs(Started, Finished, Dest_city):-
                                                delete_priority_queue(Current_vertex, Started, Rest_of_started),
                                                findall(Child,new_cities(Current_vertex,Started, Finished, Child, Dest_city), Childvertices),
                                                insert_list_to_queue(Childvertices,Rest_of_started,New_started),
                                                add_to_finished(Current_vertex, Finished, New_finished),
                                                bfs(New_started, New_finished, Dest_city),!.



print_bfs_path(Next_vertex, _,[State]):-
                                  vertex(State, nil,_, Next_vertex),
                                  write(State),nl.

print_bfs_path(Next_vertex, Finished, [State|Rem]):-
                                  vertex(State, Current_vertex, _, Next_vertex),
                                  vertex(Current_vertex, _,_, Record_vertex),
                                  check_member(Record_vertex, Finished),
                                  print_bfs_path(Record_vertex, Finished, Rem),
                                  write(State),nl.


get_heuristic(Start,_,End):-findall(Y,give_Distance(Start,_,Y),Bag), min_list(Bag,End).

vertex(Startnode, Parent_node, H_val , [Startnode,Parent_node,H_val]).

pq_insert(Startnode, [First|Rem], [First|Rem_new]):-pq_insert(Startnode, Rem, Rem_new).
pq_insert(Startnode,[First|Rem],[Startnode,First|Rem]):-pq_insert_order(Startnode,First).
pq_insert(Startnode, [], [Startnode]).
pq_insert_order([_,_,AA], [_,_,BB]) :- AA =< BB.

find_cost([],0).
find_cost([_],0).
find_cost([Start,Next|Rem],Cost):-
                   find_cost([Next|Rem],C1),
                   give_Distance(Start,Next,C2),
                   Cost is C1 + C2.

check_member(Head, [Next|Rem]):-
                    dif(Head,Next),
                    check_member(Head,Rem).



check_member(Head, [Head|_]).

check_memberpq(A,B) :- member(A,B).


check_edge(A,B) :- give_Distance(A,B,_).

delete_priority_queue(Begin, [Begin|Rem], Rem).


insert_list_to_queue([State | Tail], Ros, New_started) :- pq_insert(State, Ros, Ros2), insert_list_to_queue(Tail, Ros2, New_started).
insert_list_to_queue([], Ros, Ros).

add_to_finished(Head1, [Head|T1], [Head|T2]):- add_to_finished(Head1, T1,T2).
add_to_finished(Head, [Head|T], [Head|T]).
add_to_finished(Head, [], [Head]).


new_cities(Current_vertex, Started, Finished, Child, Dest_city):-
                                                       vertex(State, _,_,Current_vertex),
                                                       check_edge(State,Next_vertex),
                                                       vertex(Next_vertex, _, _,Check),
                                                       not(check_memberpq(Check,Started)),
                                                       not(check_member(Check, Finished)),
                                                       get_heuristic(Next_vertex, Dest_city, H_val),
                                                       vertex(Next_vertex, State, H_val, Child).