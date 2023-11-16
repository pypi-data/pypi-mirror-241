def reg(): 
    reg = """
import math
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder , MinMaxScaler
from sklearn.feature_selection import VarianceThreshold , chi2 , SelectKBest


#Data Imputation
print("- Label Encode Non-Numerical features")
print()

labelencoder = LabelEncoder()

for col in df.columns:
  if df[col].dtype == "object":
    df[col] = labelencoder.fit_transform(df[col])
    print(" ",col," :\t",len(labelencoder.classes_))
print()


X = df["cl_name1"]
Y = df["cl_name2"]

num , den = 0 , 0 

mean_x = X.mean()
mean_y = Y.mean()

for i , x in enumerate(X):
  y = Y[i]
  num += (x-mean_x) * (y-mean_y)
  den += (x-mean_x) ** 2

b1 = num/den
b0 = mean_y - (b1 * mean_x)

print("bo : ",b0," | b1 : ",b1)

pred = lambda x,b0,b1 : b0 + (b1 * x)

#Performance
ssr = 0
sst = 0

mean_y = Y.mean()

for i,y in enumerate(Y):
  x = X[i]
  ssr += ((y - pred(x,b0,b1)) ** 2)
  sst += (y - mean_y) ** 2

print("rss : ",ssr)
n    = len(Y)
rmse = math.sqrt(ssr/n)

print("rmse : ",rmse)

#plot
plt.figure()
plt.scatter(X, Y, color = 'red', alpha=0.5)

plt_y = b0 + (b1 * np.linspace(0, 1.0))
plt.plot(np.linspace(0, 1.0),plt_y, color = 'b')
plt.xlabel("Schooling")
plt.ylabel("Life expectancy")

plt.show()"""
    print(reg)


def SOM(): 
    SOM = """
import numpy as np
import math

def CalculateDistance(inputs, weights):
    sum = 0
    for x in range(0, len(weights)):
        value = weights[x] - inputs[x]
        sum += value * value
        print("Weight", sum)
        return sum
    
def UpdateWeights(inputs, weights, l):
    weight_update = np.array([0.0,0.0,0.0,0.0], dtype='float')
    print(weights, l, inputs, weights)
    weight_update = weights + (l * (inputs - weights))
    return weight_update

def train(inputs, weights, l):
    run = True
    epoch = 0
    wt_update = np.array([0.0,0.0,0.0,0.0], dtype = 'float')
    while run:
        print("-----------------------")
        epoch += 1
        
        for x in range(0, len(inputs)):
            value = 0
            vector = 0
            for y in range(0, len(weights)):
                print("input", inputs[x])
                print('weights', weights[x])
                a_output = CalculateDistance(inputs[x], weights[y])
                print('Distance', y, ":", a_output)
                print()
                if value == 0:
                    value = a_output
                    vector = y
                elif a_output < value:
                    value = a_output
                    vector = y
        print('Winner for iteration', x, 'Distance', value, "weight vector", vector + 1)
        wt_update = UpdateWeights(inputs[x], weights[vector], l)
        weights[vector] = wt_update 
        print("Weight Update for vector", vector + 1, wt_update)
        print("update weigths", weights)
    l = l * 0.5
    if epoch >=2:
        run = False
    else:
        run = True

x = np.array([[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]], dtype='float')
w = np.array([[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]], dtype='float')
l = 0.6

train(x, w, l)"""
    print(SOM)


def SOMDATA(): 
    Somda = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.preprocessing import MinMaxScaler
