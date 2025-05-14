from colorama import Fore, init
import emoji
init()
inputuser = int(input("1 happy \n2 sad \n3 excited \n4 tired  \nhi!! , how are u:"))
if inputuser == 1:
    print(emoji.emojize(Fore.YELLOW + "HAPPY!!:grinning_face:"))
elif inputuser ==2:
    print(emoji.emojize(Fore.BLUE + "ITS SAD..:downcast_face_with_sweat:"))
elif inputuser ==3:
    print(emoji.emojize(Fore.RED + "ITS GOOD IF U EXCITED!!..:cowboy_hat_face:"))
elif inputuser ==4:
    print(emoji.emojize(Fore.GREEN + "tired:tired_face:"))
else:
    print("bro u print smthing wrong!!")
    
            