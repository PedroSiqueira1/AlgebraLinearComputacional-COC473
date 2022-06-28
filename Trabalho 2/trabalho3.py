import numpy as np
import operations as op

def runge_kutta_nystrom(tempo_total, h, m, c, k, vector_a, vector_w):
    def f_normal(t): # returns f(t)
        a1 = vector_a[0]
        a2 = vector_a[1]
        a3 = vector_a[2]

        w1 = vector_w[0]
        w2 = vector_w[1]
        w3 = vector_w[2]
        deg2rad = 1 # np.pi/180
        return a1*np.sin(w1*t*deg2rad) + a2*np.sin(w2*t*deg2rad) + a3*np.cos(w3*t*deg2rad)


    def f_derivada(t, x, dx): # returns ddx aka x''
        return (f_normal(t) - c*dx - k*x)/m


    n_steps = int(tempo_total/h)
    t = 0.0
    dx = x = 0.0 # y'(0) = y(0) = 0.0


    outputs = [
        ("tempo", "deslocamento", "velocidade", "aceleração"),
        (t, x, dx, f_derivada(t, x, dx))
    ]

    for _ in range(n_steps):

        k1 = 0.5*h * f_derivada(t, x, dx)
        q = 0.5*h * (dx + 0.5*k1)

        k2 = 0.5*h * f_derivada((t+h/2), (x+q), (dx+k1))

        k3 = 0.5*h * f_derivada((t+h/2), (x+q), (dx+k2))
        l = h * (dx + k3)
        
        k4 = 0.5*h * f_derivada((t+h), (x+l), (dx+ 2*k3))

        x = x + h*(dx + (k1 + k2 + k3)/3)
        dx = dx + (k1 + 2*k2 + 2*k3 + k4)/3

        t = t + h
        outputs.append((t, x, dx, f_derivada(t, x, dx)))
    return {"result": outputs}


def main(passo=10, tempo_total=60, m=1, c=0.1, k=2, vector_a=np.array([1.0, 2.0, 1.5]), vector_w=np.array([0.05, 1.0, 2.0])):
    
    answer = runge_kutta_nystrom(tempo_total, passo, m, c, k, vector_a, vector_w)
    answer["variables"] = {"trabalho": 3, "passo": passo, "tempo_total": tempo_total, "m": m, "c": c, "k": k, "vector_a": vector_a, "vector_w": vector_w}

    return answer

