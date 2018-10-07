import matplotlib.pyplot as plt
import numpy as np

def convert(qubit):
    '''
    Converts scalar value of 0 or 1 to corresponding value in ITensor

    PARAMS: qubit (int) - Value of qubit
    RETURNS: int
    '''
    if qubit == 0:
        return 0.5
    else:
        return -0.5

def operatorCheck(folder,expectedValue,listofMs,numQubits):
    '''
    Compare average S2S3 value from samples with value obtained from
    tensor contractions. Creates a plot of error versus samples. This
    will give us an idea of the minimum number of samples to use.

    PARAMS: folder (str) - Name of folder containing Samples.txt
            expectedValue (float) - Expected value of operator
            listofMs (list int) - List of number of samples to try
            numQubits(int) - Number of qubits in quantum system
    RETURNS: None
    '''

    # Read and store samples from sample file
    samples = []
    sampleFile = open("{0}/Samples.txt".format(folder),"r")
    lines = sampleFile.readlines()
    for line in lines:
        samples.append(line.replace(" ","").strip("\n"))
    sampleFile.close()

    total = 0
    values = []
    for i in range(len(samples)):
        total += convert(int(samples[i][1])) * convert(int(samples[i][2]))
        if i in listofMs:
            print(total/(i+1))
            values.append(abs(expectedValue - total/(i+1)))

    fig, ax = plt.subplots()
    plt.plot(listofMs,values,"o")
    plt.xlabel("Number of Samples")
    plt.ylabel("Absolute Value Error")
    plt.title(r"Comparison of $\left \langle \psi \left | S_{2}S_{3} \right" +
              r" |\psi \right \rangle$ with Avg Value from Samples for " +
              "N = {0}".format(numQubits))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(0.55, 0.95, r"$\left \langle \psi \left | S_{2}S_{3} \right" +
             r" |\psi \right \rangle$ = " + str(round(expectedValue,4)),
             transform = ax.transAxes,fontsize = 14,
             verticalalignment = "top",bbox = props)
    plt.tight_layout()
    plt.savefig("OperatorChecks/{0}Q".format(numQubits),dpi = 200)
