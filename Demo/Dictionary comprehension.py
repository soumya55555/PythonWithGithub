courses=["python","java","selenium"]
length={course:len(course)for course in courses}
print(length)

long_word="stupendufentabularfantastic"
letter_count={letter:long_word.count(letter)for letter in long_word}
print(letter_count)

my_fav={
    "Fruit":"Mango",
    "Flower":"Rose",
    "Hero":"Salman",
    "Coke":"Thumps up",
    "Colour":"Black"

}
favo={key:value for key,value in my_fav.items() if key.startswith("C")}
print(favo)

channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}
def stations_to_numbers(dic):
    channel_with_numbers={value:key for key,value in dic.items()}
    return channel_with_numbers

print(stations_to_numbers(channels))

