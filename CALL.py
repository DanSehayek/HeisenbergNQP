from FrequencyCheck import countCheck
from OperatorCheck import operatorCheck

def RUN(check,numQubits):
    if check == "Frequency":
        countCheck("Samples/{0}Q".format(numQubits))
    elif check == "Operator":
        if numQubits == 3:
            operatorCheck("Samples/3Q",-0.166667,range(100,10000,100),3)
        elif numQubits == 4:
            operatorCheck("Samples/4Q",-0.0833333,range(100,10000,100),4)
        elif numQubits == 5:
            operatorCheck("Samples/5Q",-0.127916,range(100,10000,100),5)
        elif numQubits == 10:
            operatorCheck("Samples/10Q",-0.0961352,range(100,10000,100),10)

RUN("Operator",10)
