# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.the_dict = self.add_to_dict();
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.the_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 20px"> HELLO </span>')
        for word in the_dict:
            fo.write("<span style='font-size: "+str(16+(the_dict[word][1]*the_dict[word][1]))+"px'> "+the_dict[word][0]+" </span>");
        fo.write('</div>\
            </body>\
            </html>')

        fo.close()


    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self,):
        the_dict = {};
        # your code goes here
        with open("gettisburg.txt", "r") as f:
            for line in f:
                words = line.split(" ");
                for word in words:
                    if word in the_dict:
                        the_dict[word][1] = the_dict[word][1]+1;
                    else:
                        the_dict[word] = [word, 1];

        return the_dict


wc = WordCloud()
