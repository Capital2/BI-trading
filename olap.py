from OLAP.market_activity_cube import MarketActivityCube


def olap():
    ma_cube = MarketActivityCube()
    ma_cube.get_table()
    ma_cube.create_cube()
    
    print("Hierarchies:")
    print(ma_cube.hierarchies)
    print("Measures:")
    print(ma_cube.measures)


if __name__ == "__main__":
    olap()