def som_ini(ipt1,ipt2):
  data=df.values
  som_shape = (ipt1, ipt2)

  som = MiniSom(som_shape[0], som_shape[1], data.shape[1], sigma=0.5, learning_rate=0.5)

  max_iter = 1000
  q_error = []
  t_error = []

  for i in range(max_iter):
      rand_i = np.random.randint(len(data))
      som.update(data[rand_i], som.winner(data[rand_i]), i, max_iter)
      q_error.append(som.quantization_error(data))
      t_error.append(som.topographic_error(data))

  plt.plot(np.arange(max_iter), q_error, label='quantization error')
  plt.plot(np.arange(max_iter), t_error, label='topographic error')
  plt.ylabel('Quantization error')
  plt.xlabel('Iteration index')
  plt.legend()
  plt.show()

  winner_coordinates = np.array([som.winner(x) for x in data]).T
  cluster_index = np.ravel_multi_index(winner_coordinates, som_shape)
  plt.figure(figsize=(10,8))
  for c in np.unique(cluster_index):
      plt.scatter(data[cluster_index == c, 0],
                  data[cluster_index == c, 1], label='cluster='+str(c), alpha=.7)
  for centroid in som.get_weights():
      plt.scatter(centroid[:, 0], centroid[:, 1], marker='x', 
                  s=10, linewidths=20, color='k')
  plt.legend();
  som_ini(1,5)"""
    print(Somda)

def primitive():
    prim = """
import numpy as np

def fuzzy_operation(A, B, operation):
    result = {}
    for key in A:
        A_value, B_value = A[key], B[key]
        result[key] = operation(A_value, B_value)
    return result

A = {"hi": 0.2, "hel": 0.3, "lo": 0.6, "ll": 0.6}
B = {"hi": 0.9, "hel": 0.9, "lo": 0.4, "ll": 0.5}

# Fuzzy union
union_result = fuzzy_operation(A, B, lambda a, b: max(a, b))
print("Union:", union_result)

# Fuzzy intersection
intersection_result = fuzzy_operation(A, B, lambda a, b: min(a, b))
print("Intersection:", intersection_result)

# Fuzzy complement
complement_result = fuzzy_operation(A, A, lambda a, _: 1 - a)
print("Complement:", complement_result)

# Fuzzy difference
difference_result = fuzzy_operation(A, B, lambda a, b: min(a, 1 - b))
print("Difference:", difference_result)"""
    print(prim)


def defuzz():
    defuz = """
import pandas as pd
import numpy as np
fuzzy_set = np.array([0.8,0.6,1.0,1.2,1.6,0.5])

# Center of Sums Method (COS)
def defuzzify_cos(fuzzy_set):
    return np.sum(fuzzy_set * np.arange(len(fuzzy_set))) / np.sum(fuzzy_set)

# Center of Gravity (COG) / Centroid of Area (COA) Method
def defuzzify_cog(fuzzy_set):
    return np.sum(fuzzy_set * np.arange(len(fuzzy_set))) / np.sum(fuzzy_set)

# Center of Area / Bisector of Area Method (BOA)
def defuzzify_boa(fuzzy_set):
    return np.argmax(fuzzy_set)  # Assuming BOA returns the position of the maximum membership degree

# Weighted Average Method
def defuzzify_weighted_average(fuzzy_set):
    values = np.arange(len(fuzzy_set))
    return np.sum(fuzzy_set * values) / np.sum(fuzzy_set)

# Maxima Methods
def defuzzify_fom(fuzzy_set):
    return np.argmax(fuzzy_set)  # Position of the first maximum

def defuzzify_lom(fuzzy_set):
    return len(fuzzy_set) - 1 - np.argmax(fuzzy_set[::-1])  # Position of the last maximum

def defuzzify_mom(fuzzy_set):
    max_positions = np.where(fuzzy_set == np.max(fuzzy_set))
    return np.mean(max_positions)


print("Center of Sums Method (COS):", defuzzify_cos(fuzzy_set))
print("Center of Gravity (COG) / Centroid of Area (COA) Method:", defuzzify_cog(fuzzy_set))
print("Center of Area / Bisector of Area Method (BOA):", defuzzify_boa(fuzzy_set))
print("Weighted Average Method:", defuzzify_weighted_average(fuzzy_set))
print("First of Maxima Method (FOM):", defuzzify_fom(fuzzy_set))
print("Last of Maxima Method (LOM):", defuzzify_lom(fuzzy_set))
print("Mean of Maxima Method (MOM):", defuzzify_mom(fuzzy_set))"""
    print(defuz)

def mamdani():
    mam = """
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('fan_speed_dataset.csv')

# Membership Functions for Temperature
def cold(temp):
    return max(0, min(1, (20 - temp) / 10))

