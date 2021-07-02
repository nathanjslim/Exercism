def recite(start_verse, end_verse):
    day_verse = ["and a Partridge in a Pear Tree.",
                 "two Turtle Doves, ",
                 "three French Hens, ",
                 "four Calling Birds, ",
                 "five Gold Rings, ",
                 "six Geese-a-Laying, ",
                 "seven Swans-a-Swimming, ",
                 "eight Maids-a-Milking, ",
                 "nine Ladies Dancing, ",
                 "ten Lords-a-Leaping, ",
                 "eleven Pipers Piping, ",
                 "twelve Drummers Drumming, "
                 ]

    day_word = {1: "first",
                2: "second",
                3: "third",
                4: "fourth",
                5: "fifth",
                6: "sixth",
                7: "seventh",
                8: "eighth",
                9: "ninth",
                10: "tenth",
                11: "eleventh",
                12: "twelfth"
                }

    fixed_verse = ("On the " + day_word[end_verse] + " day of Christmas my true love gave to me: ")

    fin_recite = ""

    if end_verse == 1:
        fin_recite += 'a Partridge in a Pear Tree.'
    else:
        for i in range(end_verse - 1, start_verse - 2, -1):
            fin_recite += day_verse[i]

    return [fixed_verse + fin_recite]
