from numpy import sin, cos, tan, radians, degrees, array
import scipy.optimize


AZIMUTH = -22.5
PITCH = -28


def fzero(mbr):
    "Nonlinear function of three variables, we'll look for a zero"
    mit, bev, rot = mbr
    return array([
        tan(rot) + sin(bev)*tan(mit),
        sin(radians(PITCH)) + cos(rot)*sin(mit) + sin(bev)*cos(mit)*sin(rot),
        (cos(radians(PITCH))*sin(radians(AZIMUTH)) -
         sin(rot)*sin(mit) + sin(bev)*cos(mit)*cos(rot))
        ])


def fix_degrees(deg):
    "Map a number of degrees to the interval [-180, 180]"
    while deg < -180:
        deg += 360
    while deg > 180:
        deg -= 360
    return deg


if __name__ == "__main__":
    X = scipy.optimize.broyden1(
        fzero,
        [radians(-PITCH), radians(-AZIMUTH), radians(0)],
        f_tol=1e-12)
    M, B, R = (fix_degrees(d) for d in degrees(X))
    print "miter angle: %.4g degrees" % M
    print "bevel angle: %.4g degrees" % B
