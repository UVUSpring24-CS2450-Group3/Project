def main():
    with open("tests/Test1.txt", "r") as file:
        rawNumbers = file.read().split("\n")
        intNumbers = []
        print(rawNumbers)
        try:
            for num in rawNumbers:
                intNumbers.append(int(num))
        except:
            print("failed")
        print(intNumbers)
        
        


if __name__ == "__main__":
    main()
