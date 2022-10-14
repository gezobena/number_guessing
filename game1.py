import random
import time

computer_guessed_number=random.randint(1,100)
continue_game=True
user_guesses=[]
start_time=time.time()
while(continue_game):
    user_guess=int(input("Uzmini skaitli starp 1 un 100: "))
    user_guesses.append(user_guess)
    
    if user_guess==computer_guessed_number:
        print("Tu uzvarēji!")
        continue_game=False
    elif user_guess<computer_guessed_number:
        print("Vairāk")
    elif user_guess>computer_guessed_number:
        print("Mazāk")
    else:
        print("Notikusi kļūda")
sum_of_difference=0
for n in user_guesses:
    sum_of_difference += abs(n-computer_guessed_number)
ave_of_difference=sum_of_difference/len(user_guesses)
print(f"Vidējā starpība bija {ave_of_difference}")

print("Tu spēlēji %s sekundes" % (time.time()-start_time))
