# Input -----------------------------------------------------------------------------------------------------------------------------------------------------------

from durable.lang import *
# Main RuleSet. -------------------------------------------------------------------------------------------------------------------
with ruleset('choice'):

    # Choice Sport
    @when_all((m.type == 'sports'))
    def sport(c):
        c.assert_fact({
            'subject': 'Give',
            'predicate': 'a career in',
            'object': 'sports a try'
        })

    # Choice humanities
    @when_all((m.type == 'humanities') & (m.time == 'short'))
    def course(c):
        c.assert_fact('internship', {
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('humanities', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    @when_all((m.type == 'humanities') & (m.time == 'long'))
    def course(c):
        c.assert_fact('humanities', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    # Choice research
    @when_all((m.type == 'research') & (m.time == 'short'))
    def course(c):
        c.assert_fact('internship', {
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('research', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    @when_all((m.type == 'research') & (m.time == 'long'))
    def activity(c):
        c.assert_fact('research', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    # Choice information technology
    @when_all((m.type == 'information_technology') & (m.time == 'short'))
    def course(c):
        c.assert_fact('internship', {
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('information_technology', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    @when_all((m.type == 'information_technology') & (m.time == 'long'))
    def activity(c):
        c.assert_fact('information_technology', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    # Choice business, finance, entrepreneurship
    @when_all((m.type == 'business_finance') & (m.time == 'short'))
    def course(c):
        c.assert_fact('internship', {
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('business_finance', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    @when_all((m.type == 'business_finance') & (m.time == 'long'))
    def activity(c):
        c.assert_fact('business_finance', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    # Choice any
    @when_all((m.type == 'any') & (m.time == 'short'))
    def course(c):
        c.assert_fact('internship', {
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('research', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('humanities', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('information_technology', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('business_finance', {
            'time': 'short',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    @when_all((m.type == 'any') & (m.time == 'long'))
    def activity(c):
        c.assert_fact('research', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('humanities', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('information_technology', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })
        c.assert_fact('business_finance', {
            'time': 'long',
            'interests': c.m.interests,
            'courses': c.m.courses
        })

    @when_all((m.interests.anyItem((item.end >= 1))))
    def program(c):
        c.assert_fact({'feature': '-', 'feature': '-', 'feature': '-'})

    # Output if selected any facts
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate,
                                         c.m.object))


# Main RuleSet. -------------------------------------------------------------------------------------------------------------------

# Internship RuleSet for internships and such -------------------------------------------------------------------------------------------
with ruleset('internship'):

    @when_all(m.interests.anyItem((item.programming >= 1)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'software developer'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'Open Source'
        })

    @when_all(m.interests.anyItem((item.machine_learning >= 1)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'in machine learning'
        })

    @when_all(m.interests.anyItem((item.management >= 1)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'PR'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'management'
        })

    @when_all((m.interests.anyItem(
        (item.ui_design >= 2))) & (m.courses.anyItem(
            (item.designing_systems >= 5))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'UI Designer'
        })

    @when_all(m.interests.anyItem((item.leadership >= 1)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'product management'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'working on your own',
            'object': 'startup'
        })

    @when_all(m.interests.anyItem((item.public_speaking >= 1)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'Content Creation'
        })

    @when_all((m.interests.anyItem((item.teaching >= 2))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': ' as a tutor'
        })

    @when_all((m.interests.anyItem((item.research >= 1))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a',
            'object': 'research internship'
        })

    @when_all((m.interests.anyItem((item.end >= 1))))
    def program(c):
        c.assert_fact({'feature': '-', 'feature': '-', 'feature': '-'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate,
                                         c.m.object))


# Internship RuleSet for internships and such -------------------------------------------------------------------------------------------

# humanities RuleSet for careers in art and such -------------------------------------------------------------------------------------------
with ruleset('humanities'):

    @when_all(m.interests.anyItem((item.public_speaking >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'public speaker'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'content creator'
        })

    @when_all(m.interests.anyItem((item.performing >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as an',
            'object': 'actor'
        })

    @when_all(m.interests.anyItem((item.tourism >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'tour/adventure guide'
        })

    @when_all(m.interests.anyItem((item.media >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'journalist'
        })

    @when_all(m.interests.anyItem((item.literature >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'writer'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as an',
            'object': 'editor'
        })

    @when_all(m.interests.anyItem((item.art >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'commercial artist'
        })

    @when_all(m.interests.anyItem((item.fashion >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'fashion designer'
        })

    @when_all(m.interests.anyItem((item.dance >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'dancer'
        })

    @when_all(
        m.interests.anyItem((item.philosophy >= 2)) & m.courses.anyItem(
            (item.sociology >= 5)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'exploring a career in',
            'object': 'the field of philosophy'
        })

    @when_all(
        m.interests.anyItem((item.psychology >= 2)) & m.courses.anyItem(
            (item.intro_to_psychology >= 5)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'psychologist'
        })

    @when_all((m.interests.anyItem((item.end >= 1))))
    def program(c):
        c.assert_fact({'feature': '-', 'feature': '-', 'feature': '-'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate,
                                         c.m.object))


# humanities RuleSet for careers in art and such -------------------------------------------------------------------------------------------

# research RuleSet for careers in research and such -------------------------------------------------------------------------------------------
with ruleset('research'):

    @when_all(m.interests.anyItem((item.biology >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'biologist'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'internship',
            'object': 'Open Source'
        })

    @when_all(m.interests.anyItem((item.chemistry >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'chemist'
        })

    @when_all(m.interests.anyItem((item.physics >= 2)))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'physics'
        })

    @when_all((m.interests.anyItem(
        (item.teaching >= 2))) & (m.interests.anyItem((item.chemistry >= 2))))
    def program(c):
        c.assert_fact({
            'subject':
            'Consider',
            'predicate':
            'doing',
            'object':
            'higher studies and then working as a chemistry professor'
        })

    @when_all((m.interests.anyItem(
        (item.teaching >= 2))) & (m.interests.anyItem((item.biology >= 2))))
    def program(c):
        c.assert_fact({
            'subject':
            'Consider',
            'predicate':
            'doing',
            'object':
            'higher studies and then working as a biology professor'
        })

    @when_all((m.interests.anyItem(
        (item.teaching >= 2))) & (m.interests.anyItem((item.physics >= 2))))
    def program(c):
        c.assert_fact({
            'subject':
            'Consider',
            'predicate':
            'doing',
            'object':
            'higher studies and then working as a physics professor'
        })

    @when_all((m.research == 'none') | ((m.interests.anyItem(
        (item.none >= 1)))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'doing higher studies',
            'object': 'in a field of interest'
        })

    @when_all((m.interests.anyItem((item.end >= 1))))
    def program(c):
        c.assert_fact({'feature': '-', 'feature': '-', 'feature': '-'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate,
                                         c.m.object))


# research RuleSet for careers in research and such -------------------------------------------------------------------------------------------

# information_technology RuleSet for careers in art and such -------------------------------------------------------------------------------------------
with ruleset('information_technology'):

    @when_all((m.interests.anyItem((item.graphic_designing >= 2))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'graphic designer'
        })

    @when_all((m.interests.anyItem(
        (item.data_science >= 2))) & ((m.courses.anyItem(
            (item.data_mining >= 6))) | (m.interests.anyItem(
                (item.database_system_implementation >= 5)))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'data scientist'
        })

    @when_all((m.interests.anyItem((item.data_science >= 1))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'data analyst'
        })

    @when_all((m.interests.anyItem(
        (item.machine_learning >= 2))) & (m.courses.anyItem(
            (item.machine_learning >= 6))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'ML engineer'
        })

    @when_all((m.interests.anyItem(
        (item.machine_learning >= 2))) & (m.interests.anyItem(
            (item.research >= 2))) & (m.courses.anyItem(
                (item.machine_learning >= 6))))
    def program(c):
        c.assert_fact({
            'subject': 'As you are interested in research',
            'predicate': 'you can also consider doing research in ',
            'object': 'ML and related field'
        })

    @when_all((m.interests.anyItem(
        (item.programming >= 2))) & ((m.interests.anyItem(
            (item.operating_system >= 1))) | (m.interests.anyItem(
                (item.maths >= 1)))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a',
            'object': 'Software engineer'
        })

    @when_all((m.courses.anyItem(
        (item.deep_learning >= 5))) & (m.interests.anyItem(
            (item.research >= 2))))
    def program(c):
        c.assert_fact({
            'subject': 'As you are interested in research',
            'predicate': 'you can consider doing research in ',
            'object': 'deep learning and related field'
        })

    @when_all((m.courses.anyItem(
        (item.cryptography >= 5))) & (m.courses.anyItem(
            (item.data_mining >= 5))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'cryptographer'
        })

    @when_all((m.courses.anyItem(
        (item.cryptography >= 5))) & (m.courses.anyItem(
            (item.data_mining >= 5))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'cryptographer'
        })

    @when_all((m.courses.anyItem(
        (item.computer_networks >= 5))) & (m.courses.anyItem(
            (item.network_security >= 5))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career as a ',
            'object': 'network security engineer'
        })

    @when_all((m.courses.anyItem(
        (item.natural_language_processing >= 2))) & (m.interests.anyItem(
            (item.research >= 2))))
    def program(c):
        c.assert_fact({
            'subject': 'As you are interested in research',
            'predicate': 'you can also consider doing research in ',
            'object': 'NLP and related field'
        })

    @when_all((m.information_technology == 'none') | ((m.interests.anyItem(
        (item.none >= 1)))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'exploring a career in',
            'object': 'Information Technology space'
        })

    @when_all((m.interests.anyItem((item.end >= 1))))
    def program(c):
        c.assert_fact({'feature': '-', 'feature': '-', 'feature': '-'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate,
                                         c.m.object))


# information_technology RuleSet for careers in art and such -------------------------------------------------------------------------------------------

# business_finance RuleSet for careers in art and such -------------------------------------------------------------------------------------------
with ruleset('business_finance'):

    @when_all((m.interests.anyItem(
        (item.leadership >= 1))) & (m.interests.anyItem(
            (item.entrepreneurship >= 2))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'working on a',
            'object': 'startup'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'doing',
            'object': 'MBA'
        })

    @when_all((m.interests.anyItem(
        (item.finance >= 2))) & (m.interests.anyItem((item.maths >= 2))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career',
            'object': 'as financial consultant'
        })

    @when_all((m.interests.anyItem(
        (item.public_speaking >= 2))) & (m.interests.anyItem(
            (item.entrepreneurship >= 2))) & (m.courses.anyItem(
                (item.entrepreneurship >= 7))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'a career',
            'object': 'in public speaking'
        })

    @when_all((m.business_finance == 'none') | ((m.interests.anyItem(
        (item.none >= 1)))))
    def program(c):
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'exploring a career',
            'object': 'in management space'
        })
        c.assert_fact({
            'subject': 'Consider',
            'predicate': 'joining in a',
            'object': 'family business'
        })

    @when_all((m.interests.anyItem((item.end >= 1))))
    def program(c):
        c.assert_fact({'feature': '-', 'feature': '-', 'feature': '-'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate,
                                         c.m.object))


# business_finance RuleSet for careers in art and such -------------------------------------------------------------------------------------------

print("\n--------------------------------\n")
print("Welcome to Career Advisory System\n")
print("--------------------------------")
userName = input("What's your name? ")
print("\nHi, {0}! Hope you are having a great time at IIITD.".format(userName))

type_ = input(
    "Enter the type of career that fascinates you: sports, humanities, research, information_technology, business_finance, any: \n"
)
print()
time_duration = input(
    "Enter the duration of work you're looking for: short (part-time internship), long (considering joining full-time): \n"
)
print()
list_interest = [{'end': 1}]
print(
    "Enter interests and level at the interests. Enter 'end' to stop input\n")
print(
    "Available options: ui_design, graphic_designing, physics, biology, chemistry, literature, public_speaking, management, leadership, finance, entrepreneurship, fashion, philosophy, psychology, dance, performing, tourism, media, art, machine_learning, data_science, programming, operating_systems, teaching, research, maths, quantum_computing"
)

for i in range(23):
    inter = input("Enter interest: ")

    if (inter == "end"):
        break
    num = int(input("Enter level (1, 2, 3): "))
    interest = {inter: num}
    list_interest.append(interest)
    print()

print()

list_courses = [{'end': 1}]
print(
    "Select the courses you have done and then enter the cgpa scored by you in that particular course. Enter 'end' to stop input\n"
)
print(
    "Available options: designing_systems, entrepreneurship, economics, human_centered_design, machine_learning, artificial_intelligence, computer_networks, natural_langugae_processing, database_system_implementation, cryptography, network_security, competitive_programming, deep_learning, data_mining, graphic_designing, sociology, intro_to_philosophy"
)

for j in range(17):
    inter = input("Enter course name: ")

    if (inter == "end"):
        break

    num = int(
        input("Enter cgpa in that course (Enter integer between 1-10): "))
    course = {inter: num}
    list_courses.append(course)
    print()

print()
# Input -----------------------------------------------------------------------------------------------------------------------------------------------------------

# Asserting the choices ---------------------------------------------------------------------------------------------------------------------------------------------------------
print("Suggestions: \n")
assert_fact(
    'choice', {
        'type': type_,
        'time': time_duration,
        'interests': list_interest,
        'courses': list_courses
    })