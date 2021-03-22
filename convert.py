"""
Implemented a function.

To make it open source can make rules dict to a public variable in a class called process_text.

... init : input_text

... def change_signs(self , input_text)

... def change_Numbers(self , input_text)

... def change_values(self , input_text)

#Can add more functionality.

"""



rules = {

            "Signs":{
                        "rupees" : "Rs"
                        "dollar" : "$"
                    }

             "Values": {
                         "single":1,
                         "double":2,
                         "tripple":3
                        }

            "Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                    }
    }


def process_text(input_text):

    temp = input_text

    # Decontractions, replace words like below to full words.
    temp = re.sub(r"won't" , "will not" , temp)
    temp = re.sub(r"can\'t" , "cannot" , temp)
    temp = re.sub(r"n\'t" , " not" , temp)
    temp = re.sub(r"\'re" , " are" , temp)
    temp = re.sub(r"\'s" , " is" , temp)
    temp = re.sub(r"\'d" , " would" , temp)
    temp = re.sub(r"\'ll" , " will" , temp)
    temp = re.sub(r"\'t" , " not" , temp)
    temp = re.sub(r"\'ve" , " have" , temp)
    temp = re.sub(r"\'m" , " am" , temp)


    temp = temp.lower()

    #for Signs
    for i in range(rules["Signs"].keys):
        temp = re.sub(i , rules["Signs"][i] , temp)

    #for Numbers
    for i in range(rules["Numbers"].keys):
        temp = re.sub(i , rules["Numbers"][i] , temp)

    #creating Dict for Values
    text_list = temp.split(" ")
    for i in range[len(text_list)]:

        if(text_list[i] in rules["Values"].keys):
            if i == len(text_list) - 1:
                break

            text_list[i+1] =  rules["Values"][i]*text[i+1]
            text_list.remove(i)

    temp = " ".join(for i in text_list)
    return temp


#Sample Call

"""
input_text = input()

print(process_text(input_text))

"""
