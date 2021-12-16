from numpy import array, linspace
import matplotlib as mpl
import matplotlib.pyplot as plt
from constants import *

E2=m
E3=2*m
E4=3*m

p1x = 0
p1y = 0
p1z = m/2
p4x = m/100
p4y = m/100
p4z = m/2.1

p2x = -m/200
p2y = -m/200
p2z =  m/2000
p3x = m/200
p3y = m/200
p3z = m/1000

I = 0+1j

def getMid(E1=m):
    return \
    - \
    (((E3 + m)*p2x + (E2 + m)*p3x)*((E4 + m)*p1x + (E1 + m)*p4x)) \
    + \
    ((E2 + m)*(E3 + m) + p2x*p3x + (p2y + I*p2z)*(p3y - I*p3z)) \
    * \
    ((E1 + m)*(E4 + m) + p1x*p4x + (p1y + I*p1z)*(p4y - I*p4z)) \
    - \
    (m*p2y + E3*(p2y + I*p2z) + I*m*p2z + E2*p3y + m*p3y - I*(E2 + m)*p3z) \
    * \
    (m*p1y + E4*(p1y + I*p1z) + I*m*p1z + E1*p4y + m*p4y - I*(E1 + m)*p4z) \
    - \
    (E3*((-I)*p2y + p2z) + E2*(I*p3y + p3z) + m*((-I)*p2y + p2z + I*p3y + p3z)) \
    * \
    (E4*((-I)*p1y + p1z) + E1*(I*p4y + p4z) + m*((-I)*p1y + p1z + I*p4y + p4z))

def getOld(E1=m):
    return (-(((E3 + m)*p2x + (E2 + m)*p3x)*((E4 + m)*p1x + (E1 + m)*p4x)) +
            ((E2 + m)*(E3 + m) + p2x*p3x + (p2y + I*p2z)*(p3y - I*p3z))*((E1 +
                m)*(E4 + m) + p1x*p4x + (p1y + I*p1z)*(p4y - I*p4z)) - (m*p2y +
                    E3*(p2y + I*p2z) + I*m*p2z + E2*p3y + m*p3y - I*(E2 +
                        m)*p3z)*(m*p1y + E4*(p1y + I*p1z) + I*m*p1z + E1*p4y +
                            m*p4y - I*(E1 + m)*p4z) - (E3*((-I)*p2y + p2z) +
                                E2*(I*p3y + p3z) + m*((-I)*p2y + p2z + I*p3y +
                                    p3z))*(E4*((-I)*p1y + p1z) + E1*(I*p4y +
                                        p4z) + m*((-I)*p1y + p1z + I*p4y +
                                            p4z)))

def getNew(E1=m):
    return \
    + \
    ((E2 + m)*(E3 + m) + p2x*p3x + (p2y + I*p2z)*(p3y - I*p3z)) \
    * ((E1 + m)*(E4 + m) + I*p1z*(p4y - I*p4z)) \
    - \
    (E1 + m)*p4x*((E3 + m)*p2x + (E2 + m)*p3x) \
    - \
    2*(E2 + m)*(E4 + m)*I*p1z*(p3y - I*p3z) \
    - \
    2*(E1 + m)*(E3 + m)*(p2y + I*p2z)*(p4y - I*p4z)

def getCode(E1=m):
    return \
    (E1 + m)*((E3 + m)*p2x + (E2 + m)*p3x)*p4x\
    +(m*p2y + E3*(p2y + 1j*p2z) + 1j*m*p2z\
        +E2*p3y + m*p3y - 1j*(E2 + m)*p3z)\
    *(1j*E4*p1z + 1j*m*p1z + E1*p4y\
        +m*p4y - 1j*(E1 + m)*p4z)\
    -((E2 + m)*(E3 + m) + p2x*p3x\
        +(p2y + 1j*p2z)*(p3y - 1j*p3z))\
    *((E1 + m)*(E4 + m) + p1z*(1j*p4y + p4z))\
    +(E3*((-1j)*p2y + p2z) + E2*(1j*p3y + p3z)\
        +m*((-1j)*p2y + p2z + 1j*p3y + p3z))\
    *(E4*p1z + E1*(1j*p4y + p4z)\
    +m*(p1z + 1j*p4y + p4z))

#     - \
#     (((E3 + m)*p2x + (E2 + m)*p3x) \
#     *((E4 + m)*p1x + (E1 + m)*p4x)) \
#     + \
#     ((E2 + m)*(E3 + m) + p2x*p3x + (p2y + I*p2z)*(p3y - I*p3z)) \
#     *((E1 + m)*(E4 + m) + p1x*p4x + (p1y + I*p1z)*(p4y - I*p4z)) \
#     - \
#     2*(E2 + m)*(p3y - I*p3z) \
#     *(E4 + m)*(p1y + I*p1z) \
#     - \
#     2*(E3 + m)*(p2y + I*p2z) \
#     *(E1 + m)*(p4y - I*p4z) \

