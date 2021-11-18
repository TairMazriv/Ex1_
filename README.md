# Ex1_:
1. https://github.com/meatfighter/knuth-elevator
https://towardsdatascience.com/elevator-optimization-in-python-73cab894ad30
http://www.columbia.edu/~cs2035/courses/ieor4405.S13/p14.pdf
Our problem space is to build an efficient algorithm given a list of elevator calls in the building.
In the algorithm we would like to insert for each call an elevator that will perform the call in the shortest time. 

2. Offline Algorithm:
We will define in each building an array that represents the current location of each elevator. The index of the elevator in the array represents the location of that elevator at that given time.
In addition, an array of arrays was constructed. In each location in a particular index in the large array will appear all the floors where the elevator with the same index stops.
An auxiliary function is built that calculates the time it will take for an elevator to get from the floor where it is located to the floor where a call appears.
In the algorithm itself we will go over all the call in the loop,
If there's one elevator in the building, we'll put all the calls to it.
If there is more than one elevator in the building, we will go through another loop on all the elevators in the building and insert the fastest elevator.
If the call up, we will check on all the elevators that are currently on the floor lower than the source of the call who will perform the call the fastest using the auxiliary function. For all elevators that are currently on a floor higher than the original floor of the call we will set a random time. At the end we will select the shortest time and place for the same call the elevator that will perform the call in the shortest time.
If the call down, we will check on all the elevators that are currently on the floor higher than the source of the call who will perform the call the fastest using the auxiliary function. For all elevators that are currently on a floor lower than the original floor of the call we will set a random time. At the end we will select the shortest time and place for the same call the elevator that will perform the call in the shortest time.
After we have selected the elevator we will add the source floor and destination floor of the call to the list of floors where the elevator stops it. 

uml:

![image](https://user-images.githubusercontent.com/80627174/142486356-65bf6873-1625-4a57-8173-4f7056571629.png)
