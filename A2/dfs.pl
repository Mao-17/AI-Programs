% solving with the depth first search algorithm

dfs_search :-
            !,
                writeln("Selected Depth First Search"),
                write("Please Enter Starting City: "),nl,
                read(Start_city),
                write("Please Enter Destination City: "),nl,
                read(Dest_city),
                solve_dfs(Start_city, Dest_city).

solve_dfs(Start_city,Dest_city) :-
               write("Path: "), nl,
               dfs([], Start_city, Dest_city,Solution),
               reverse(Solution,Path),
               print_dfs_path(Path),nl,
               write("Cost:  "),
               find_cost(Path,Best_cost),
               write(Best_cost), nl ,!.

dfs(Path, Node, Node, [Node|Path]).

dfs(Path, Start_city, Dest_city, Sol) :-
                check_edge(Start_city, New_city),
                dif(Dest_city, Start_city),
                not(check_member(New_city, Path)),
                dfs([Start_city|Path],New_city, Dest_city, Sol).

print_dfs_path([]).

print_dfs_path([Current_city|Remaining]) :-
                 write(Current_city), nl,
                 print_dfs_path(Remaining).