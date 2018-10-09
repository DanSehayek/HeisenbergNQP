import matplotlib.pyplot as plt
import numpy as np


def transform(sample,j,operator):
    '''
    Transforms a given sample based on specified set of raising and
    lowering operators. Transformed state can be used to obtain
    corresponding amplitude coefficient in local estimator.

    :param sample: Sample for which value of observable is being determined.
    :type sample: str
    :param j: Subscript of first spin observable.
    :type j: int
    :param operator: The observable to be measured.
                     One of "S+S-" "S-S+".
    :type operator: str

    :returns: Transformed sample after applying two spin observable.
    :rtype: str
    '''
    newSample = list(sample)
    if operator == "S+S-":
        newSample[j] = "1"
        newSample[j+1] = "0"
    elif operator == "S-S+":
        newSample[j] = "0"
        newSample[j+1] = "1"
    return "".join(newSample)

def convert(operator,sample,amplitudes):
    '''
    Calculates the value of an observable corresponding to a given
    spin configuration.

    :param operator: The observable to be measured.
                     One of "S2S3" "SzSz" "S+S-" "S-S+".
    :type operator: str
    :param sample: Sample for which value of observable is being determined.
    :type sample: str
    :param amplitudes: List of amplitudes corresponding to quantum state.
    :type amplitudes: listof float

    :returns: Value of the observable corresponding to the given sample.
    :rtype: float
    '''
    total = 0
    org = amplitudes[int(sample,2)]
    if operator == "S2S3":
        for i in range(len(sample)-1):
            if i == 1:
                if sample[i:i+2] == "00" or sample[i:i+2] == "11":
                    total += 0.25
                else:
                    total += -0.25
    elif operator == "SzSz":
        for i in range(len(sample)-1):
            if sample[i:i+2] == "00" or sample[i:i+2] == "11":
                total += 0.25
            else:
                total += -0.25
    elif operator == "S+S-":
        for i in range(len(sample)-1):
            if sample[i:i+2] == "01":
                total += amplitudes[int(transform(sample,i,"S+S-"),2)]/org
    elif operator == "S-S+":
        for i in range(len(sample)-1):
            if sample[i:i+2] == "10":
                total += amplitudes[int(transform(sample,i,"S-S+"),2)]/org

    return total

def operatorCheck(operator,folder,expectedValue,listofMs,numQubits):
    '''
    Compares average value of observable from samples with expected value
    from tensor contractions. Creates a plot of error versus number of samples.
    This will verify that the simulator is working and will give us an idea
    of the minimum number of samples to use.

    :param operator: The observable to be measured.
                     One of "S2S3" and "H".
    :type operator: str
    :param folder: Name of folder containing samples file.
                   Sample file must be named "Samples.txt".
    :type folder: str
    :param expectedValue: Expected value of observable calculated
                          from ITensor.
    :type expectedValue: float
    :param listofMs: List of number of samples to try.
    :type listofMs: listof int
    :param numQubits: Number of qubits comprising the quantum system.
    :type numQubits: int

    :returns: None
    '''

    # Read and store samples from sample file
    samples = []
    sampleFile = open("{0}/Samples.txt".format(folder),"r")
    lines = sampleFile.readlines()
    for line in lines:
        samples.append(line.replace(" ","").strip("\n"))
    sampleFile.close()

    # Read and store amplitudes from amplitudes file
    amplitudes = []
    amplitudeFile = open("{0}/Amplitudes2.txt".format(folder),"r")
    lines = amplitudeFile.readlines()
    for line in lines:
        amplitudes.append(float(line.split(" ")[0]))
    amplitudeFile.close()

    total = 0
    values = []
    for i in range(len(samples)):
        if operator == "S2S3":
            total += convert("SzSz",samples[i],amplitudes)
        elif operator == "H":
            total += convert("SzSz",samples[i],amplitudes)
            total += 0.5 * convert("S+S-",samples[i],amplitudes)
            total += 0.5 * convert("S-S+",samples[i],amplitudes)
        if i in listofMs:
            print(total/(i+1))
            values.append(abs(expectedValue - total/(i+1))/abs(expectedValue))

    fig, ax = plt.subplots()
    plt.plot(listofMs,values,"o")
    plt.xlabel("Number of Samples")
    plt.ylabel("Relative Error")
    plt.title(r"Accuracy Plot of $\left \langle \psi \left | H \right" +
              r" |\psi \right \rangle$ for " +
              "N = {0}".format(numQubits))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(0.55, 0.95, r"$\left \langle \psi \left | S_{2}S_{3} \right" +
             r" |\psi \right \rangle$ = " + str(round(expectedValue,4)),
             transform = ax.transAxes,fontsize = 14,
             verticalalignment = "top",bbox = props)
    plt.tight_layout()
    plt.savefig("OperatorChecks/{0}Q".format(numQubits),dpi = 200)