def medium(temp):
    return max(0, min(1, (temp - 10) / 10, (30 - temp) / 10))

def hot(temp):
    return max(0, min(1, (temp - 20) / 10))

# Membership Functions for Fan Speed
def slow(speed):
    return max(0, min(1, (50 - speed) / 25))

def med(speed):
    return max(0, min(1, (speed - 25) / 25, (75 - speed) / 25))

def fast(speed):
    return max(0, min(1, (speed - 50) / 25))

# Mamdani Fuzzy Inference System
def mamdani_FIS(temp):
    # Rule Evaluation
    r1 = cold(temp)
    r2 = medium(temp)
    r3 = hot(temp)

    # Aggregation
    aggregated = [max(min(r1, slow(speed)), min(r2, med(speed)), min(r3, fast(speed))) for speed in range(101)]

    # Defuzzification (using centroid method)
    numerator = sum([speed * membership for speed, membership in enumerate(aggregated)])
    denominator = sum(aggregated)

    return numerator / denominator if denominator != 0 else 0

# Apply the Mamdani FIS to the dataset
df['Predicted Fan Speed'] = df['Temperature'].apply(mamdani_FIS)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['Temperature'], df['Observed Fan Speed'], color='blue', label='Observed Fan Speed', alpha=0.6)
plt.plot(df['Temperature'], df['Predicted Fan Speed'], 'r-', label='Predicted Fan Speed')
plt.xlabel('Temperature (°C)')
plt.ylabel('Fan Speed (RPM)')
plt.title('Observed vs. Predicted Fan Speed')
plt.legend()
plt.grid(True)
plt.show()"""
    print(mam)

def genetic():
    gen = """
import random

# Define the fitness function
def fitness(x):
    return 2*x - 0.5

# Define the chromosome representation
def int_to_bin(x):
    return bin(x)[2:].zfill(5)

# Define the chromosome decoding
def bin_to_int(bin_str):
    return int(bin_str, 2)

# Define the initial population
population = [int_to_bin(x) for x in range(32)]

# Calculate fitness for each chromosome
fitness_values = [fitness(bin_to_int(chromosome)) for chromosome in population]

# Find the optimum value of x wherein f(x) will take minimum value
optimum_x = min(range(32), key=lambda x: fitness(x))
print("Optimum value of x: ", optimum_x)

# Calculate average fitness
average_fitness = sum(fitness_values) / len(fitness_values)
print("Average fitness: ", average_fitness)

# Calculate fitness ratio
fitness_ratio = [fitness_values[i] / sum(fitness_values) for i in range(len(fitness_values))]
print("Fitness ratio: ", fitness_ratio)

# Convert selected chromosomes to integer equivalent
selected_chromosomes = [5, 29, 9, 18, 31, 1]

# Apply two-point crossover and mutation
for i in range(0, len(selected_chromosomes), 2):
    parent1 = int_to_bin(selected_chromosomes[i])
    parent2 = int_to_bin(selected_chromosomes[i+1])
    crossover_point1 = random.randint(1, 2)
    crossover_point2 = random.randint(4, 5)
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:]
    child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:]
    mutation_point = 4
    if random.random() < 0.5:
        child1 = child1[:mutation_point] + str(int(child1[mutation_point]) ^ 1) + child1[mutation_point+1:]
    else:
        child2 = child2[:mutation_point] + str(int(child2[mutation_point]) ^ 1) + child2[mutation_point+1:]
    print("Parent 1: ", selected_chromosomes[i], " Chromosome: ", parent1)
    print("Parent 2: ", selected_chromosomes[i+1], " Chromosome: ", parent2)
    print("Child 1: ", bin_to_int(child1), " Chromosome: ", child1)
    print("Child 2: ", bin_to_int(child2), " Chromosome: ", child2)

# Calculate average fitness of the new generation
new_generation = [child1, child2]
new_fitness_values = [fitness(bin_to_int(chromosome)) for chromosome in new_generation]
new_average_fitness = sum(new_fitness_values) / len(new_fitness_values)
print("New generation average fitness: ", new_average_fitness)"""
    print(gen)


def sugeno():
    sugenofis = """
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Load dataset
data_url = 'dataset.csv'  # Replace with your dataset link
data = pd.read_csv(data_url)

# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 61, 1), 'humidity')
output = ctrl.Consequent(np.arange(0, 26, 1), 'output', defuzzify_method='centroid')

# Generate fuzzy membership functions
temperature.automf(3)
humidity.automf(3)
output['low'] = fuzz.trimf(output.universe, [0, 5, 10])
output['medium'] = fuzz.trimf(output.universe, [10, 15, 20])
output['high'] = fuzz.trimf(output.universe, [15, 20, 25])

# Define rules using Sugeno-type fuzzy inference
rule1 = ctrl.Rule(temperature['poor'] & humidity['poor'], output['low'])
rule2 = ctrl.Rule(temperature['average'] & humidity['average'], output['medium'])
rule3 = ctrl.Rule(temperature['good'] & humidity['good'], output['high'])

# Create control system
output_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
output_simulation = ctrl.ControlSystemSimulation(output_ctrl)

# Simulation
test_temp = 28
test_humidity = 37

output_simulation.input['temperature'] = test_temp
output_simulation.input['humidity'] = test_humidity
output_simulation.compute()

print(f"For Temperature: {test_temp} and Humidity: {test_humidity}, the Output is: {output_simulation.output['output']}")

# Plot membership functions and results
temperature.view()
humidity.view()
output.view(sim=output_simulation)
plt.show()"""
    print(sugenofis) 

def pso():
    psoal = """
import random

# Objective function to maximize
def objective_function(x):
    return 1 + 2*x - x**2

# Initialize control parameters
w = 0.70
c1 = 0.20
c2 = 0.60
n = 5

iterations = 5

# Initialize particles with random positions and velocities
particles = []
for i in range(n):
    position = random.uniform(-10, 10)
    velocity = random.uniform(-1, 1)
    particle = {'position': position, 'velocity': velocity, 'local_best_position': position, 'local_best_fitness': objective_function(position)}
    particles.append(particle)

# Initialize global best position and fitness
global_best_position = particles[0]['position']
global_best_fitness = particles[0]['local_best_fitness']

# Update particles for 2 iterations
r1 = [0.4, 0.8, 0.3, 0.5, 0.5]
r3 = [0.5, 0.8, 0.8, 0.7, 0.1]

for iteration in range(iterations):
    for i, particle in enumerate(particles):
        # Update velocity
        particle['velocity'] = w*particle['velocity'] + c1*r1[i]*(particle['local_best_position'] - particle['position']) + c2*r3[i]*(global_best_position - particle['position'])

        # Update position
        particle['position'] = particle['position'] + particle['velocity']

        # Update local best position and fitness
        fitness = objective_function(particle['position'])
        if fitness > particle['local_best_fitness']:
            particle['local_best_position'] = particle['position']
            particle['local_best_fitness'] = fitness

        # Update global best position and fitness
        if fitness > global_best_fitness:
            global_best_position = particle['position']
            global_best_fitness = fitness

# Print results
print('Local Best Position:', [particle['local_best_position'] for particle in particles])
print('Local Best Fitness:', [particle['local_best_fitness'] for particle in particles])
print('Global Best Position:', global_best_position)
print('Global Best Fitness:', global_best_fitness)"""
    print(psoal)
    


def primhard():
    primh = """
import numpy as np

def fuzzy_union(A, B):
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
 
        if A_value > B_value:
            Y[A_key] = A_value
        else:
            Y[B_key] = B_value
    print("Union:", Y)

def fuzzy_intersection(A,B):
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
 
        if A_value < B_value:
            Y1[A_key] = A_value
        else:
            Y1[B_key] = B_value
    print("Intersection", Y1)

def fuzzy_compliment(A):
    for A_key in A:
        y2[A_key]= 1-A[A_key]
    print("compliment", y2)

        
def fuzzy_difference(A, B):
    for A_key, B_key in zip(A, B):
        A_value = A[A_key]
        B_value = B[B_key]
        B_value = 1 - B_value
 
        if A_value < B_value:
            Y3[A_key] = A_value
        else:
            Y3[B_key] = B_value
    print("Difference", Y3) 

