from OLAP.gme_cube import GME_Cube


def olap():
    cube = GME_Cube()
    cube.get_gme_table()
    cube.create_cube()
    print("Hierarchies:")
    print(cube.hierarchies)
    print("Measures:")
    print(cube.measures)


if __name__ == "__main__":
    olap()