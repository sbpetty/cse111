def main():
    provinces = file_into_list("provinces.txt")
    
    print(provinces)

    provinces.pop(0)
    provinces.pop()

    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"

    print(f"\nAlberta occurs {provinces.count("Alberta")} times in the modified list.")

def file_into_list(filename):
    list = []

    with open(filename) as file:
        for line in file:
            list.append(line.strip())

    return list

if __name__ == "__main__":
    main()