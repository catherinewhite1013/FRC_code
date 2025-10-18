import wpilib           # Used to get the joysticks
import wpilib.drive     # Used for the DifferentialDrive class
import rev              # REV library

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
            """
            This function is called upon program startup and
            should be used for any initialization code.
            """
            self.leftFront = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushed) #這怎麼調(?
            self.leftRear = rev.CANSparkMax(4, rev.CANSparkMax.MotorType.kBrushed) #這怎麼調(?
            self.rightFront = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushed)#這怎麼調(?
            self.rightRear = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushed)#這怎麼調(?
            self.leftRear.follow(self.leftFront)
            self.rightRear.follow(self.rightFront)
            self.robotDrive = wpilib.drive.DifferentialDrive(self.leftFront, self.rightFront)
            self.controller = wpilib.XboxController(0)
            self.rightDrive.setInverted(True)#這個要調左右邊(看馬達方向)

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        self.robotDrive.arcadeDrive(-self.controller.getLeftY(), -self.controller.getRightX())

    