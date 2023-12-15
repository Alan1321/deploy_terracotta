import terracotta as tc

def generate_database(datas, db_name):
    driver = tc.get_driver(db_name)

    key_names = ('type', 'date', 'band')
    driver.create(key_names)

    rasters = {}
    for keys, value in datas.items():
        arg = keys.split('+') 
        rasters[(f'{arg[0]}',f'{arg[1]}',f'{arg[2]}')] = value

    for keys, raster_file in rasters.items():
        print(keys, raster_file)
        driver.insert(keys, raster_file)

    print(f"{db_name} database generated.")
