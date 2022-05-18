import Trabalho1 as t1
import trabalho2 as t2
import trabalho3 as t3


def file2matrix(matrix_file):
    matrix = []
    line_c = 0
    for line in matrix_file:
        row = line.split(" ")
        
        matrix_line = [float(x) for x in row]
        matrix.append(matrix_line)
    return matrix


def file2vector(vector_file):
    vector = []
    line_c = 0

    for line in vector_file:
        vector.append(float(line))
    return vector


def main():

    input_file = open("inputs.txt", "r")
    
    # Get the variables from inputs.txt
    variables = {}
    for line in input_file:
        line_elements = line.split(":")
        try:
            variables[line_elements[0].strip()] = float(line_elements[1])
        except:
            print(f"Error loading variable {line_elements[0]}, value: {line_elements[1]}")
            output_file = open("out_log.txt", "w")
            output_file.write(f"Unnable to load variable {line_elements[0]}, value: {line_elements[1]}")
            output_file.close()
            return False
    
    trabalho = variables["trabalho"] if ("trabalho" in variables) else 1
    N = variables["N"] if ("N" in variables) else 3
    ICOD = variables["ICOD"] if ("ICOD" in variables) else 3
    IDET = variables["IDET"] if ("IDET" in variables) else 0
    tolM = variables["tolM"] if ("tolM" in variables) else 0.001

    # Getting matrices
    try:
        matrixA_file = open("matrixA.txt", "r")
    except:
        print("File 'matrixA' not found")
        output_file = open("out_log.txt", "w")
        output_file.write("File 'matrixA' not found")
        output_file.close()
        return False
    
    matrix_a = file2matrix(matrixA_file)
    matrixA_file.close()
    
    try:
        vectorB_file = open("vectorB.txt", "r")
    except:
        print("File 'matrixB' not found")
        output_file = open("out_log.txt", "w")
        output_file.write("File 'matrixB' not found")
        output_file.close()
        return False
    
    vector_b = file2vector(vectorB_file)
    matrixA_file.close()



    if trabalho == 1:
        result = t1.main(N=N, ICOD=ICOD, IDET=IDET, matrix_a=matrix_a, matrix_b=vector_b, tolM=tolM)
    
    elif trabalho == 2:
        result = t2.main(n=N, ICOD=ICOD, IDET=IDET, matrix_a=matrix_a, tolM=tolM)

    elif trabalho == 3:
        try:
            points_file = open("points.txt", "r")
        except:
            print("File 'points.txt' not found")
            output_file = open("out_log.txt", "w")
            output_file.write("File 'points.txt' not found")
            output_file.close()
            return False
        
        points = file2matrix(points_file)

        result = t3.main(points)

    else:
        output_file = open("out_log.txt", "w")
        output_file.write(f"Invalid 'trabalho' value, value inserted: {variables['trabalho']}")
        output_file.close()
        return False

    input_file.close()

    print("Files:")
    for key in result:
        print(key)
        output_file = open(f"out_{key}.txt", "w")
        output_file.write(str(result[key]))
        output_file.close()

    
    return True



if __name__ == '__main__':
    main()