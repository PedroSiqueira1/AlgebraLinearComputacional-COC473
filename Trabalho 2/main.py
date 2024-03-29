﻿import trabalho1 as t1
import trabalho2 as t2
import trabalho3 as t3
import re
import numpy as np


def line2array(vector_str):
    strvalues_list = vector_str.split(" ")
    
    vector_lst = [float(re.sub('[^(0-9|\-|\.)]','', x)) for x in strvalues_list]
    
    np_arr = np.array(vector_lst)

    return np_arr


def main():

    input_file = open("inputs.txt", "r")
    
    # Get the variables from inputs.txt
    variables = {}
    for line in input_file:
        if ":" in line:
            line_elements = line.split(":")
            
            key = re.sub('[^(A-Z|a-z\_)|0-9]', '', line_elements[0].strip())
            value = re.sub('[^(\.|\s|\-|0-9)]', '', line_elements[1].strip())
            if key in {"vector_a", "vector_w", "vector_c"}:
                variables[key] = value # value is still a string here
            
            else:
                try:
                    variables[key] = float(value)
                except:
                    print(f"Error loading variable {key}, value: {value}, line: {line}")
                    output_file = open("outputs.txt", "w")
                    output_file.write(f"Unnable to load variable {key}, value: {value}")
                    output_file.close()
                    return False

    input_file.close()

    # VARIALBES
    print(variables)
    # global
    trabalho = variables["trabalho"] if ("trabalho" in variables) else 1
    icod = variables["ICOD"] if ("ICOD" in variables) else 3
    method = variables["method"] if ("method" in variables) else 0
    tolM = variables["tolM"] if ("tolM" in variables) else 0.001
    max_iter = int(variables["max_iter"]) if ("max_iter" in variables) else 10000

    # trabalho1
    theta1 = variables["theta1"] if ("theta1" in variables) else 0.5
    theta2 = variables["theta2"] if ("theta2" in variables) else 0.5

    # trabalho2
    vector_c = line2array(variables["vector_c"]) if ("vector_c" in variables) else np.array([1.0, 1.0, 1.0, 1.0])
    a = variables["a"] if ("a" in variables) else 100
    b = variables["b"] if ("b" in variables) else -100
    n = variables["n"] if ("n" in variables) else 2
    
    # trabalho 3
    passo = variables["passo"] if "passo" in variables else 1
    tempo_total = variables["tempo_total"] if "tempo_total" in variables else 10
    m = variables["m"] if "m" in variables else 1
    c = variables["c"] if "c" in variables else 0.1
    k = variables["k"] if "k" in variables else 2
    vector_a = line2array(variables["vector_a"]) if "vector_a" in variables else np.array([1.0, 2.0, 1.5])
    vector_w = line2array(variables["vector_w"]) if "vector_w" in variables else np.array([0.05, 1.0, 2.0])

    if trabalho == 1:
        result = t1.main(icod, theta1, theta2, tolM, max_iter)
    
    elif trabalho == 2:
        result = t2.main(icod, method, vector_c, a, b, n, tolM, max_iter)

    elif trabalho == 3:
        result = t3.main(passo, tempo_total, m, c, k, vector_a, vector_w)

    else:
        output_file = open("outputs.txt", "w")
        output_file.write(f"ERROR: Invalid 'trabalho' value, inserted: {trabalho}")
        output_file.close()
        return False


    output_file = open(f"outputs.txt", "w")

    for key in result:
        output_file.write("\n\n" + str(key) + ":\n")
        if type(result[key]) == list:
            for value in result[key]:
                output_file.write(str(value)+"\n")

        elif type(result[key]) == dict:
            for value in result[key]:
                output_file.write(str(value) + ": " + str(result[key][value])+"\n")

        else:
            output_file.write(str(result[key]))
    
    output_file.close()

    
    return True



if __name__ == '__main__':
    main()