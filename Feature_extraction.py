import cv2
import os


j = 0
# Empty list to store all images
images = []

# loops to transfer each image of Animal file
for filename in os.listdir('Animal'):
    img = cv2.imread(os.path.join('Animal',filename))
    if img is not None:
        img = cv2.resize(img, (250,250))
        img = img.flatten()
        images.append(img)

# loop to transfer each of animal images       
animal = list()
for i in range(len(images[0])):
    animal.append(0)
    for j in images:
        animal[i]+=j[i]     
    animal[i] = animal[i]//len(images)

# Empty list to store all images
images = []

# loops to transfer each image of Machine file
for filename in os.listdir('Machine'):
    img = cv2.imread(os.path.join('Machine',filename))
    if img is not None:
        img = cv2.resize(img, (250,250))
        img = img.flatten()
        images.append(img)

# loop to transfer each of macine images          
machine = list()
for i in range(len(images[0])):
    machine.append(0)
    for j in images:
        machine[i]+=j[i]     
    machine[i] = machine[i]//len(images)


# loop to traverse each image in folder Check_Found 
for filename in os.listdir('Check_Found'):
    img = cv2.imread(os.path.join('Check_Found',filename))
    
    print(filename)
    
    if img is not None:
        img = cv2.resize(img, (250,250))
        img = img.flatten()
        Machine_Sum = 0
        Animal_Sum = 0
        
        for i in range(len(img)):
            Machine_Sum+=abs(machine[i]-img[i])
            Animal_Sum+=abs(animal[i]-img[i])
            
        if Animal_Sum<Machine_Sum:
            print('Animal')
        else:
            print('Machine')