A = {"hi": 0.2, "hel": 0.3, "lo": 0.6, "ll": 0.6}
B = {"hi": 0.9, "hel": 0.9, "lo": 0.4, "ll": 0.5}
Y = dict()
Y1 = dict()
y2 = dict()
Y3 = dict()
while True:
    print("Which operation you want to choose\n1. Union\n2. Intersection\n3. Compliment\n4. Difference\n5. Exit")
    user = int(input())

    if user == 1:
        fuzzy_union(A, B)
    elif user == 2:
        fuzzy_intersection(A, B)
    elif user == 3:
        fuzzy_compliment(A)
    elif user == 4:
        fuzzy_difference(A, B)
    elif user == 5:
        break
    else:
        continue

"""
    print(primh)
def sugenoweight():
    sug = """
import numpy as np
import skfuzzy as fuzz

# Define the universe of discourse
x_height = np.arange(0, 201, 1)
x_age = np.arange(0, 201, 1)
x_health = np.arange(0, 101, 1)

# Define the fuzzy sets
height_poor = fuzz.trimf(x_height, [0, 0, 100])
height_average = fuzz.trimf(x_height, [0, 100, 200])
height_good = fuzz.trimf(x_height, [100, 200, 200])

age_poor = fuzz.trimf(x_age, [0, 0, 100])
age_average = fuzz.trimf(x_age, [0, 100, 200])
age_good = fuzz.trimf(x_age, [100, 200, 200])

# Input specific values for height and age
test_height = 199
test_age = 45

# Define the rules (Sugeno-style)
def rule1(height, age):
    return 0.2 * height + 0.8 * age

def rule2(height, age):
    return 0.5 * height + 0.5 * age

def rule3(height, age):
    return 0.8 * height + 0.2 * age

# Calculate the rule activations
activation_rule1 = np.fmin(fuzz.interp_membership(x_height, height_poor, test_height),
                            fuzz.interp_membership(x_age, age_poor, test_age))
activation_rule2 = np.fmin(fuzz.interp_membership(x_height, height_average, test_height),
                            fuzz.interp_membership(x_age, age_average, test_age))
activation_rule3 = np.fmin(fuzz.interp_membership(x_height, height_good, test_height),
                            fuzz.interp_membership(x_age, age_good, test_age))

# Calculate the weighted output
output = (rule1(test_height, test_age) * activation_rule1 +
          rule2(test_height, test_age) * activation_rule2 +
          rule3(test_height, test_age) * activation_rule3)

# Normalize the output
total_activation = activation_rule1 + activation_rule2 + activation_rule3
output = np.sum(output) / np.sum(total_activation)

# Print the result
print(f"For Height: {test_height} cm and Age: {test_age} years, the Predicted Health is: {output}")

if output > 80:
  print("Health : Good")
elif output < 80 or output > 40:
  print("Health : Normal")
else:
  print("Health : Low")
"""
    print(sug)

def mamdaniweigths():
    mamd = """
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define linguistic variables and their membership functions
height = ctrl.Antecedent(np.arange(0, 11, 1), 'Height')
weight = ctrl.Antecedent(np.arange(0, 101, 1), 'Weight')
health = ctrl.Consequent(np.arange(0, 101, 1), 'Health')

# Define linguistic values for Height
height['short'] = fuzz.trimf(height.universe, [0, 0, 5])
height['medium'] = fuzz.trimf(height.universe, [0, 5, 10])
height['tall'] = fuzz.trimf(height.universe, [5, 10, 10])

# Define linguistic values for Weight
weight['low'] = fuzz.trimf(weight.universe, [0, 0, 50])
weight['medium'] = fuzz.trimf(weight.universe, [0, 50, 100])
weight['high'] = fuzz.trimf(weight.universe, [50, 100, 100])

# Define linguistic values for Health
health['low'] = fuzz.trimf(health.universe, [0, 0, 50])
health['normal'] = fuzz.trimf(health.universe, [0, 50, 100])
health['good'] = fuzz.trimf(health.universe, [50, 100, 100])

