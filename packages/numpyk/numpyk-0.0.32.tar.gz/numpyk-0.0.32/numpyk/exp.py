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
target_string = "11010110010001100101"
population_size = 100
mutation_rate = 0.01
num_generations = 1000
def generate_individual(length):
    return ''.join(random.choice('01') for _ in range(length))
def calculate_fitness(individual):
    return sum(1 for a, b in zip(individual, target_string) if a == b)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child
def mutate(individual):
    mutated = list(individual)
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = '0' if mutated[i] == '1' else '1'
    return ''.join(mutated)
population = [generate_individual(len(target_string)) for _ in range(population_size)]
for generation in range(num_generations):
    fitness_scores = [calculate_fitness(individual) for individual in population]
    selected_parents = random.choices(population, weights=fitness_scores, k=population_size)
    next_generation = []
    while len(next_generation) < population_size:
        parent1 = random.choice(selected_parents)
        parent2 = random.choice(selected_parents)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)
# Replace the old population with the new generation
        population = next_generation
# Find the best individual in this generation
        best_individual = max(population, key=calculate_fitness)

print(f"Generation {generation}: {best_individual} (Fitness: {calculate_fitness(best_individual)})")
best_individual = max(population, key=calculate_fitness)
print(f"Best Individual: {best_individual} (Fitness: {calculate_fitness(best_individual)})")"""
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

def psoal():
    psoal = """
import numpy as np

class Particle:
    def __init__(self, x0):
        self.position = np.array(x0)
        self.velocity = np.zeros_like(self.position)
        self.best_position = self.position.copy()
        self.best_fitness = float('inf')

    def update_position(self):
        self.position += self.velocity

    def update_velocity(self, global_best_position, w, c1, c2):
        r1, r2 = np.random.rand(len(self.position)), np.random.rand(len(self.position))
        self.velocity = w * self.velocity + c1 * r1 * (self.best_position - self.position) + c2 * r2 * (global_best_position - self.position)

    def evaluate_fitness(self, objective_function):
        self.fitness = objective_function(self.position)
        if self.fitness < self.best_fitness:
            self.best_fitness = self.fitness
            self.best_position = self.position.copy()

def particle_swarm_optimization(objective_function, bounds, num_particles, max_iterations, w, c1, c2):
    particles = [Particle([np.random.uniform(b[0], b[1]) for b in bounds]) for _ in range(num_particles)]
    global_best_position = min(particles, key=lambda p: p.best_fitness).best_position.copy()
    global_best_fitness = min(particles, key=lambda p: p.best_fitness).best_fitness

    for _ in range(max_iterations):
        for particle in particles:
            particle.update_velocity(global_best_position, w, c1, c2)
            particle.update_position()
            particle.evaluate_fitness(objective_function)

            if particle.best_fitness < global_best_fitness:
                global_best_fitness = particle.best_fitness
                global_best_position = particle.best_position.copy()

    return global_best_position, global_best_fitness

# Example usage
def objective_function(x):
    return np.sum(x**2)

bounds = [(-5, 5), (-5, 5), (-5, 5)]  # Variable bounds
num_particles, max_iterations, w, c1, c2 = 20, 100, 0.5, 1.0, 1.0

best_position, best_fitness = particle_swarm_optimization(objective_function, bounds, num_particles, max_iterations, w, c1, c2)

print("Best position:", best_position)
print("Best fitness:", best_fitness)"""
    print(psoal)
    
def PSO(): 
    pso = """
import random

def fitness_function(x):
    return x**2

class Particle:
    def __init__(self):
        self.position = random.uniform(-5, 5) # Initial position within a defined range
        self.velocity = random.uniform(-1, 1) # Initial velocity within a defined range
        self.best_position = self.position # Best position found by the particle
        self.best_fitness = fitness_function(self.position) # Best fitness value

# Main optimization loop
num_particles = 20
max_iterations = 100
global_best_position = None
global_best_fitness = float('inf')
particles = [Particle() for _ in range(num_particles)]

for iteration in range(max_iterations):
    for particle in particles:
        current_fitness = fitness_function(particle.position)
        if current_fitness < particle.best_fitness:
            particle.best_fitness = current_fitness
            particle.best_position = particle.position
        if current_fitness < global_best_fitness:
            global_best_fitness = current_fitness
            global_best_position = particle.position
    
    inertia_weight = 0.7
    cognitive_weight = 1.5
    social_weight = 1.5
    for particle in particles:
        cognitive_component = cognitive_weight * random.random() * (particle.best_position - particle.position)
        social_component = social_weight * random.random() * (global_best_position - particle.position)
        particle.velocity = inertia_weight * particle.velocity + cognitive_component + social_component
        particle.position += particle.velocity

print("Global Best Position:", global_best_position)
print("Global Best Fitness:", global_best_fitness)
"""
    print(pso)

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

def dir(): 
    print("Regression - reg()")
    print("SOM with weights - SOM()")
    print("SOM with dataset - SOMDATA")
    print("Primitive operations on fuzzy - primitive()")
    print("Primitive Hardc - primhard()")
    print("Defuzzification Techniques - defuzz()")
    print("Genetic algorithm - genetic()")
    print("Sugeno Fuzzy Inference System - sugeno()")
    print("Particle Swarm Optimization - PSO()")
    print("PSO Big one - psoal()")
    print("Mamdani Fuzzy Inference system - mamdani()")