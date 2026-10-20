def main():
    my_list = ["h", "e", "l", "l", "o"]
    print(my_list)
    # I see the letters being printed with quatation marks, and they are in the same order.

    my_list.append("!")
    print(my_list)
    # I see an exclamation mark was added, right next to the letters. The original had only the leters, but this includes an exclamation mark.

    print(len(my_list))
    # There are 6 elements in this list.

    print(my_list[4:6])
    # I see 'o' and '!' being printed, as o is the fourth element, and we don't have a 6th element, so it chose the exclamation mark, the last element.

    print(my_list[4:])
    # I see this list being printed twice; it is the same elements.

    print(my_list[-2:])
    # This prints the exact same thing, and it is useful to show the difference betgween elements 4 and 6.

    my_list.remove("l")
    print(my_list)
    # I noticed one of the L's was removed, as there were two. The second one was removed, and the first one stayed.

    my_list.insert(2, "l")
    print(my_list)
    # It added another L, and I did expect it to be at element two, which replaced the first L.

    del my_list[0]
    print(my_list)
    # The element H got removed, as it was the first element.

    last_item = my_list.pop()
    print(last_item)
    print(my_list)
    # The exclamation mark was moved down a line. Additionally, the exclamation mark is not at the end of the element list.

    print(my_list[2])
    # L is printed on a seperate line.

    print("!" in my_list)
    # It is false because the exclamation mark was moved out of the main list.

    my_list.sort(reverse=True)
    print(my_list)
    # The list is now sorted backward, alternating the element order. It was returned.

    print(sorted(my_list))
    print(my_list)
    # It is printed twice, once in the original, and once in the reverse way.

    my_tuple = ("red", "green", "blue")
    print(my_tuple)
    # Red, green, and blue are printed and are in the tuple.

    print(my_tuple[0])
    print(my_tuple[-1])
    # Red and blue were printed, and negative works as it will give the last element.

    # my_tuple[1] = "yellow"
    # The code does not run, and the error I got is that the tuple object does not support item assignment.

    one_item = ("hello",)
    print(one_item)
    # I noticed this just posted hello in quotations and a comma.

    colors = ("red", "blue", "red", "green", "red")
    print(colors.count("red"))
    # There are three red entries.

    print(colors.index("green"))
    # In the tuple, green is in the third position.

    my_set = {"apple", "banana", "cherry"}
    print(my_set)
    # The order does not match as I have typed, as these are unordered.

    my_set.add("orange")
    print(my_set)
    # Orange is now added to the end of the set.

    # my_set.add("banana")
    # print(my_set)
    # There is now an error, as banana is already there, and you cannot have two instances of one element.

    my_set.remove("apple")
    print(my_set)
    # Apple is now gone.

    my_set.discard("pear")
    # There was not an error, and nothing printed, because the element pear does not exist.

    tropical = {"banana", "mango", "papaya"}
    all_fruits = my_set.union(tropical)
    print(all_fruits)
    # There are no duplicates, but the items included are cherry, orange, papaya, banana, and mango.

    my_dict = {"name": "Sam", "age": 16, "grade": "11th"}
    print(my_dict)
    # The name and value, age and value, and grade and value are printed.

    print(my_dict["age"])
    # The value returned is 16.

    # print(my_dict["school"])
    # I got an error, as school is not an element previously in our dictionary.

    my_dict["grade"] = "12th"
    print(my_dict)
    # The value of the grade updated to 12th.

    my_dict["school"] = "Central High"
    print(my_dict)
    # The new key and value are school and Central High.

    del my_dict["age"]
    print(my_dict)
    # The age key and value is now missing.

    print(my_dict.get("locker"))
    # There was not an error, but the word "None" was printed.

    for key, value in my_dict.items():
        print(key, "->", value)
    # There are three lines now, giving the index and the value, per each line. This is much easier to read now, as it is much more polished and better developed.

























if __name__ == "__main__":
    main()
