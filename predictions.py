import random

# name of the file to read in
PREDICTIONS_LIST = 'predictions_list.txt'


# get a prediction from a list
def get_prediction():
    created_list = []
    with open(PREDICTIONS_LIST) as file:
        # give lines one at a time
        for line in file:
            # strip removes whitespace at the start or end
            created_list.append(line.strip())
    return created_list


# generate a random prediction
def random_prediction(prediction):
    # comes with 'import random'
    return random.choice(prediction)


def show_prediction():
    prediction = get_prediction()
    print(random_prediction(prediction))


# main code to show the prediction to the user
def main():
    # ask for a user name
    user_name = input('Enter your name: ')
    while user_name == '':
        user_name = input('Please enter your name: ')
    print('Hello ' + user_name.title() + '!')
    show_prediction()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
