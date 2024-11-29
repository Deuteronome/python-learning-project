from statistics import mean
from random import shuffle
from random import randint

def main():
    # basics
    # average()
    # condition()
    # password_verif()
    # ticket_sale()
    # list_practice()
    # grade_manager()
    # text_generator()
    # loop_practice()
    fair_price()

def basics():
    # print("Hello World!")
    # Création de variables
    user_name = "Mister Bear"  # string
    age = 19  # integer
    wallet = 125.7  # float
    is_happy = True  # boolean
    # print(user_name, age)
    age = 25
    # print(age)
    age = age + 1
    # print(age)
    print("Salut " + user_name + "!, vous avez " + str(age) + " ans.")

def average():
    note1 = float(input("première note?"))
    note2 = float(input("deuxième note?"))
    note3 = float(input("troisième note?"))

    average_note = (note1 + note2 + note3) /3

    print("moyenne : "+ str(average_note))

def condition():
    wallet = 4000
    computer_price = 2959

    if wallet >= computer_price:
        print(f"Vous pouvez acheter cet ordinateur, il vous restera {wallet - computer_price} euros")
    else :
        print(f"Cet ordinateur est trop cher, il vous manque {computer_price - wallet} euros")

    #ternaire :

    verif = ("achat possible", "ce n'est pas raisonable")[wallet <= computer_price]
    print(wallet, computer_price, wallet <= computer_price, verif)

def password_verif():
    password = input('Définnissez votre mot de passe : ')
    pass_lenght = len(password)
    verif_message = ("Mot de passe trop court", "Longueur suffisante")[pass_lenght>8]
    print(verif_message)

def ticket_sale():
    age = int(input("quel est votre age?"))
    popcorn = input("Voulez-vous du popcorn? (oui/non)")

    if age <= 12 :
        price = 4
    elif 12 < age < 18 :
        price = 5.5
    else :
        price = 8

    if popcorn == "oui" :
        price += 5

    print("Coût du billet : {}€".format(price))

def list_practice():
    online_players = ["MisterBear", "Graven", "Ananas", "Climax"]
    print(online_players)

    online_players[0] = "Lord of bears"
    print(online_players[0])

    online_players.insert(2, "Flying Cat")

    online_players[2:5] = ["Caribou", "Firebird", "Noob"]
    print(online_players)

    online_players.append("Gameur123")
    print(online_players)
    online_players.extend(['Mighty Frog', 'Red Beard'])
    print(online_players)

    online_players.pop(1)
    online_players.remove("Noob")
    print(online_players)

    online_players.clear()
    print(online_players)

def grade_manager():
    notes =[8, 12, 13, 9, 14]
    print(notes)
    shuffle(notes)
    print(notes)

    result = mean(notes)
    print("moyenne : {}".format(result))

    text = input("emil/mot de passe/pseudo").split("/")
    print("Salut {}, ton email est {} et ton mot de passe est {}".format(text[2], text[0], text[1]))

def text_generator():
    words = input("Liste de mot séparés par /").split("/")
    shuffle(words)

    if len(words) < 10 :
        print("{} {}".format(words[0], words[1]))
    else:
        print("{} {} {}".format(words[len(words)-3], words[len(words)-2], words[len(words)-1]))

def loop_practice():
    for num_client in range(1, 6):
        print("Vous êtes le client numéro {}".format(num_client))

    email_list = ["misterbear@e2c.fr", "jpd@e2c.fr", "other@outlook.com", "admin@e2c-app-factory.fr", "noob@e2c.fr"]
    black_list = ["misterbear@e2c.fr", "admin@e2c-app-factory.fr"]

    for email in email_list:
        if email in black_list :
            print("email {} bloqué, envoi impossible".format(email))
            continue

        print("email envoyé à l'adresse {}".format(email))

    salary =1500

    while salary < 2000 :
        salary += 120
        print("salaire actuel : {}".format(salary))

    subscriber_count = 2500
    month = 24

    for now in range(1, month+1):
        subscriber_count *= 1.1
        print("mois {} - nombre d'abonnés : {}".format(now, int(subscriber_count)))

def fair_price():
    target = randint(1,100)
    #print(target)

    print("Devinez un nombre entre 1 et 100")
    count = 1
    user_choice = int(input("votre proposition : "))

    while user_choice != target:
        message = ("Trop petit", "Trop grand")[user_choice > target]
        print(message)
        user_choice = int(input("Nouvelle proposition : "))
        count +=1

    print("Bravo, vous avez trouvé en {} coups".format(count))

if __name__ == '__main__':
     main()