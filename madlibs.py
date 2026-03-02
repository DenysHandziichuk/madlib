print("Welcome to the MadLib Generator!\n")

personName = input("Enter a name: ")
adjectiveOne = input("Enter an adjective: ")
placeName = input("Enter a place: ")
pastTenseVerb = input("Enter a past-tense verb: ")
nounOne = input("Enter a noun: ")
adjectiveTwo = input("Enter another adjective: ")
numberOne = float(input("Enter a number: "))
numberTwo = float(input("Enter another number: "))
emotion = input("Enter an emotion: ")

if numberOne == 0:
    averageValue = 0
else:
    averageValue = numberTwo / numberOne

print("\n" + "*" * 60)
print(" " * 15 + "THE UNEXPECTED DAY")
print("*" * 60 + "\n")

story = (
    f"One day, {personName} arrived at {placeName}. It was a very {adjectiveOne} day. "
    f"Out of nowhere, something strange happened — {personName} suddenly {pastTenseVerb} "
    f"right next to a {nounOne}. Everyone nearby became extremely {adjectiveTwo}.\n\n"
    
    f"Later on, a random discussion started about the numbers {numberOne:.2f} and {numberTwo:.2f}. "
    f"When someone divided them, the result was approximately {averageValue:.2f}. "
    f"No one really knew why this mattered, but it somehow made the moment feel important.\n\n"
    
    f"By the end of the day, {personName} felt completely {emotion}. "
    f"And that is how an ordinary visit to {placeName} became unforgettable."
)

print(story)
print("\n" + "*" * 60)