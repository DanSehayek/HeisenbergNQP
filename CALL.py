from FrequencyCheck import countCheck
from OperatorCheck import operatorCheck

def RUN(check,numQubits):
    if check == "Frequency":
        countCheck("Samples/{0}Q".format(numQubits))
    elif check == "S2S3":
        operatorCheck("S2S3",range(100,10000,100),numQubits)
    elif check == "H":
        operatorCheck("H",range(100,10000,100),numQubits)

RUN("Frequency",5)
