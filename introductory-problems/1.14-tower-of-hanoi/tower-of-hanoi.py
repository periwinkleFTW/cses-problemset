# Creating a recursive function  
def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print(source, target)  
        return  
    # function call itself  
    tower_of_hanoi(disks - 1, source, target, auxiliary) 
    print(source, target)  
    tower_of_hanoi(disks - 1, auxiliary, source, target)
  


if __name__ == '__main__':
    disks = int(input()) 

    tower_of_hanoi(disks, '1', '2', '3')  # Calling the function  
