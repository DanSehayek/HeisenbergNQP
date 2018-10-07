from FrequencyCheck import countCheck
from OperatorCheck import operatorCheck

def RUN(check,numQubits):
    if check == "Frequency":
        countCheck("Samples/{0}Q".format(numQubits))
    elif check == "S2S3":
        if numQubits == 3:
            operatorCheck("S2S3","Samples/3Q",-0.166667,range(100,10000,100),3)
        elif numQubits == 4:
            operatorCheck("S2S3","Samples/4Q",-0.0833333,range(100,10000,100),4)
        elif numQubits == 5:
            operatorCheck("S2S3","Samples/5Q",-0.127916,range(100,10000,100),5)
        elif numQubits == 10:
            operatorCheck("S2S3","Samples/10Q",-0.0961352,range(100,10000,100),10)
    elif check == "H":
        if numQubits == 3:
            operatorCheck("H","Samples/3Q",-1.000000,range(100,10000,100),3)
        elif numQubits == 4:
            operatorCheck("H","Samples/4Q",-1.616025,range(100,10000,100),4)
        elif numQubits == 5:
            operatorCheck("H","Samples/5Q",-1.927886,range(100,10000,100),5)
        elif numQubits == 10:
            operatorCheck("H","Samples/10Q",-4.258035,range(100,10000,100),10)

RUN("H",4)
