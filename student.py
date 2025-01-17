#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 82
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1025  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": (" Navigate the World", self.nav),
                "d": (" Dance", self.dance),
                "o": (" Obstacle Counting", self.obstacle_count),
                "s": (" Shy Greg", self.shy),
                "f": (" Follow the Leader", self.follow),
                "c": (" Calibrate", self.calibrate),
                "q": (" Quit at Life", self.quit),
                "v": (" Vanek Test", self.vanek),
                "x": (" Skri Test", self.skri),
                "j": (" Do A Jig", self.Do_A_Jig),
                "l": (" Go Find Wall and Spin 'Round 'n 'Round", self.spin_wall),
                "w": (" Avoid All the Boxes", self.Avoid_Box),
                "g": (" Just Find the Shorter Wall for Crying Out Loud", self.To_Be_Short_Or_Not_To_Be),
                "u": (" The Ultimate Avoidance of the Consequences of Your Life Choices", self.Ultimate_Avoidance),
                "m": (" Maze Runner but Christopher Paolini Style", self.Maze_Runner)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def Maze_Runner(self):
      while True:
        self.fwd()
        self.read_distance()

        if (self.read_distance() < 200):
          self.stop()
          self.servo(self.MIDPOINT + 500)
          time.sleep(.25)
          rightfront = self.read_distance()

          self.servo(self.MIDPOINT - 500)
          time.sleep(.25)
          leftfront = self.read_distance()

          self.servo(self.MIDPOINT)
          time.sleep(.25)
          front2 = self.read_distance()

          if (rightfront < 200 and leftfront > 200):
            self.right()
            time.sleep(.85)
            self.stop()
          elif (leftfront < 200 and rightfront > 200):
            self.left()
            time.sleep(.85)
            self.stop()
          elif (front2 < 200 and rightfront < 200 and leftfront < 200):
            self.right()
            time.sleep(1.7)
          """
          else:
            self.To_Be_Short_Or_Not_To_Be_Short_4_Maze_Runner()
      """



    def To_Be_Short_Or_Not_To_Be_Short_4_Maze_Runner(self):
          self.stop()
          self.servo(self.MIDPOINT + 300)
          time.sleep(.25)
          idk_1 = self.read_distance()

          self.servo(self.MIDPOINT - 300)
          time.sleep(.25)
          idk_2 = self.read_distance()
          
          self.servo(self.MIDPOINT)
          if (idk_1 > idk_2):
            self.left()
            time.sleep(.75)
            self.stop
          elif (idk_1 < idk_2):
            self.right()
            time.sleep(.75)
            self.stop



    def Ultimate_Avoidance(self):
      while True:
        self.fwd()
        self.servo(self.MIDPOINT + 300)
        time.sleep(.25)

        idk_1 = self.read_distance()
        if (idk_1 < 200):
          self.stop()
          print ("swerving left")
          self.right(primary=90, counter=60)
          time.sleep(.75)
          self.left(primary=90, counter=60)
          time.sleep(.75)
          self.stop()


        self.servo(self.MIDPOINT)
        time.sleep(.25)
        idk_2 = self.read_distance()

        if (idk_2 < 200):
          self.To_Be_Short_Or_Not_To_Be_Short()


        self.servo(self.MIDPOINT - 300)
        time.sleep(.25)
        idk_3 = self.read_distance()

        if (idk_3 < 200):
          self.stop()
          self.left(primary=90, counter=60)
          time.sleep(.75)
          self.right(primary=90, counter=60)
          time.sleep(.75)
          self.stop()



    def To_Be_Short_Or_Not_To_Be_Short(self):
          self.stop()
          self.servo(self.MIDPOINT + 300)
          time.sleep(1)
          idk_1 = self.read_distance()
          print ("leFt: " + str(idk_1))
          self.servo(self.MIDPOINT - 300)
          time.sleep(1)
          idk_2 = self.read_distance()
          print ("Right: " + str(idk_2))
          self.servo(self.MIDPOINT)
          if (idk_1 > idk_2):
            print("Left")
            self.left()
            time.sleep(1)
            self.fwd()
            time.sleep(2)
            self.right()
            time.sleep(1)
            self.fwd()
          elif (idk_1 < idk_2):
            print("Right")
            self.right()
            time.sleep(1)
            self.fwd()
            time.sleep(2)
            self.left()
            time.sleep(1)
            self.fwd()



    def To_Be_Short_Or_Not_To_Be(self):
       while True:
        if (self.read_distance() < 200):
          self.stop()
          self.servo(self.MIDPOINT + 300)
          time.sleep(1)
          idk_1 = self.read_distance()
          print ("leFt: " + str(idk_1))
          self.servo(self.MIDPOINT - 300)
          time.sleep(1)
          idk_2 = self.read_distance()
          print ("Right: " + str(idk_2))
          self.servo(self.MIDPOINT)
          if (idk_1 > idk_2):
            print("Left")
            self.left()
            time.sleep(1)
            self.fwd()
            time.sleep(2)
            self.right()
            time.sleep(1)
            self.fwd()
          elif (idk_1 < idk_2):
            print("Right")
            self.right()
            time.sleep(1)
            self.fwd()
            time.sleep(2)
            self.left()
            time.sleep(1)
            self.fwd()
        else:
          self.fwd()



    def Avoid_Box(self):
      while True:
        self.read_distance()
        if self.read_distance() < 200:
          self.stop()
          self.right()
          time.sleep(1)
          self.stop()
          self.fwd()
          time.sleep(1)
          self.stop()
          self.left()
          time.sleep(1)
          self.fwd()
          #self.servo(1750)
          #self.read_distance()
          #self.servo(-1750)
          #if self.read_distance() < 200:
          #  self.fwd()
          #elif self.read_distance() > 200:
          #  self.left(primary = 40, counter = -40)
          #  time.sleep(1)
        else:
          self.fwd()

    #use self.servo(#) to move head left and right for when I have to find out which way    to go.



    def Do_A_Jig(self):
      if safe_to_dance():
        pass
      for _ in range(13):
        self.back()
        time.sleep(.15)
        self.stop()
        self.right(primary = 60, counter = -60)
        time.sleep(.25)
        self.stop()
        self.back()
        time.sleep(.15)
        self.stop()
        self.left(primary = 60, counter = -60)
        time.sleep(.25)
        self.stop()




    #Square = Skri Test
    def skri(self):
      #D.R.Y.
      for _ in range (4):
        self.fwd()
        time.sleep(2)
        self.stop()
        self.right(primary = 40, counter = -40)
        time.sleep(.96)
        self.stop()





#Decided to keep the Vanek Test anyways for reference

    def vanek(self):
      self.left(primary = 30, counter  = -30)
      time.sleep(1)
      self.stop()
     
        




    def spin_wall(self):
      while True:
        self.read_distance()
        if self.read_distance() < 100:
          self.stop()
          self.right(primary = 40, counter = -40)
          time.sleep(.75)
          self.stop()
          self.fwd()
          time.sleep(2)
          self.stop()
        else:
          self.fwd()





    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # TODO: check to see if it's safe before dancing
        
        # lower-ordered example...
        self.right(primary=50, counter=50)
        time.sleep(2)
        self.stop()
        





    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        return True





    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()





    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left





    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()






    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass






    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