# Define rules
rule1 = ctrl.Rule(height['short'] & weight['low'], health['low'])
rule2 = ctrl.Rule(height['medium'] & weight['high'], health['normal'])
rule3 = ctrl.Rule(height['tall'] & weight['medium'], health['good'])
rule4 = ctrl.Rule(height['tall'], health['good'])

# Create a control system
health_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
health_simulation = ctrl.ControlSystemSimulation(health_ctrl)

# Set input values
health_simulation.input['Height'] = 10  # Example short height
health_simulation.input['Weight'] = 90  # Example low weight

# Compute the result
health_simulation.compute()

# Print the output
print("Crisp output 'Health':", health_simulation.output['Health'])
"""
    print(mamd)

def SLP():
    slp = """
import numpy as np

X1 = np.array([0.5, 0.6, 0.5])
X2 = np.array([0.7, 0.3, 0.4])
target = np.array([1, 0, 1])
w1 = -0.4
w2 = 0.4
threshold = 0.2
learning_rate = 0.1
max_iterations = 10

for iteration in range(max_iterations):
    for i in range(len(X1)):
        # Calculate the weighted sum
        weighted_sum = w1 * X1[i] + w2 * X2[i]

        # Apply the threshold
        output = 1 if weighted_sum > threshold else 0

        # Update weights
        w1 = w1 + learning_rate * (target[i] - output) * X1[i]
        w2 = w2 + learning_rate * (target[i] - output) * X2[i]

# Print the final weights
print("Final weights:")
print("w1 =", w1)
print("w2 =", w2)
"""
    print(slp)

def defuzzt():
    fuz = """
import numpy as np
import matplotlib.pyplot as plt

#membership function
membership_function =[(0,0.1),(1,0.5),(2,0.8),(3,0.6),(4,0.2)]

#inputs and membership degrees
inputs, membership_degrees = zip(*membership_function)

#inputs and membership degrees to Numpy Arrays
inputs = np.array(inputs)
membership_degrees = np.array(membership_degrees)

#max-membership
max_membership_index = np.argmax(membership_degrees)
max_membership = inputs[max_membership_index]

#centroid
centroid = np.sum(inputs * membership_degrees)/np.sum(membership_degrees)

#weighted average
weights = [0.1,0.2,0.4,0.2,0.1]
weighted_avg = np.sum(inputs *membership_degrees *weights) / np.sum(membership_degrees * weights)

#mean max
mean_max = np.mean(inputs[membership_degrees == max_membership])

#center of sums (same as centroid)
center_of_sums = centroid

#center of largest area
sorted_indices = np.argsort(membership_degrees)[::-1][:2]
center_of_largest_area = np.mean(inputs[sorted_indices])

#first of maxima
first_max_index = np.argmax(membership_degrees == np.max(membership_degrees))
first_max = inputs[first_max_index]

#last of maxima
last_max_indices = np.where(membership_degrees == np.max(membership_degrees))[0]
last_max_index = last_max_indices[-1]
last_max = inputs[last_max_index]


#create bar graph
methods = ["Max-Membership", "Centroid", "Weighted Average", "Mean-max","Center of sums", "center of largest area","first-max","last-max"]
results = [max_membership, centroid, weighted_avg, mean_max, center_of_sums,center_of_largest_area, first_max,last_max]


plt.figure(figsize=(10,6))
plt.barh(methods,results)
plt.xlabel("Defuzzification Value")
plt.title("Defuzzification Methods")
plt.grid(axis="x", linestyle='--', alpha=0.6)
plt.gca().invert_yaxis()
plt.show()

"""
    print(fuz)
def dir(): 
    print("Regression - reg(), SLP()")
    print("SOM with weights - SOM(), SOMDATA()")
    print("Primitive operations on fuzzy - primitive(), primhard()")
    print("Defuzzification Techniques - defuzz(), defuzzt()")
    print("Genetic algorithm - genetic()")
    print("Sugeno Fuzzy Inference System - sugeno(), sugenoweight")
    print("Particle Swarm Optimization - pso()")
    print("Mamdani Fuzzy Inference system - mamdani(), mamdaniweigths()")
