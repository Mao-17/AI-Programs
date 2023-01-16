electiveguide :-
    reset_system,
    intro(Name),
    get_interests,
    recommend_electives,
    convert_to_list(Electives),nl,
    write('Below is the list of recommended electives for you ' ),write(Name),write(' based on your interests/choices'),nl,
    display(Electives).

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

intro(Name):-
    write('Welcome to IIIT DELHI M.Tech Electives Advisory System!'),nl,
    write('I will help you find the best electives you can choose based on your interest areas and a few other important factors'),nl,
    write('For each question enter your answer followed by a full stop(.)'),nl,nl,
    write('Please enter your name, followed by a full stop: '),
    read(Name),
    nl,
    write('Hello,  '),
    write(Name),write('!'),nl.

get_interests:- 
    know_branch,
    know_cgpa,
    know_programming,
    courses_completed,
    know_maths,
    know_statistics,
    likes_ml,
    likes_data,
    likes_complex_algoithms,
    likes_ns,
    likes_os,
    likes_higherstudies,
    likes_research,
    published_research.
    

/*getting all the information about the students interests*/

know_branch:-
        write('Select your branch from the following:\n'),
        write(
              '1.CSE\n
               2.ECE\n
               3.CSB\n'),
               write('Select the number(1 to 3): '),
               read(B), assert(branch(B)).

branch(1):- write('\nThese are the available electives to choose from:
                         1.Mobile Computing.\n
                         2.Advanced Algorithms.\n
                         3.Machine Learning.\n
                         4.Big Data Analytics.\n
                         5.Network Anonymity and Privacy.\n'),nl.

branch(2):- write('\nThese are the available electives to choose from:
                         1.Probability and Random Process.\n
                         2.Modeling and Analysis of Random 5G Networks.\n
                         3.Statistical Signal Processing.\n
                         4.Digital Signal Processing.\n
                         5.Machine Learning.\n'),nl.

branch(3):- write('\nThese are the available electives to choose from:
                         1.Machine Learning for Bio medical Applications.\n
                         2.Datascience for genomics.\n
                         3.Big data mining in healthcare.\n
                         4.Network science.\n'),nl.
                                          
branch(B):- B > 3, write('\nLet us start again!'), intro(Name),nl.               

know_cgpa:-
    write('Please enter your CGPA '),
    read(CGPA),
    assert(cgpa(CGPA)).

know_programming:-
    write('Do you have good programming skills '),
    read(Y),
    Y == y,
    assert(skills(programming)),
    write('Do you know the following languages? '),
    nl,
    append([c_plus_plus,c,python,java,mysql,unix,matlab],[],List),
    get_languages(List).

know_programming.

get_languages([H|T]):-
    write('Do you know '),
    write(H),
    write('? '),
    read(Y),
    Y == y -> assert(knows_language(H)),get_languages(T);
    get_languages(T).

get_languages([]).

courses_completed:-
    write('I would now ask you about the courses you have currenty done to check the pre-requisite conditions'),
    nl,
    append([dsa,la,pns,multivariate_calculus,dbms,principles_of_communication_systems,signals_and_systems],[],List),
    get_current_courses(List).

courses_completed.

get_current_courses([H|T]):-
    write('Have you done '),
    write(H),
    write('? '),
    read(Y),
    Y == y -> assert(courses_completed_curr(H)),get_current_courses(T);
    get_current_courses(T).

get_current_courses([]).

know_maths:-
    write('Do you have high level knowledge in maths and like doing it? '),
    read(Y),
    Y == y,assert(skills(maths)).

know_maths.

know_statistics:-
    write('Do you have good knowledge in statistics? '),
    read(Y),
    Y == y,assert(skills(statistics)).

know_statistics.

likes_ml:-
    write('Are you interested in Machine learning field?'),
    read(Y),
    Y == y,assert(likes(ml)).

likes_ml.

likes_data:-
    write('Are you interested working with data?'),
    read(Y),
    Y == y,assert(likes(data)).

likes_data.

likes_complex_algoithms:-
    write('Do you like analysing and designing complex algorithms?'),
    read(Y),
    Y == y,assert(likes(algorithms)).

likes_complex_algoithms.

likes_ns:-
    write('Are you interested in network systems?'),
    read(Y),
    Y == y,assert(likes(network_systems)).

likes_ns.

likes_os:-
    write('Are you interested in operating systems?'),
    read(Y),
    Y == y,assert(likes(operating_systems)).

likes_os.

likes_higherstudies:-
    write('Are you interested in higher studies? '),
    read(Y),
    Y == y,assert(interested(higher_studies)).

likes_higherstudies.

likes_research:-
    write('Are you interested in research? '),
    read(Y),
    Y == y,assert(likes(research)).

likes_research.

published_research:-
    write('Have you ever published any research papers? '),
    read(Y),
    Y == y,assert(publishedresearchpapers(yes)),
    how_many_papers.

published_research.

how_many_papers:-
    write('How many papers have you published? '),
    read(Ans),
    assert(researchpapers(Ans)).

/*converting the recommended electives to list*/ 

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

/*display all the recommended Electives*/
display([H|T]):-
    nl,
    write('The elective recommended for you is '),write(H),nl,
    write('     Brief description about the elective '),nl,
    describe(H),nl,nl,
    display(T).

display([]).


/*brief details about the Electives*/

describe(machine_learning):-
    write('This is an introductory course on Machine Learning (ML) that is offered to undergraduate and graduate students. The contents are designed to cover both theoretical and practical aspects of several well-established ML techniques. The assignments will contain theory and programming questions that help strengthen the theoretical foundations as well as learn how to engineer ML solutions to work on simulated and publicly available real datasets. The project(s) will require students to develop a complete Machine Learning solution requiring preprocessing, design of the classifier/regressor, training and validation, testing and evaluation with quantitative performance comparisons.'),nl,nl.

describe(mobile_computing):-
    write('The course prepares and trains the students to program mobile devices with understanding on constaints and opportunites that mobile devices offer. This course will cover challenges in mobile systems. It will also cover latest research in the field of Mobile Computing.'),nl,nl.

describe(advanced_algorithms):-
    write('The purpose of this course is to develop advanced techniques in the design and analysis of algorithms. It will focus on exploring both the breadth of theoritical tools necessary for computer science as well as the depth through analysis of the related data structure and algorithms.When taught as a graduate-level course, the students will be required to write a survey paper. Topics covered in this course include string matching, linear programming, max-flow, min-cut, numerical algorithms (including polynomial operations and FFT), amortized analysis and advanced data structures like Fibonacci heaps, splay trees, steiner trees, skip lists.'),nl,nl.

describe(big_data_analytics):-
    write('Distributed processing frameworks have emerged as a feasible and cost effective way of analyzing the increasing volume of data. This course provides an understanding of most popular distributed processing frameworks – Hadoop, Spark and Giraph. Example Applications will include Graph Analysis algorithms such as BFS, Page Rank, Finding Graph Patterns; Finding Similar Items, Mining Algorithms such as Clustering, Frequent Itemsets, Data Streams. Hands-on exercises will prepare those taking this course to be able to apply these frameworks in practice.'),nl,nl.

describe(network_anonymity_and_privacy):-
    write('Historical network anonymity and privacy protocols - MIXes and MIXnets, various theoretical and practical attack strategies against high and low-latency anonymity networks, practical traffic analysis against modern anonymity systems like Tor, Freenet, GNUnet, JAP, defenses against traffic analysis attacks, performance vs anonymity trade-offs, side-channel attacks, covert channel communications, pseudonymity and privacy, Anonymous P2P communication systems (e.g. Oneswarm), traffic analysis against anonymous VoIP communications, Internet censorship and censorship resistance tools and strategies, large-scale Internet surveillance and anti-surveillance, decoy routing.'),nl,nl.

describe(probability_and_random_processes):-
    write('The course will provide students with an in depth introduction to stochastic processes with applications in electrical engineering. A review of axioms of probability, single and multivariate distributions, and functions of random variables will be followed by study of fundamental theorems like Markovs inequality, Chebyshevs inequality, Chernoffs Bound, weak and strong law of large numbers (convergence in probability and almost sure convergence), mean-squared convergence, convergence in distribution, the central limit theorem, vector random variables, properties of covariance matrices, random processes, stationarity, ergodicity, linear systems with stochastic inputs, autocorrelation and the power spectrum. Along the course we will also look at examples like the Weiner process, Poisson process and Markov Chains.'),nl,nl.

describe(modeling_and_ananlysis_of_random_5g_networks):-
    write('This course will commence with introduction to the tools from stochastic geometry, applied in the context of wireless network modeling. Then, the course will build up on the learned tools to model several features of 5G systems such as mm-wave communication, massive MIMO, ultra dense networks etc. Detailed PHY layer aspects will be translated into simplistic stochastic geometry models, for performing system-level analysis. A notion of performance metrics for the users in modern wireless systems will be developed, e.g., SINR coverage, rate coverage, positioning accuracy, network load etc. The fundamental tractability-accuracy tradeoffs will be discussed while choosing appropriate stochastic geometry tools for modeling 5G networks. Impact of physical layer modeling on the MAC layer protocols will be studied and accordingly, cross-layer algorithms will be discussed. Throughout the course, several real-world examples will be demonstrated showcasing the practical impact of the tools learned in the course.'),nl,nl.

describe(statistical_signal_processing):-
    write('This post graduate course is designed to cover techniques for statistical signal processing, detection and parameter estimation. It will briefly review the preliminaries on linear algebra and statistics. The rest of the course is broadly divided into three parts. The first part will deal with the design, implementation and performance evaluation of detectors; this would cover composite and M-ary hypothesis testing. The second part of the course deals with estimation techniques like Maximum Likelihood, MAP and MMSE estimation. The third part introduces adaptive filtering approaches; this will cover stochastic and data-driven approach with emphasis on least squares based techniques. Homework will be a mix of theory and programming assignments.'),nl,nl.

describe(digital_signal_processing):-
    write('The objective of this course is to provide a basic introduction to the theory of digital signal processing (DSP). Since students have familiarity with Fourier and Laplace transforms and concepts such as linearity and shift invariance for the description and analysis of linear analog systems, we extend the use of ideas to the field of discrete time systems in this course. Major parts of the course will concentrate on signal analysis using Fourier transforms, linear system analysis, Filter design and a few more advanced topics. In this course, the discrete Fourier transform and its properties, sampling theorem and the relationship between continuous and discrete time transform will be covered. We will see how discrete time, linear shift invariant systems can be characterized using linear difference equations and the impulse response and show how tools such as the z-transform and discrete Fourier transform can be used in the design and analysis of such systems. We will then study the design and implementation of digital filters FIR and IIR filters). While this course deals largely with the theory of DSP, Python will be used to look at applications of this theory, particularly Fourier analysis and digital filter design.'),nl,nl.

describe(machine_learning_for_bio_medical_applications):-
    write('This course is designed for students having wide range of background like biology, medical science, pharmacology, bioinformatics, computer science. This course is divided in following three sections; i) Major challenges in the field of biomedical science, ii) Introduction/implementation of machine learning techniques for developing prediction models, and iii) solving biomedical problems using machine learning techniques. This course will be help students in developing novel methods for solving real-life problems in the field of biological and health sciences. Attempt will made to bridge gap between students and world class researchers, studentds will be exposed to highly accurate methods based on machine learning techniques (research papers).'),nl,nl.

describe(data_sciences_in_genomics):-
    write('The field of Genomics is expanding its horizon with help of high throughput technologies. Scientist are trying to answer fundamental questions related to health, society and human survival outside earth using genomics. With such increase of applications, it constantly needs computational experts for systematic analysis of data and acheiving meaning full insights. Infact the computational experts have now started taking lead in genomic projects. Hence this course is meant to guide students for data analysis approach and steps involved in computational genomics and make them familiar with latest development in genomics.'),nl,nl.

describe(big_data_mining_in_healthcare):-
    write('There is a exponential growth of data in the field of biological, medical and clinical scineces. Aim of this course is to taught implementation of data mining techniques in healthcare, to solve health-related problems. In this course, students will learn techniques for managing and mining big data. It will be broadly divided in four parts; first part will cover various repositories or databases in the field of medical and biological data. In second part, students will be introduced with techniques comonly used to analyze and manage big data. Implementation of techniques using Python will be covered in third phase of this course. Finally, students will learn how to solve health-related problems using knowldge based discovery approach.'),nl,nl.

describe(network_science):-
    write('The objective of this course is to provide introduction to network science, an emerging interdisciplinary discipline with various applications.'),nl,nl.