# Problem-1 Simulator For Cell Organization
This is a simulator for cell organization in a mobile wireless system where a user should be able to take various input factors in the cell system and find out the desired output.
 
### Input Factor:
* Area size to cover
* Cell type: Macrocell, Microcell
* Radius of each cell
* Total number of frequencies allotted to the system
* Frequency reuse factor, N = I2 + J2 + (I * J); where I, J = 0, 1, 2, 3…

### Output:
* Number of cells required
* Number of channels per cell
* Total channel capacity
* Total number of possible concurrent call


# Problem-2 The Okumura/Hata model to predict the path loss
This is a basic python Gui design to give some input and find out the path loss of a system.

### Input Facotor:
* fc = carrier frequency in MHz from 150 to 1500 MHz  
* ht = height of transmitting antenna (base station) in m, from 30 to 300 m
* hr = height of receiving antenna (mobile unit) in m, from 1 to 10 m
* d = propagation distance between antennas in km, from 1 to 20 km
* City size = Small/Medium, Large 
* Area type: Urban/Suburban, Open area

### Output: 
* Predicted path loss in dB.
