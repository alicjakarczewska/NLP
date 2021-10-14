# tutorial source: https://www.machinelearningplus.com/spacy-tutorial-nlp/

# Before run code install:
# pip3 install spacy
# python -m spacy download en_core_web_sm

import spacy
nlp=spacy.load("en_core_web_sm")
print(nlp)

# Parse text through the `nlp` model
my_text = """The economic situation of the country is on edge , as the stock 
market crashed causing loss of millions. Citizens who had their main investment 
in the share-market are facing a great loss. Many companies might lay off 
thousands of people to reduce labor cost"""

my_doc = nlp(my_text)
print(type(my_doc))

# Printing the tokens of a doc
for token in my_doc:
  print(token.text)

# Printing tokens and boolean values stored in different attributes
for token in my_doc:
  print(token.text,'--',token.is_stop,'---',token.is_punct)

# Removing StopWords and punctuations
my_doc_cleaned = [token for token in my_doc if not token.is_stop and not token.is_punct]

for token in my_doc_cleaned:
  print(token.text)

# Reading a huge text data on robotics into a spacy doc
robotics_data= """Robotics is an interdisciplinary research area at the interface of computer science and engineering. Robotics involvesdesign, construction, operation, and use of robots. The goal of robotics is to design intelligent machines that can help and assist humans in their day-to-day lives and keep everyone safe. Robotics draws on the achievement of information engineering, computer engineering, mechanical engineering, electronic engineering and others.Robotics develops machines that can substitute for humans and replicate human actions. Robots can be used in many situations and for lots of purposes, but today many are used in dangerous environments(including inspection of radioactive materials, bomb detection and deactivation), manufacturing processes, or where humans cannot survive (e.g. in space, underwater, in high heat, and clean up and containment of hazardousmaterials and radiation). Robots can take on any form but some are made to resemble humans in appearance. This is said to help in the acceptance of a robot in 
certain replicative behaviors usually performed by people. Such robots attempt to replicate walking, lifting, speech, cognition, or any other human activity. Many of todays robots are inspired by nature, contributing to the field of bio-inspired 
robotics.The concept of creating machines that can operate autonomously dates back to classical times, but research into the functionality and potential uses of robots did not grow substantially until the 20th century. Throughout history, it has been frequently assumed by various scholars, inventors, engineers, and technicians that robots will one day be able to mimic human behavior and manage tasks in a human-like fashion. Today, robotics is a rapidly growing field, as technological advances continue; researching, designing, and building new robots serve various practical purposes, whether domestically, commercially, or militarily. Many robots are built to do jobs that are hazardous to people, such as defusing bombs, finding survivors in unstable ruins, and exploring mines and shipwrecks. Robotics is also used in STEM (science, technology, engineering, and mathematics) as a teaching aid. The advent of nanorobots, microscopic robots that can be injected into the human body, could revolutionize medicine and human health.Robotics is a branch of engineering that involves the conception, design, manufacture, and operation of robots. This field overlaps with computer engineering, computer science (especially artificial intelligence), electronics, mechatronics, nanotechnology and bioengineering.The word robotics was derived from the word robot, which was introduced to the public by Czech writer Karel Capek in his play R.U.R. (Rossums Universal Robots), whichwas published in 1920. The word robot comes from the Slavic word robota, which means slave/servant. The play begins in a factory that makes artificial people called robots, creatures who can be mistaken for humans – very similar to the modern ideas of androids. Karel Capek himself did not coin the word. He wrote a short letter in reference to an etymology in the 
Oxford English Dictionary in which he named his brother Josef Capek as its actual 
originator.According to the Oxford English Dictionary, the word robotics was first 
used in print by Isaac Asimov, in his science fiction short story "Liar!", 
published in May 1941 in Astounding Science Fiction. Asimov was unaware that he 
was coining the term  since the science and technology of electrical devices is 
electronics, he assumed robotics already referred to the science and technology 
of robots. In some of Asimovs other works, he states that the first use of the 
word robotics was in his short story Runaround (Astounding Science Fiction, March 
1942) where he introduced his concept of The Three Laws of Robotics. However, 
the original publication of "Liar!" predates that of "Runaround" by ten months, 
so the former is generally cited as the words origin.There are many types of robots; 
they are used in many different environments and for many different uses. Although 
being very diverse in application and form, they all share three basic similarities 
when it comes to their construction:Robots all have some kind of mechanical construction, a frame, form or shape designed to achieve a particular task. For example, a robot designed to travel across heavy dirt or mud, might use caterpillar tracks. The mechanical aspect is mostly the creators solution to completing the assigned task and dealing with the physics of the environment around it. Form follows function.Robots have electrical components which power and control the machinery. For example, the robot with caterpillar tracks would need some kind of power to move the tracker treads. That power comes in the form of electricity, which will have to travel through a wire and originate from a battery, a basic electrical circuit. Even petrol powered machines that get their power mainly from petrol still require an electric current to start the combustion process which is why most petrol powered machines like cars, have batteries. The electrical aspect of robots is used for movement (through motors), sensing (where electrical signals are used to measure things like heat, sound, position, and energy status) and operation (robots need some level of electrical energy supplied to their motors and sensors in order to activate and perform basic operations) All robots contain some level of computer programming code. A program is how a robot decides when or how to do something. In the caterpillar track example, a robot that needs to move across a muddy road may have the correct mechanical construction and receive the correct amount of power from its battery, but would not go anywhere without a program telling it to move. Programs are the core essence of a robot, it could have excellent mechanical and electrical construction, but if its program is poorly constructed its performance will be very poor (or it may not perform at all). There are three different types of robotic programs: remote control, artificial intelligence and hybrid. A robot with remote control programing has a preexisting set of commands that it will only perform if and when it receives a signal from a control source, typically a human being with a remote control. It is perhaps more appropriate to view devices controlled primarily by human commands as falling in the discipline of automation rather than robotics. Robots that use artificial intelligence interact with their environment on their own without a control source, and can determine reactions to objects and problems they encounter using their preexisting programming. Hybrid is a form of programming that incorporates both AI and RC functions.As more and more robots are designed for specific tasks this method of classification becomes more relevant. For example, many robots are designed for assembly work, which may not be readily adaptable for other applications. They are termed as "assembly robots". For seam welding, some suppliers provide complete welding systems with the robot i.e. the welding equipment along with other material handling facilities like turntables, etc. as an integrated unit. Such an integrated robotic system is called a "welding robot" even though its discrete manipulator unit could be adapted to a variety of tasks. Some robots are specifically designed for heavy load manipulation, and are labeled as "heavy-duty robots".one or two wheels. These can have certain advantages such as greater efficiency and reduced parts, as well as allowing a robot to navigate in confined places that a four-wheeled robot would not be able to.Two-wheeled balancing robots Balancing robots generally use a gyroscope to detect how much a robot is falling and then drive the wheels proportionally in the same direction, to counterbalance the fall at hundreds of times per second, based on the dynamics of an inverted pendulum.[71] Many different balancing robots have been designed.[72] While the Segway is not commonly thought of as a robot, it can be thought of as a component of a robot, when used as such Segway refer to them as RMP (Robotic Mobility Platform). An example of this use has been as NASA Robonaut that has been mounted on a Segway.One-wheeled balancing robots Main article: Self-balancing unicycle A one-wheeled balancing robot is an extension of a two-wheeled balancing robot so that it can move in any 2D direction using a round ball as its only wheel. Several one-wheeled balancing robots have been designed recently, such as Carnegie Mellon Universitys "Ballbot" that is the approximate height and width of a person, and Tohoku Gakuin University BallIP Because of the long, thin shape and ability to maneuver in tight spaces, they have the potential to function better than other robots in environments with people
"""

# Pass the Text to Model
robotics_doc = nlp(robotics_data)

print('Before PreProcessing n_Tokens: ', len(robotics_doc))

# Removing stopwords and punctuation from the doc.
robotics_doc=[token for token in robotics_doc if not token.is_stop and not token.is_punct]

print('After PreProcessing n_Tokens: ', len(robotics_doc))

# Lemmatizing the tokens of a doc
text='she played chess against rita she likes playing chess.'
doc=nlp(text)
for token in doc:
  print(token.lemma_)

# Strings to Hashes and Back
doc = nlp("I love traveling")

# Look up the hash for the word "traveling"
word_hash = nlp.vocab.strings["traveling"]
print(word_hash)

# Look up the word_hash to get the string
word_string = nlp.vocab.strings[word_hash]
print(word_string)

# Create two different doc with a common word
doc1 = nlp('Raymond shirts are famous')
doc2 = nlp('I washed my shirts ')

# Printing the hash value for each token in the doc

print('-------DOC 1-------')
for token in doc1:
  hash_value=nlp.vocab.strings[token.text]
  print(token.text ,' ',hash_value)

print('-------DOC 2-------')
for token in doc2:
  hash_value=nlp.vocab.strings[token.text]
  print(token.text ,' ',hash_value)

