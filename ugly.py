import turtle

w=600
h=600
turtle.setup(w,h) # start with calling setup to turn on listeners
questions = 2
global points
height1 = h/2-h/5
height2 = h/2-3*h/5
points = 0
z = False
# define variables
panel=turtle.Screen()

panel.register_shape("button", ((0,0), (0,120),(40,120),(40,0)))

class answerTurt(turtle.Turtle):
    def __init__(self, Color):
        super().__init__() # copy all the methods and attributes of turtle
        self.running = False # for animation
        
        # immediately set up turtle and start movements
        self.up()
        self.goto(w/4,h)
        self.shape('button')
        self.color(Color)


turtle1= turtle.Turtle() # text turtle
# first question 
answerChoice1 = answerTurt('green',height1) 
answerChoice2 = answerTurt('red',height2)

#answerChoice1.up()
answerChoice1.goto(w/4,h/2-h/5)
#answerChoice1.shape('button')
#answerChoice1.color('green')
answerChoice1.write(teaTypes[0], False, align="Left",font=("Arial", 16, "bold"))  
answerChoice1Button = answerChoice1.stamp()

answerChoice2.up()
answerChoice2.goto(w/4,h/2-3*h/5)
answerChoice2.shape('button')
answerChoice2.color('red')
answerChoice2.write(teaTypes[1], False, align="Left",font=("Arial", 16, "bold")) 
answerChoice2Button = answerChoice2.stamp()


answerChoice1B = turtle.Turtle()
answerChoice2B = turtle.Turtle()
teaTurtle= turtle.Turtle()

questionturtle = turtle.Turtle()
questionturtle.up()
questionturtle.goto(0,h/2-h/10)



Question = ['What kind of tea is this?','What should this tea be brewed at?']
Answer = ['Correct!','Not quite! Try again!', '']

teaTypes = ['Oolong','Rooibos']
teaNames = ['Tie Guan Yin - Iron Goddess of Mercy']
teaTemps = [200,212]

#turtle.write(Tea[0], False, align="center",font=("Arial", 16, "bold"))

teaTurtle.hideturtle()
teaTurtle.up()
teaTurtle.goto(-w/4,h/3)
teaTurtle.down()
teaTurtle.write(teaNames[0], False, align="center",font=("Arial", 16, "bold"))

questionturtle.write(Question[points], False, align="Left",font=("Arial", 16, "bold"))


def setUp(x,y):
    # turtle.hideturtle()
    turtle1.clear()
    answerChoice1.clear()
    answerChoice2.hideturtle()
    turtle1.write(Answer[2], False, align="Left",font=("Arial", 16, "bold"))
    questionturtle.write(Question[points], False, align="Left",font=("Arial", 16, "bold"))
    
    answerChoice1.showturtle()
    answerChoice2.showturtle()
    answerChoice1.color('green')
    answerChoice1.up()
    answerChoice1.goto(w/4,h/2-h/5)
    answerChoice1.shape('button')
    answerChoice1.write(teaTypes[0], False, align="Left",font=("Arial", 16, "bold"))  


    answerChoice2.color('red')
    answerChoice2.up()
    answerChoice2.goto(w/4,h/2-3*h/5)
    answerChoice2.shape('button')
    answerChoice2.write(teaTypes[1], False, align="Left",font=("Arial", 16, "bold"))  

  
    answerChoice1.onclick(correct)
    answerChoice2.onclick(incorrect)  
    
def pointsCheck(points):
    print('HECK YEAH U WIN')
    answerChoice1B.clear()
    answerChoice2B.clear()
    answerChoice1B.hideturtle()
    answerChoice2B.hideturtle()
    turtle1.hideturtle()
    turtle1.clear()
    turtle1.write('What a delightful brew!', False, align="center",font=("Arial", 16, "bold"))
    questionturtle.clear()
    teaTurtle.clear()
    #TODO: Turtle scripts stops
        
def correct(x,y): #going to become selectionturtle
    i=0
    # turtle.hideturtle()
    turtle1.hideturtle()
    turtle1.clear()
    answerChoice1.clear()
    answerChoice2.clear()
    global points 
    global questionCounter
    points+=1
    if(points==questions):
        pointsCheck(points)
    else:
        questionturtle.clear()
        questionturtle.write(Question[points], False, align="Left",font=("Arial", 16, "bold"))
        answerChoice1.clearstamp(answerChoice1Button)
        answerChoice2.clearstamp(answerChoice2Button)
        answerChoice1.hideturtle()
        answerChoice2.hideturtle()
        
        turtle1.up()
        turtle1.goto(0,h/2-h/5)
        turtle1.write(Answer[i], False, align="center",font=("Arial", 16, "bold"))
        
    
        answerChoice1B.color('purple')
        answerChoice1B.up()
        answerChoice1B.goto(w/4,h/2-h/5)
        answerChoice1B.shape('button')
        answerChoice1B.write(teaTemps[0], False, align="Left",font=("Arial", 16, "bold"))  
        answerChoice1B.onclick(correct)
            
        answerChoice2B.color('blue')
        answerChoice2B.up()
        answerChoice2B.goto(w/4,h/2-3*h/5)
        answerChoice2B.shape('button')
        answerChoice2B.write(teaTemps[1], False, align="Left",font=("Arial", 16, "bold"))  
        answerChoice2B.onclick(incorrect)
    

def incorrect(x,y): #going to become selectionturtle
    i=1
    print('incorrect!!')
    answerChoice2.clearstamp(answerChoice2Button)
    answerChoice1.clearstamp(answerChoice1Button)
    answerChoice1.clear()
    answerChoice2.clear()
    answerChoice2.hideturtle()
    answerChoice1.hideturtle()
 
    turtle1.clear()
    turtle1.up()
    turtle1.goto(0,h/2-h/5)
    turtle1.write(Answer[i], False, align="Left",font=("Arial", 16, "bold"))
    turtle1.onclick(setUp)

    
   
answerChoice2.onclick(incorrect)   
answerChoice1.onclick(correct)



turtle.done()
