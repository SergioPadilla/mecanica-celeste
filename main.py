"""
Created at 1/12/16
__author__ = 'Sergio Padilla'
"""
from Algorithm import get_planets_list
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if __name__ == '__main__':
    planets = get_planets_list()
    axis_x = []
    axis_y = []
    axis_z = []
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    for planet in planets:
        print('Momento angular NR: ', planet.angular_moment_newton_raphson(50))
        print('Momento angular Bessel: ', planet.angular_moment_bessel(50))
        print('u NR: ', planet.get_u_newton_raphson(50))
        print('u Bessel: ', planet.get_u_bessel(50))
        print('distancia al sol NR: ', planet.distance_sun_newton_raphson(50))
        print('distancia al sol Bessel: ', planet.distance_sun_bessel(50))
        print('area NR (0,50): ', planet.area_newton_raphson(0, 50))
        print('area Bessel (0,50): ', planet.area_bessel(0, 50))
        for i in range(0, int(planet.period+1)+10):
            position = planet.get_pos_newton_raphson(i)
            axis_x.append(position[0])
            axis_y.append(position[1])
            axis_z.append(position[2])

        ax.plot(axis_x, axis_y, axis_z)
        axis_x = []
        axis_y = []
        axis_z = []

    ax.set_xlim3d(-40, 40)
    ax.set_ylim3d(-40, 40)
    ax.set_zlim3d(-40, 40)

    plt.show()
