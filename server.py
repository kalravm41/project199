import socket
from threading import Thread
import random
from typing import Collection

clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipAddress = '127.0.0.1'
port = 8000

def remove(conn):
    if conn in clients:
        clients.remove(Collection) 


def broadcast(message, conn) :
    for client in clients:
        if(client != conn) :
            try:
                client.send(message.encode('UTF-8'))

            except:
                remove(client) 

def clientThread(conn, addr):
    score = 0
    conn.send('Welcome To This Quiz Game'.encode('UTF-8')) 
    conn.send(('You Will Recieve a Question, Answer To Which Should Be Any One a, b, c or d\n'.encode('UTF-8'))) 
    conn.send('Good Luck\n\n'.encode('UTF-8')) 

    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('UTF-8')

            if message :
                if message.lower() == answer:
                    score += 1
                    conn.send(f"Bravo! Your Score is {score}\n\n".encode("UTF-8"))

                else:
                    conn.send("Incorrect answer ! Better Luck Next Time!\n\n".encode("UTF-8")) 

                remove_question(index)
                index, question, answer = get_random_question_answer(conn)   

            else :
                remove(conn)    

        except:
            continue 

def get_random_question_answer(conn):
    random_index = random.randint(0, len(questions)-1)
    random_question = questions[random_index]
    random_answer = answers[random_index]

    conn.send(random_question.encode('UTF-8'))
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

questions = [" What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\nd.Pizza",
             " Water boils at 212 Units at which scale? \n a.Fahrenheit\n b.Celsius\nc.Rankine\n d.Kelvin",
             " Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\nc.Walrus\n d.Seal",
             " Who was the character famous in our childhood rhymes associated with alamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Mukesh",
             " How many bones does an adult human have? \n a.206\n b.208\n c.201\nd.196",
             " How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4",
             " What element does not exist? \n a.Xf\n b.Re\n c.Si\n d.Pa",
             " How many states are there in India? \n a.24\n b.29\n c.30\n d.31",
             " Who invented the telephone? \n a.A.G Bell\n b.John Wick\n c.Thomas Edison\n d.G Marconi",
             " Who is Loki? \n a.God of Thunder\n b.God of Dwarves\n c.God of Mischief\n d.God of Gods",
             " Who was the first Indian female astronaut ? \n a.Sunita Williams\nb.Kalpana Chawla\n c.None of them\n d.Both of them ",
             " What is the smallest continent? \n a.Asia\n b.Antarctic\n c.Africa\nd.Australia",
             " The beaver is the national embelem of which country? \n a.Zimbabwe\nb.Iceland\n c.Argentina\n d.Canada",
             " How many players are on the field in baseball? \n a.6\n b.7\n c.9\nd.8",
             " Hg stands for? \n a.Mercury\n b.Hulgerium\n c.Argenine\n d.Halfnium", " Who gifted the Statue of Libery to the US? \n a.Brazil\n b.France\nc.Wales\n d.Germany",
             " Which planet is closest to the sun? \n a.Mercury\n b.Pluto\n c.Earth\nd.Venus"
             ]

answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd',
'c', 'a', 'b', 'a']

server.bind((ipAddress, port))
server.listen()

while True:
    conn, addr = server.accept()
    clients.append(conn);

    print(addr[0] + ' connected ')

    newThread = Thread(target= clientThread, args= (conn, addr))
    newThread.start()    