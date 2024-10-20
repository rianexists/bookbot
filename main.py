def words(file):
    return len(file.split())

def chars(file):
    frequency = {}
    for char in file:
        try:
            frequency[char.lower()] += 1
        except:
            frequency[char.lower()] = 1
    return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

def main():
#    path = input("Please enter the path to your text")
    path = "texts/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

    print(f"--- Begin report of {path} ---")
    print(f"{words(file_contents)} words found in the document")
    print(f"{len(file_contents)} characters found in the document")
    print()
    for i in chars(file_contents).items():
        print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")

main()