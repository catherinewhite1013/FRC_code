import wpilib           # Used to get the joysticks
import wpilib.drive     # Used for the DifferentialDrive class
import rev              # REV library

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.leftFront = rev.SparkMax(1, rev.SparkMax.MotorType.kBrushed) #這個出錯不要理他
        self.leftRear = rev.SparkMax(4, rev.SparkMax.MotorType.kBrushed) 
        self.rightFront = rev.SparkMax(2, rev.SparkMax.MotorType.kBrushed)
        self.rightRear = rev.SparkMax(3, rev.SparkMax.MotorType.kBrushed)
        self.leftRear.follow(self.leftFront) #這個也是不理他
        self.rightRear.follow(self.rightFront)
        self.robotDrive = wpilib.drive.DifferentialDrive(self.leftFront, self.rightFront)
        self.controller = wpilib.XboxController(0)
        self.rightFront.setInverted(True)

    def deadzone(self, value, zone = 0.1): #zone之後測試
        if abs(value) < zone: #看一下搖桿數值有沒有大於zone
           return 0.0
        return value 

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        self.robotDrive.arcadeDrive( self.deadzone(self.controller.getLeftY()), self.deadzone(self.controller.getRightX()) ) #調用zone(數值為搖桿XY)



    