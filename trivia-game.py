import random

questions = {
  "What is the capital of France?": "Paris",
  "What is the largest planet in our solar system?": "Jupiter",
  "How many continents are there on Earth?": "Seven",
  "What is the chemical symbol for water?": "H₂O",
  "Who painted the Mona Lisa?": "Leonardo da Vinci",
  "What gas do plants absorb from the atmosphere?": "Carbon dioxide",
  "What is the hardest natural substance on Earth?": "Diamond",
  "Which planet is known as the Red Planet?": "Mars",
  "How many bones are in the adult human body?": "206",
  "What is the process by which plants make their own food?": "Photosynthesis",
  "Who was the first President of the United States?": "George Washington",
  "What year did the Titanic sink?": "1912",
  "Which ancient civilization built the pyramids?": "Egyptians",
  "Who was the first man to walk on the Moon?": "Neil Armstrong",
  "In which year did World War II end?": "1945",
  "Which is the longest river in the world?": "The Nile River",
  "What is the smallest country in the world?": "Vatican City",
  "Which ocean is the largest?": "Pacific Ocean",
  "Which U.S. state is known as the Sunshine State?": "Florida",
  "What is the capital of Japan?": "Tokyo",
  "How many players are on a soccer team on the field at one time?": "11",
  "What sport uses a shuttlecock?": "Badminton",
  "Which country won the FIFA World Cup in 2018?": "France",
  "How many rings are there in the Olympic Games symbol?": "Five",
  "In which sport would you perform a slam dunk?": "Basketball",
  "Who played Iron Man in the Marvel movies?": "Robert Downey Jr.",
  "What is the name of Harry Potter’s pet owl?": "Hedwig",
  "Which animated movie features a talking snowman named Olaf?": "Frozen",
  "What is the highest-grossing film of all time?": "Avatar",
  "Which movie series features the character Jack Sparrow?": "Pirates of the Caribbean",
  "Who is known as the King of Pop?": "Michael Jackson",
  "Which British band wrote the song ‘Hey Jude’?": "The Beatles",
  "Which female artist released the album ‘1989’?": "Taylor Swift",
  "What instrument does a pianist play?": "Piano",
  "Who sang ‘Shape of You’?": "Ed Sheeran",
  "What is the main ingredient in guacamole?": "Avocado",
  "Which fruit is known for having its seeds on the outside?": "Strawberry",
  "Which country is famous for sushi?": "Japan",
  "What type of pasta is shaped like small rice grains?": "Orzo",
  "What is the primary ingredient in hummus?": "Chickpeas",
  "Who wrote ‘Romeo and Juliet’?": "William Shakespeare",
  "What is the name of the wizarding school in Harry Potter?": "Hogwarts",
  "Who wrote ‘The Hobbit’?": "J.R.R. Tolkien",
  "What is the name of Sherlock Holmes' assistant?": "Dr. John Watson",
  "Which book series features the character Katniss Everdeen?": "The Hunger Games",
  "Who founded Microsoft?": "Bill Gates",
  "What does “HTTP” stand for in a website address?": "Hypertext Transfer Protocol",
  "What is the name of Apple’s virtual assistant?": "Siri",
  "Which social media platform is known for tweets?": "Twitter (now X)",
  "What does “CPU” stand for in computing?": "Central Processing Unit"
}


def trivia_game():
    questions_list = list(questions.keys())
    total_question = 5
    score = 0

    selected_questions = random.sample(questions_list, total_question)

    for idx, q in enumerate(selected_questions):
        print(f"{idx + 1}. {q} > {questions[q]}")

        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[q]

        if user_answer == correct_answer.lower():
            score += 1
            print("Correct!\n")
        else:

            print(f"Wrong. The correct answer is: {correct_answer}\n")


    print(f"Game over! Your final score is: {score}/{total_question}")


trivia_game()
