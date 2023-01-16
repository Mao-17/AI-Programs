:- set_prolog_flag(stack_limit, 2_147_483_648).


start:-
    consult('dfs.pl'),nl,
    consult('bfs.pl'),nl,
    printmsg,
    import_roaddistance,
    choose_search.


printmsg:-
    write("----------------------------------------------------------------------"),nl,
    write("Welcome to Road Route Planner System"),nl,
    write("----------------------------------------------------------------------"),nl.


import_roaddistance :-
            csv_read_file('roaddistance.csv' ,R, [functor(give_Distance), arity(3)]),
            maplist(assert, R).

choose_search :-
                write("Choose whether you want to use the dfs or bfs search - (dfs/bfs)."),
                nl,
                read(Ans),
                Ans=bfs -> bfs_search ; dfs_search.