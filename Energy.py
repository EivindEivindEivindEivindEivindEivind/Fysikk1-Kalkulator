import math

GRAVITY = 9.81

def potential_energy(m, s):
    return m*s * GRAVITY

def kinetick_energy(m, v):
    return 1/2*m*v**2

def kinetick_energy_v(m, e):
    return math.sqrt((2*e)/m)

def v(s, v_0 = 0, my = 1):
    return math.sqrt(2*my*GRAVITY*s+v_0**2)

def s(v, my = 1):
    return (v**2)/(2*my*GRAVITY)

def MY(s, v):
    return ((v**2)/(2*GRAVITY))/s

def work_A(m, v, s):
    return (kinetick_energy(m, v[1]) + potential_energy(m, s[1])) - (kinetick_energy(m, v[0]) + potential_energy(m, s[0]))

def work_F(F, s):
    force = [0, 0]
    for v in F:
        force = [force[0]+v[0], force[1]+v[1]]
    
    return [force[0]*s, force[1]*s]

def elastic(m, v):
    E_k0 = 1/2*m[0] * (v[0][0])**2 + 1/2*m[1] * (v[1][0])**2
    E_k = 1/2*m[0] * (v[0][1])**2 + 1/2*m[1] * (v[1][1])**2

    print(str(E_k) + " - " + str(E_k0))
    return E_k-E_k0

def pressure(force, area):
    return force/area