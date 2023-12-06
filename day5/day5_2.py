with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()


    seeds = []
    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    flag, flag1,flag2,flag3, flag4, flag5, flag6 = False, False, False, False, False, False, False

    for line in lines:


        if line.startswith("seeds"):
            _, seeds = line.split(":")
            seeds = seeds.strip()
            seeds = list(map(int, seeds.split()))


        elif line.startswith("seed-to"):
            flag = True
            continue
        if flag and line!="":
            start, end, ranges = map(int, line.split())

            seed_to_soil[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag = False




        elif line.startswith("soil-to"):
            flag2 = True
            continue
        if flag2 and line!="":
            start, end, ranges = map(int, line.split())

            soil_to_fertilizer[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag2 = False



        elif line.startswith("fertilizer-to"):
            flag3 = True
            continue
        if flag3 and line!="":
            start, end, ranges = map(int, line.split())

            fertilizer_to_water[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag3 = False



        elif line.startswith("water-to"):
            flag4 = True
            continue
        if flag4 and line!="":
            start, end, ranges = map(int, line.split())

            water_to_light[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag4 = False




        elif line.startswith("light-to"):
            flag5 = True
            continue
        if flag5 and line!="":
            start, end, ranges = map(int, line.split())

            light_to_temperature[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag5 = False



        elif line.startswith("temperature-to"):
            flag6 = True
            continue
        if flag6 and line!="":
            start, end, ranges = map(int, line.split())

            temperature_to_humidity[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag6 = False



        elif line.startswith("humidity-to"):
            flag1 = True
            continue
        if flag1 and line!="":
            start, end, ranges = map(int, line.split())

            humidity_to_location[(start, start+ranges)] = [end, end+ranges]
            # print(line)
            # continue
        if line=="":
            flag1 = False


    # print(seeds)
    # print(seed_to_soil)
    # print(soil_to_fertilizer)
    # print(fertilizer_to_water)
    # print(water_to_light)
    # print(light_to_temperature)
    # print(temperature_to_humidity)
    # print(humidity_to_location)

    # seeds_2 = []
    #
    # for i in range(0, len(seeds), 2):
    #     for j in range(seeds[i], seeds[i] + seeds[i+1]):
    #         seeds_2.append(j)

    # print(seeds_2)

    # seeds = seeds_2

    # print(seeds)



    seed_data = {}

    for t in range(0, len(seeds), 2):
        for i in range(seeds[t], seeds[t] + seeds[t + 1]):
            flag = False
            for j in seed_to_soil:
                if seed_to_soil[j][0] <= i <= seed_to_soil[j][1]:
                    diff = i - seed_to_soil[j][0]
                    seed_data[i] = [j[0] + diff]
                    flag = True
                    break

            if not flag:
                seed_data[i] = [i]

    for relation_dict in [soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]:
        for i in seed_data:
            flag = False
            for j in relation_dict:
                if relation_dict[j][0] <= seed_data[i][-1] <= relation_dict[j][1]:
                    diff = seed_data[i][-1] - relation_dict[j][0]
                    seed_data[i].append(j[0] + diff)
                    flag = True
                    break

            if not flag:
                seed_data[i].append(seed_data[i][-1])

        del relation_dict

    min_value = min(seed_data.values(), key=lambda x: x[-1])[-1]
    print(f'min is {min_value}')