#     (E1 + m)*(E2 + m)*(E3 + m)*(E4 + m) \
#     - \
#     2*(E1 + m)*(E3 + m)*(p2y + I*p2z)*(p4y - I*p4z) \
#     + \
#     (E1 + m)*(E4 + m)*(p2y + I*p2z)*(p3y - I*p3z) \
#     + \
#     (E2 + m)*(E3 + m)*(p1y + I*p1z)*(p4y - I*p4z) \
#     - \
#     2*(E2 + m)*(E4 + m)*(p1y + I*p1z)*(p3y - I*p3z) \
#     - \
#     (E1 + m)*(E2 + m)*p3x*p4x \
#     - \
#     (E1 + m)*(E3 + m)*p2x*p4x \
#     + \
#     (E1 + m)*(E4 + m)*p2x*p3x \
#     + \
#     (E2 + m)*(E3 + m)*p1x*p4x \
#     - \
#     (E2 + m)*(E4 + m)*p1x*p3x \
#     - \
#     (E3 + m)*(E4 + m)*p1x*p2x \
#     + \
#     p1x*p2x*p3x*p4x \
#     + \
#     p1x*p4x*(p2y + I*p2z)*(p3y - I*p3z) \
#     + \
#     p2x*p3x*(p1y + I*p1z)*(p4y - I*p4z) \
#     + \
#     (p1y + I*p1z)*(p2y + I*p2z)*(p3y - I*p3z)*(p4y - I*p4z) 

#     (p2y + I*p2z)*(p3y - I*p3z)*(p1y + I*p1z)*(p4y - I*p4z) \
#     + \
#     p2x*p3x*p1x*p4x \
#     + \
#     (E2 + m)*(E3 + m)*(E1 + m)*(E4 + m) \
#     + \
#     (E2 + m)*(E3 + m)*(p1y + I*p1z)*(p4y - I*p4z) \
#     + \
#     (E1 + m)*(E4 + m)*(p2y + I*p2z)*(p3y - I*p3z) \
#     + \
#     (E2 + m)*(E3 + m)*p1x*p4x \
#     + \
#     (E1 + m)*(E4 + m)*p2x*p3x \
#     + \
#     p2x*p3x*(p1y + I*p1z)*(p4y - I*p4z) \
#     + \
#     p1x*p4x*(p2y + I*p2z)*(p3y - I*p3z) \
#     - \
#     ((E3 + m)*p2x + (E2 + m)*p3x) \
#     *((E4 + m)*p1x + (E1 + m)*p4x) \
#     - \
#     2 \
#     *(E2 + m)*(p3y - I*p3z) \
#     *(E4 + m)*(p1y + I*p1z) \
#     - \
#     2 \
#     *(E3 + m)*(p2y + I*p2z) \
#     *(E1 + m)*(p4y - I*p4z)

#     (E2 + m)*(E3 + m)*(p1y + I*p1z)*(p4y - I*p4z) \
#     + \
#     (E1 + m)*(E4 + m)*(p2y + I*p2z)*(p3y - I*p3z) \
#     + \
#     (E2 + m)*(E3 + m)*p1x*p4x \
#     + \
#     (E1 + m)*(E4 + m)*p2x*p3x \
#     + \
#     p2x*p3x*(p1y + I*p1z)*(p4y - I*p4z) \
#     + \
#     p1x*p4x*(p2y + I*p2z)*(p3y - I*p3z) \
#     - \
#     ((E3 + m)*p2x + (E2 + m)*p3x) \
#     *((E4 + m)*p1x + (E1 + m)*p4x) \
#     - \
#     2 \
#     *(E2 + m)*(p3y - I*p3z) \
#     *(E4 + m)*(p1y + I*p1z) \
#     - \
#     2 \
#     *(E3 + m)*(p2y + I*p2z) \
#     *(E1 + m)*(p4y - I*p4z)

#     - \
#     2*(E1 + m)*(E3 + m)*(p2y + I*p2z)*(p4y - I*p4z) \
#     + \
#     (E1 + m)*(E4 + m)*(p2y + I*p2z)*(p3y - I*p3z) \
#     + \
#     (E2 + m)*(E3 + m)*(p1y + I*p1z)*(p4y - I*p4z) \
#     - \
#     2*(E2 + m)*(E4 + m)*(p1y + I*p1z)*(p3y - I*p3z) \
#     - \
#     (E1 + m)*(E2 + m)*p3x*p4x \
#     - \
#     (E1 + m)*(E3 + m)*p2x*p4x \
#     + \
#     (E1 + m)*(E4 + m)*p2x*p3x \
#     + \
#     (E2 + m)*(E3 + m)*p1x*p4x \
#     - \
#     (E2 + m)*(E4 + m)*p1x*p3x \
#     - \
#     (E3 + m)*(E4 + m)*p1x*p2x \
#     + \
#     p1x*p4x*(p2y + I*p2z)*(p3y - I*p3z) \
#     + \
#     p2x*p3x*(p1y + I*p1z)*(p4y - I*p4z)


