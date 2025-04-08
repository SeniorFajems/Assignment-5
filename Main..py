import random

def bubble_sort(A):
    n = len(A)
    swap = True
    while swap:
        swap = False
        for i in range(0, n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swap = True
        n = n - 1
    return A

def binary_search(lst,key):
    low=0
    high=len(lst)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==lst[mid]:
            found=True
        elif key>lst[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        return mid
    else:
        return None
    

def main():
    while True:
        try:
            lenght = int(input("Enter an integer between 10 and 20: "))
            if 10 <= lenght <= 20:
                break
            print("Invalid input! Enter a number between 10 and 20.")
        except ValueError:
            print("Please enter a valid integer.")

  
    numbers = [random.randint(1, 100) for i in range(lenght)]
    sorted_numbers = bubble_sort(numbers)
    print(sorted_numbers)

    min_range = max(0, min(sorted_numbers) - 5)
    max_range = max(sorted_numbers) + 5
    print(f"Number range: {min_range} to {max_range}")
    guess_limit=12
    attempts=0
    while True:
        attempts_left=guess_limit-attempts
        score=max(10-attempts,0)
        
        try:
            guess = int(input("Guess a number in the list (-1 to quit): "))
            if guess == -1:
                print("Game over!")
                break
            
            if attempts<guess_limit:
                if binary_search(sorted_numbers, guess):
                    print("Congratulations! The number is in the list.")
                    print(F"Your score is {score}/10")
                    break
                else:
                    print("Your number is not in the list, try again.")
                    print(F"You have {attempts_left-1} left")
                attempts=attempts+1

            else:
                print("You have finished your guess attempts")
                print(F"Your score is {score}/10")
                print("Game Over!")
                break
        except ValueError:
            print("Please enter a valid integer.")


main()