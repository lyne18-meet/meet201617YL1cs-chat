#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!

#####################################################################################
#                                  IMPORTS
from turtle_chat_widgets import TextInput
import turtle
from turtle_chat_widgets import Button
from turtle_chat_client import Client


#####################################################################################
#import the turtle module
#import the Client class from the turtle_chat_client module
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
#####################################################################################
#####################################################################################

#####################################################################################
#                                  TextBox
class TextBox(TextInput):
    def draw_box(self):
        self.draw=turtle.clone()
        self.draw.penup()
        self.draw.hideturtle()
        self.draw.goto(self.width/2,0)
        self.draw.pendown()
        self.draw.goto(-self.width/2,0)
        self.draw.goto(-self.width/2,-self.height)
        self.draw.goto(self.width/2,-self.height)
        self.draw.goto(self.width/2,0)

    def write_msg(self):
        self.writer.clear()
        self.writer.write(self.new_msg, font=('Arial',12,'normal'))
##        if self.TextBox.letters_per_line== 40:
##            self.new_msg([40])+'\r'+self.new_msg
##       
class SendButton(Button):
     def __init__(self,my_turtle=None,shape=None,pos=(0,0),view=None):
         super(SendButton,self).__init__(my_turtle=None,shape=None,pos=(0,-150))
         self.view=view
     def fun(self,x=None,y=None):
         self.view.send_msg()
         
         
         
        

        

        
      
        
           
###################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:

#draw_box
#write_msg

#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.

#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like

 #  self.writer.write(a_string_variable)

  # and you can erase that text using

   #self.writer.clear()

#3. If you want to make a newline character (i.e. go to the next line), just add
 #  \r to your string.  Test it out at the Python shell for practice
###################################################################################
###################################################################################

###################################################################################
  #                                SendButton                                       #
###################################################################################
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to

 #1. send a message to the other chat participant - to do this,
  #  you will need to call the send method of your Client instance
 #2. update the messages that you see on the screen

#HINT: You may want to override the __init__ method so that it takes one additional
 #     input: view.  This will be an instance of the View class you will make next
  #    That class will have methods inside of it to help
   #   you send messages and update message displays.
###################################################################################
###################################################################################


################################################################
    #                         View                               #
################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.

#Read the comments below for hints and directions.
################################################################
################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):
        self.username=username
        self.partner_name= partner_name
        self.my_client= Client()
        turtle.setup(width= self._SCREEN_WIDTH, height= self._SCREEN_HEIGHT)
         
        
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###

        #Make a new client object and store it in this instance.

        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.

        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        self.turtle_list=[]
        self.me=turtle.clone()
        self.me.penup()
        self.me.goto(-100,120)
        partner=turtle.clone()
        partner.penup()
        partner.goto(-100,150)
        self.msg_queue.append(self.me)
        self.msg_queue.append(partner)
        #for msg in self.msg_queue:
        #    self.msg_queue.append(turtle.clone())
        
            ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###

        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###

        self.TextBox=TextBox()
        self.send_btn=SendButton(view=self)
        self.setup_listeners()
        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###
    
    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also call update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        self.my_client.send(self.TextBox.new_msg)
        self.msg_queue.append(self.TextBox.new_msg)
        self.TextBox.clear_msg()
        self.display_msg()
        
        
    def get_msg(self):
        return self.textbox.get_msg()

    def setup_listeners(self):

        turtle.onkeypress(self.send_btn.fun,"Return")
        turtle.listen()
       
        
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        self.msg_queue.insert(0,msg)
        self.display_msg()
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display

    def display_msg(self):
        self.me.clear()
        self.me.write(self.msg_queue[0],font=('Arial',14,'normal'))
       
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        
##############################################################
##############################################################
turtle.bgpic("bgimg.gif")
turtle.pensize(3)
turtle.pencolor("white")
new_pos= turtle.pos()



    
    
    
##x_pos= new_pos[0]

##if x_pos== 200/2:
##    turtle.goto(-200/2,y_pos-1)

#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        msg_in=my_view.my_client.receive()
        if not(msg_in is None):
            if msg_in==my_view.my_client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()


