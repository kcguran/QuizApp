# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def chechAnswer(self, answer):
        return self.answer == answer



# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = quiz.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-' + q)

        answer = input('Answer : ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.chechAnswer(answer):
            self.score += 1
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print ('Score : ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Over...')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('Which is the best programming language ?', ['C#','python','javascript','java'], 'python')
q2 = Question('Which is the most popular programming language ?', ['python','C#','javascript','java'], 'python')
q3 = Question('Which programming language is the most profitable ?', ['C#','java','javascript','python'], 'python')
questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.loadQuestion()