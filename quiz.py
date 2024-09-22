questions = [
    ["Who is known as the Father of the Nation in India?", "Jawaharlal Nehru", "Bhagat Singh", "Mahatma Gandhi",
     "Sardar Patel", 3],
    ["What is the capital city of Australia?", "Sydney", "Melbourne", "Brisbane", "Canberra", 4],
    ["Which planet is known as the Red Planet?", "Venus", "Jupiter", "Mars", "Saturn", 3],
    ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Who wrote the play Romeo and Juliet?", "Charles Dickens", "William Shakespeare", "George Bernard Shaw",
     "Jane Austen", 2],
    ["Which element has the chemical symbol 'O'?", "Gold", "Osmium", "Oxygen", "Silver", 3],
    ["Which country is known as the Land of the Rising Sun?", "China", "Thailand", "Japan", "South Korea", 3],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the smallest prime number?", "0", "1", "2", "3", 3],
    ["Which company is known for the iPhone?", "Samsung", "Google", "Apple", "Sony", 3],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", 3],
    ["What is the main ingredient in traditional guacamole?", "Tomato", "Avocado", "Onion", "Pepper", 2],
    ["Who is the author of the Harry Potter series?", "J.K. Rowling", "J.R.R. Tolkien", "C.S. Lewis", "Suzanne Collins",
     1],
    ["What is the largest mammal in the world?", "African Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["who made this application", "sam", "harry", "Aryan", "ram", 3]

]

levels = ["1000", "2000", "4000", "5000", "10000", "20000", "40000", "80000", "160000", "320000", "640000", "1250000",
          "2500000", "5000000", "10000000"]
# assigning levels of money in list


# correct answer from list

money = 0
# assigning take home money

for i in range(0, len(questions)):
    print(f"Questions for Rs.{levels[i]} is on your computer screen\n")
    question = questions[i][0]
    print(question)
    print(f"a. {questions[i][1]}         b. {questions[i][2]}")
    print(f"c. {questions[i][3]}         d. {questions[i][4]} \n")

    try :
        userAnswer = int(input("Enter your Answer(1-4):"))
    except :
        print("invalid input input number between 1 to 4")
        continue

    if userAnswer == questions[i][5]:
        print(f"correct answer ,you have won Rs.{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 1000000

    else:
        print(" Wrong answer ")
        break

print(f"your take home money is {money}")