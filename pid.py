"a class implementation of Proportional-Integral-Derivative control, made from scratch to understand the concept"

import time

class PID: 
    # initialize 
    def __init__(self,
                 kp,
                 ki,
                 kd
                 ):
        # weights
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        # working variables
        self.setpoint = 0
        self.input = 0
        self.output = 0
        self.errSum = 0
        self.lastErr = 0
        self.lastTime = time.time()
        # self.sampleTime = 0.01 # sample time in sec
        
    def Compute(self):
        # compute the PID output
        
        # find the loop time
        self.now = time.time()
        dt = self.now - self.lastTime
        print(dt)

        # evaluate at regular intervals
        #if dt >= self.sampleTime:
        
        # compute error variables
        self.error = self.setpoint - self.input
        self.errSum += self.error *dt
        self.dErr = (self.error - self.lastErr) /dt
        
        
        # compute the output
        self.output = self.kp * self.error + self.ki * self.errSum + self.kd * self.dErr
        
        # for the next loop
        self.lastErr = self.error
        self.lastTime = self.now
        
    def SetTunings(self, kp, ki, kd):
        # adjusts the tunings
        self.kp = kp
        self.ki = ki #* self.sampleTime
        self.kd = kd #/ self.sampleTime

    # def SetSampleTime(self, newSampleTime):
    #     if newSampleTime > 0:
    #         ratio = newSampleTime / self.sampleTime

    #     self.ki *= ratio 
    #     self.kd /= ratio
    #     self.sampleTime = newSampleTime