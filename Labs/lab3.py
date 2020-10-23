import string


class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence:");

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input);

        li = list(self.user_input.split(" "));
        print(li);

        i = 0;
        j = 0;
        print("Total amount of words");
        print(len(li));
        print("Total amount of characters");
        print(len(li[i]));

        print("Test:");
        temp = list(li[i]);
        print(temp);
        character = len(li[i]);

        print("Switching Values:");
        register = temp[1];
        print(register);
        temp[1] = temp[character - 2];
        temp[character - 2] = register;
        print(temp);


scrambler = WordScramble();
scrambler.scramble();
