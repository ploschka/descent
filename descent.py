import math as m
from scipy.interpolate import CubicSpline as spline
import matplotlib.pyplot as plt
import numpy as np
import decimal as dcm

dcm.getcontext().prec = 100

epsilon = 0.001
results = [
    (dcm.Decimal(-100), dcm.Decimal(7.534424797774636)),
    (dcm.Decimal(-98), dcm.Decimal(5.696333189216324)),
    (dcm.Decimal(-96), dcm.Decimal(3.1835146258186278)),
    (dcm.Decimal(-94), dcm.Decimal(0.3448827414177389)),
    (dcm.Decimal(-92), dcm.Decimal(-2.3960466042407464)),
    (dcm.Decimal(-90), dcm.Decimal(-4.607666190523203)),
    (dcm.Decimal(-88), dcm.Decimal(-5.919003275291804)),
    (dcm.Decimal(-86), dcm.Decimal(-6.079786805614593)),
    (dcm.Decimal(-84), dcm.Decimal(-5.002312956692161)),
    (dcm.Decimal(-82), dcm.Decimal(-2.7784055345863052)),
    (dcm.Decimal(-80), dcm.Decimal(0.3313305731704461)),
    (dcm.Decimal(-78), dcm.Decimal(3.9344157722652917)),
    (dcm.Decimal(-76), dcm.Decimal(7.563904188569079)),
    (dcm.Decimal(-74), dcm.Decimal(10.74741223131181)),
    (dcm.Decimal(-72), dcm.Decimal(13.077056252314003)),
    (dcm.Decimal(-70), dcm.Decimal(14.269442717571447)),
    (dcm.Decimal(-68), dcm.Decimal(14.206415403038774)),
    (dcm.Decimal(-66), dcm.Decimal(12.950285772947446)),
    (dcm.Decimal(-64), dcm.Decimal(10.731278498554463)),
    (dcm.Decimal(-62), dcm.Decimal(7.909282506942583)),
    (dcm.Decimal(-60), dcm.Decimal(4.916022036559534)),
    (dcm.Decimal(-58), dcm.Decimal(2.1868178995878016)),
    (dcm.Decimal(-56), dcm.Decimal(0.09271549579283578)),
    (dcm.Decimal(-54), dcm.Decimal(-1.1163390379090612)),
    (dcm.Decimal(-52), dcm.Decimal(-1.3483733141795025)),
    (dcm.Decimal(-50), dcm.Decimal(-0.680595263715392)),
    (dcm.Decimal(-48), dcm.Decimal(0.6567053726035867)),
    (dcm.Decimal(-46), dcm.Decimal(2.3208631850472066)),
    (dcm.Decimal(-44), dcm.Decimal(3.9155509060041997)),
    (dcm.Decimal(-42), dcm.Decimal(5.0580473061884135)),
    (dcm.Decimal(-40), dcm.Decimal(5.4442518183239095)),
    (dcm.Decimal(-38), dcm.Decimal(4.900998465862166)),
    (dcm.Decimal(-36), dcm.Decimal(3.417238325224382)),
    (dcm.Decimal(-34), dcm.Decimal(1.149014273701727)),
    (dcm.Decimal(-32), dcm.Decimal(-1.6026861647859438)),
    (dcm.Decimal(-30), dcm.Decimal(-4.437802539421297)),
    (dcm.Decimal(-28), dcm.Decimal(-6.919621306093541)),
    (dcm.Decimal(-26), dcm.Decimal(-8.643918593581866)),
    (dcm.Decimal(-24), dcm.Decimal(-9.303901993853595)),
    (dcm.Decimal(-22), dcm.Decimal(-8.74065369619595)),
    (dcm.Decimal(-20), dcm.Decimal(-6.971031076390988)),
    (dcm.Decimal(-18), dcm.Decimal(-4.188507787230684)),
    (dcm.Decimal(-16), dcm.Decimal(-0.7366829270718738)),
    (dcm.Decimal(-14), dcm.Decimal(2.940521030066635)),
    (dcm.Decimal(-12), dcm.Decimal(6.364286086148616)),
    (dcm.Decimal(-10), dcm.Decimal(9.091808422995975)),
    (dcm.Decimal(-8), dcm.Decimal(10.781681656655048)),
    (dcm.Decimal(-6), dcm.Decimal(11.24361149069576)),
    (dcm.Decimal(-4), dcm.Decimal(10.464779796751555)),
    (dcm.Decimal(-2), dcm.Decimal(8.608842491956457)),
    (dcm.Decimal(0), dcm.Decimal(5.987840056419071)),
    (dcm.Decimal(2), dcm.Decimal(3.0115451750183895)),
    (dcm.Decimal(4), dcm.Decimal(0.12229973341539341)),
    (dcm.Decimal(6), dcm.Decimal(-2.2743523323467256)),
    (dcm.Decimal(8), dcm.Decimal(-3.872303478698424)),
    (dcm.Decimal(10), dcm.Decimal(-4.510958393301271)),
    (dcm.Decimal(12), dcm.Decimal(-4.197562640508542)),
    (dcm.Decimal(14), dcm.Decimal(-3.1023795413950968)),
    (dcm.Decimal(16), dcm.Decimal(-1.527623431228919)),
    (dcm.Decimal(18), dcm.Decimal(0.14477907112820965)),
    (dcm.Decimal(20), dcm.Decimal(1.5181720082958114)),
    (dcm.Decimal(22), dcm.Decimal(2.248451084404659)),
    (dcm.Decimal(24), dcm.Decimal(2.1028348399160075)),
    (dcm.Decimal(26), dcm.Decimal(1.0006701299136755)),
    (dcm.Decimal(28), dcm.Decimal(-0.970332018224497)),
    (dcm.Decimal(30), dcm.Decimal(-3.5651330863099306)),
    (dcm.Decimal(32), dcm.Decimal(-6.418045900800262)),
    (dcm.Decimal(34), dcm.Decimal(-9.099344867660804)),
    (dcm.Decimal(36), dcm.Decimal(-11.182914894825533)),
    (dcm.Decimal(38), dcm.Decimal(-12.31426651086173)),
    (dcm.Decimal(40), dcm.Decimal(-12.268149550172984)),
    (dcm.Decimal(42), dcm.Decimal(-10.986603786356227)),
    (dcm.Decimal(44), dcm.Decimal(-8.591339943331953)),
    (dcm.Decimal(46), dcm.Decimal(-5.368367610333075)),
    (dcm.Decimal(48), dcm.Decimal(-1.727143752254811)),
    (dcm.Decimal(50), dcm.Decimal(1.8594801851026173)),
    (dcm.Decimal(52), dcm.Decimal(4.925214586169027)),
    (dcm.Decimal(54), dcm.Decimal(7.079334065821906)),
    (dcm.Decimal(56), dcm.Decimal(8.06401596156578)),
    (dcm.Decimal(58), dcm.Decimal(7.791135789690124)),
    (dcm.Decimal(60), dcm.Decimal(6.3528663143516475)),
    (dcm.Decimal(62), dcm.Decimal(4.004538982336003)),
    (dcm.Decimal(64), dcm.Decimal(1.1225766421971919)),
    (dcm.Decimal(66), dcm.Decimal(-1.855790944996615)),
    (dcm.Decimal(68), dcm.Decimal(-4.501477097990962)),
    (dcm.Decimal(70), dcm.Decimal(-6.460271171440375)),
    (dcm.Decimal(72), dcm.Decimal(-7.50685909063316)),
    (dcm.Decimal(74), dcm.Decimal(-7.577678618527118)),
    (dcm.Decimal(76), dcm.Decimal(-6.77753054393271)),
    (dcm.Decimal(78), dcm.Decimal(-5.359038529343097)),
    (dcm.Decimal(80), dcm.Decimal(-3.6783597014024014)),
    (dcm.Decimal(82), dcm.Decimal(-2.134313948815297)),
    (dcm.Decimal(84), dcm.Decimal(-1.100727108033691)),
    (dcm.Decimal(86), dcm.Decimal(-0.8628566122312336)),
    (dcm.Decimal(88), dcm.Decimal(-1.5681182079779674)),
    (dcm.Decimal(90), dcm.Decimal(-3.1990618396709927)),
    (dcm.Decimal(92), dcm.Decimal(-5.573012732397188)),
    (dcm.Decimal(94), dcm.Decimal(-8.36855847960797)),
    (dcm.Decimal(96), dcm.Decimal(-11.174794223217948)),
    (dcm.Decimal(98), dcm.Decimal(-13.555610946290713)),
    (dcm.Decimal(100), dcm.Decimal(-15.118900474608456)),
]
prediction = {
    's1': dcm.Decimal(-7),
    's2': dcm.Decimal(-3),
    's3': dcm.Decimal(5),
    'c1': dcm.Decimal(-7),
    'c2': dcm.Decimal(-3),
    'c3': dcm.Decimal(5),
    'l1': dcm.Decimal(3),
    'l2': dcm.Decimal(-1),
}

def cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.87758256189
    >>> print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    dcm.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    dcm.getcontext().prec -= 2
    return +s

def sin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)

    """
    dcm.getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    dcm.getcontext().prec -= 2
    return +s


__x = []
__y = []

for result in results:
    __x.append(result[0])
    __y.append(result[1])

spl = spline(__x, __y)

def their_function(x):
    return dcm.Decimal(float(spl(x)))

def our_function(x: dcm.Decimal):
    s1, s2, s3, c1, c2, c3, l1, l2 = prediction.values()
    return s1 * sin(s2 * x + s3) + c1 * cos(c2 * x + c3) + l1 * x + l2

def loss(x):
    a = their_function(x) - our_function(x)
    return a * a

def calculate_gradient(x: dcm.Decimal, y: dcm.Decimal, rate: dcm.Decimal):
    s1, s2, s3, c1, c2, c3, l1, l2 = prediction.values()

    # partial derivative by s1
    ds1 = -2 * sin(s2 * x + s3) * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s1 * x + s3) + y)

    # partial derivative by s2
    ds2 = -2 * s1 * x * cos(s2 * x + s3) * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s2 * x + s3) + y)

    # partial derivative by s3
    ds3 = -2 * s1 * cos(s3 + s2 * x) * (l2 + l1 * x + y + c1 * cos(c3 + c2 * x) - s1 * sin(s3 + s2 * x))

    # partial derivative by c1
    dc1 = 2 * cos(c2 * x + c3) * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s2 * x + s3) + y)

    # partial derivative by c2
    dc2 = -2 * c1 * x * sin(c2 * x + c3) * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s2 * x + s3) + y)

    # partial derivative by c3
    dc3 = -2 * c1 * sin(c2 * x + c3) * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s2 * x + s3) + y)

    # partial derivative by l1
    dl1 = 2 * x * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s2 * x + s3) + y)

    # partial derivative by l2
    dl2 = 2 * (c1 * cos(c2 * x + c3) + l1 * x + l2 - s1 * sin(s2 * x + s3) + y)

    prediction['s1'] += ds1 * rate
    prediction['s2'] += ds2 * rate
    prediction['s3'] += ds3 * rate
    prediction['c1'] += dc1 * rate
    prediction['c2'] += dc2 * rate
    prediction['c3'] += dc3 * rate
    prediction['l1'] += dl1 * rate
    prediction['l2'] += dl2 * rate

rate = dcm.Decimal(0.01)
max_count = 10
count = 0

while True:
    loss_sum = sum([loss(x) for x in __x])
    if loss_sum > epsilon and count < max_count:
        for result in results:
            calculate_gradient(result[0], result[1], rate)
    else:
        break
    count += 1


new_x = np.linspace(-100, 100, 1001)

fig, ax = plt.subplots(2, 1, figsize=(5, 7))
ax[0].plot(__x, __y, 'o')
ax[0].plot(new_x, our_function)

plt.show()

