import nltk
from nltk import punkt
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import pyswip
from pyswip import Prolog

f = open("C:/Users/shiva/Downloads/AI-A5-Shivamgupta-2020406/ai_a5.txt", 'w')

ps = PorterStemmer()
inplist = []
inp1 = input("Select your branch from the following (CSE, ECE and CSB):  ")
tok1 = word_tokenize(inp1)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if 'cse' in inplist:
    f.write("branch(1).\n")
elif 'ece' in inplist:
    f.write("branch(2).\n")
elif 'csb' in inplist:
    f.write("branch(3).\n")

inp2 = input("Please enter your CGPA: ")
tok1 = word_tokenize(inp2)

for wod in tok1:
    stem1 = ps.stem(wod)

f.write("cgpa(" + stem1 + ").\n")

inplist = []
inp3 = input('Do you have good programming skills? ')
tok1 = word_tokenize(inp3)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("skills(programming).\n")

inplist = []
inp5 = input('Do you have high level knowledge in maths and like doing it? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("skills(maths).\n")

inplist = []
inp5 = input('Do you have good knowledge in statistics? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("skills(statistics).\n")

inplist = []
inp4 = input("Do you know c_plus_plus? ")
tok1 = word_tokenize(inp4)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("knows_language(c_plus_plus).\n")

inplist = []
inp4 = input("Do you know python? ")
tok1 = word_tokenize(inp4)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("knows_language(python).\n")

inplist = []
inp4 = input("Do you know java? ")
tok1 = word_tokenize(inp4)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("knows_language(java).\n")

inplist = []
inp4 = input("Do you know mysql? ")
tok1 = word_tokenize(inp4)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("knows_language(mysql).\n")

inplist = []
inp5 = input('Have you done dsa? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(dsa).\n")

inplist = []
inp5 = input('Have you done la? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(la).\n")

inplist = []
inp5 = input('Have you done pns? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(pns).\n")

inplist = []
inp5 = input('Have you done dbms? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(dbms).\n")

inplist = []
inp5 = input('Have you done multivariate_calculus? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(multivariate_calculus).\n")

inplist = []
inp5 = input('Have you done principles_of_communication_systems? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(principles_of_communication_systems).\n")

inplist = []
inp5 = input('Have you done signals_and_systems? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("courses_completed_curr(signals_and_systems).\n")

inplist = []
inp5 = input('Are you interested in Machine learning field? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("likes(ml).\n")

inplist = []
inp5 = input('Are you interested working with data? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("likes(data).\n")

inplist = []
inp5 = input('Do you like analysing and designing complex algorithms? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("likes(algorithms).\n")

inplist = []
inp5 = input('Are you interested in network systems? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("likes(network_systems).\n")

inplist = []
inp5 = input('Are you interested in operating systems? ')
tok1 = word_tokenize(inp5)
for wod in tok1:
    stem1 = ps.stem(wod)
    inplist.append(stem1)
if "y" in inplist:
    f.write("likes(operating_systems).\n")

f.close()

swipl = Prolog()
swipl.consult(
    "C:/Users/shiva/Downloads/AI-A5-Shivamgupta-2020406/2020406_ai (assignment 1).pl"
)

# Query for courses
courses = list(swipl.query('electiveguide'))