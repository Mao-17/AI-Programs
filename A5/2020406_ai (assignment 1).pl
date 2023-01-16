electiveguide :-
    reset_system,
    consult('C:/Users/shiva/Downloads/AI-A5-Shivamgupta-2020406/ai_a5.txt'),
    recommend_electives,
    convert_to_list(Electives),nl,
    write('Below is the list of recommended electives for you based on your interests/choices'),nl,
    write(Electives).

:-dynamic(skills/1).
:-dynamic(branch/1).
:-dynamic(likes/1).
:-dynamic(cgpa/1).
:-dynamic(knows_language/1).
:-dynamic(courses_completed_curr/1).

reset_system :-
    retractall(skills(_)),
    retractall(branch(_)),
    retractall(cgpa(_)),
    retractall(knows_language),
    retractall(courses_completed_curr(_)),
    retractall(likes(_)),
    retractall(publishedresearchpapers(_)),
    retractall(researchpapers(_)),
    fail.
reset_system.

convert_to_list([Car|Tail]):-
    retract(recommended(Car)),
    convert_to_list(Tail).

convert_to_list([]).

/*different types of elective options*/

recommend_electives:-
    skills(maths),
    knows_language(python),
    courses_completed_curr(la),
    courses_completed_curr(pns),
    courses_completed_curr(multivariate_calculus),
    cgpa(M),
    M >= 7.5,
    likes(ml),
    likes(data),
    branch(1),
    assert(recommended(machine_learning)),
    fail.

recommend_electives:-
    skills(maths),
    knows_language(java),
    skills(programming),
    knows_language(c_plus_plus),
    courses_completed_curr(dsa),
    cgpa(M),
    M >= 8.0,
    likes(algorithms),
    branch(1),
    assert(recommended(advanced_algorithms)),
    fail.

recommend_electives:-
    likes(network_systems),
    likes(operating_systems),
    branch(1),
    assert(recommended(mobile_computing)),
    fail.    

recommend_electives:-
    skills(statistics),
    skills(maths),
    likes(data),
    courses_completed_curr(dbms),
    knows_language(mysql),
    knows_language(unix),
    branch(1),
    assert(recommended(big_data_analytics)),
    fail.

recommend_electives:-
    likes(network_systems),
    branch(1),
    assert(recommended(network_anonymity_and_privacy)),
    fail.       

recommend_electives:-
    skills(maths),
    knows_language(python),
    courses_completed_curr(la),
    courses_completed_curr(pns),
    courses_completed_curr(multivariate_calculus),
    cgpa(M),
    M >= 7.5,
    likes(ml),
    likes(data),
    branch(2),
    assert(recommended(machine_learning)),
    fail.

recommend_electives:-
    skills(maths),
    knows_language(matlab),
    courses_completed_curr(pns),
    likes(network_systems),
    likes(data),
    branch(2),
    assert(recommended(modeling_and_ananlysis_of_random_5g_networks)),
    fail.    

recommend_electives:-
    skills(maths),
    courses_completed_curr(principles_of_communication_systems),
    courses_completed_curr(la),
    cgpa(M),
    M >= 6,
    branch(2),
    assert(recommended(probability_and_random_processes)),
    fail.

recommend_electives:-
    skills(maths),
    skills(statistics),
    knows_language(matlab),
    courses_completed_curr(la),
    courses_completed_curr(pns),
    courses_completed_curr(signals_and_systems),
    branch(2),
    assert(recommended(statistical_signal_processing)),
    fail.        

recommend_electives:-
    skills(maths),
    skills(python),
    courses_completed_curr(signals_and_systems),
    branch(2),
    assert(recommended(digital_signal_processing)),
    fail.

recommend_electives:-
    skills(maths),
    knows_language(python),
    skills(statistics),
    cgpa(M),
    M >= 6.5,
    likes(ml),
    likes(data),
    branch(3),
    assert(recommended(machine_learning_for_bio_medical_applications)),
    fail.

recommend_electives:-
    cgpa(M),
    M >= 6.0,
    likes(data),
    branch(3),
    assert(recommended(data_sciences_in_genomics)),
    fail.

recommend_electives:-
    skills(maths),
    skills(statistics),
    skills(programming),
    branch(3),
    assert(recommended(big_data_mining_in_healthcare)),
    fail.

recommend_electives:-
    skills(maths),
    skills(statistics),
    skills(programming),
    likes(network_systems),
    likes(data),
    branch(3),
    assert(recommended(network_science)),
    fail.

recommend_electives:-
    nl,nl,write('Thank you for your responses!!'),nl,nl.