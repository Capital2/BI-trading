from OLAP.gme_cube import GME_Cube


def olap():
    cube = GME_Cube()
    cube.get_gme_table()
    cube.create_cube()


if __name__ == "__main__":
    olap()