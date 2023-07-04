import add
import data_ip
# from matplotlib import pyplot as plt
# from matplotlib import image as mpimg
menu_options = {
    1: 'add',
    2: 'find',
    3: 'replace',
    4: 'delete',
    5: 'Exit',
}
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


def option1():
    movie_name = input("Enter A Movie : ")
    result = data_ip.search_in_mongo(movie_name)
    if result == 1:
        print('The file exists')
        file = data_ip.read(movie_name)
        with open('templates/newfile5.jpeg', 'wb') as f:
            f.write(file['contents'])
    else:
        res=add.add_movie(movie_name)


def option2():
    movie_name = input("Enter A Movie to search : ")
    res = data_ip.search_to_get_poster(movie_name)
    # image = mpimg.imread(res)
    # plt.imshow(image)
    # plt.show()


def option4():
    movie_name = input("Enter A Movie to delete : ")
    data_ip.delete(movie_name)

def option3():
    movie_name1 = input("Enter A Movie to change : ")
    movie_name2 = input("Enter A Movie  : ")
    data_ip.replace(movie_name1, movie_name2)
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
           option4()
        elif option == 5:
            print('bye bye')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')