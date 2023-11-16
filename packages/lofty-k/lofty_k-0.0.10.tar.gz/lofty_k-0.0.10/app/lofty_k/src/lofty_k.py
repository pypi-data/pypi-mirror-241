

def help():
    print("SLP, MLP, SOM, Fuzzy, d_fuzzy, mam, sugo, genetic, pso, regression")

def SLP():
    xml="""
import pandas
import numpy as np
from sklearn.preprocessing import LabelEncoder
LabelEncoder = LabelEncoder()
df = pandas.read_csv("Iris1.csv")
df
-------------------------------------------
for i in df.columns:
    if i in df.select_dtypes("object").columns:
        df[i] = LabelEncoder.fit_transform(df[i])
print(df)
--------------------------------------------
for i in df.columns:
    df[i].fillna(df[i].mean(), inplace = True)
df.isnull().sum()
--------------------------------------------
input_dim = 6
Weights = np.random.rand(input_dim)
#Weights[0] = 0.5
#Weights [1] = 0.5
#Weights [2] = 0.5
er = []
w = []
l = [0,0.1,0.2]
for i in l:
    learning_rate = i
    e = []
    Training_Data = df.copy(deep=True)
    Expected_Output = Training_Data.Species
    Training_Data = Training_Data.drop(['Species'], axis=1)
    Training_Data = np.asarray(Training_Data)
    training_count = len(Training_Data[:,0])
    for epoch in range(0,5):
        for datum in range(0, training_count):
            Output_Sum = np.sum(np.multiply(Training_Data[datum, :], Weights))
            if Output_Sum < 0:
                Output_Value = 0
            else:
                Output_Value = 1
            error = Expected_Output[datum] - Output_Value
            e.append(error)
            for n in range(0, input_dim):
                Weights[n] = Weights[n] + learning_rate * error * Training_Data[datum,n]
    er.append(e)
    w.append(Weights)
----------------------------------------------------
min_er = []
for i in er:
    c = 0
    for j in i:
        c += abs(j)
    min_er.append(c)

for i in range(len(min_er)):
    if min_er[i] == min(min_er):
        print(l[i])
        print(w[i])
---------------------------------------------------------
import matplotlib.pyplot as plt

plt.plot(er[0])
plt.show()
plt.plot(er[1])
plt.show()
plt.plot(er[2])
plt.show()
-------------------------------------------------------------
import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return self.activation_function(summation)

    def train(self, training_data, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Example dataset: OR gate
training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 1, 1, 1])

input_size = 2
learning_rate = 0.1
epochs = 100

perceptron = Perceptron(input_size, learning_rate, epochs)
perceptron.train(training_data, labels)

# Test the trained perceptron
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for inputs in test_data:
    prediction = perceptron.predict(inputs)
    print(f"Input: {inputs}, Prediction: {prediction}")
    """

    print(xml)

def MLP():
    xml="""
import numpy as np
import pandas as pd

# Load data
data=pd.read_csv('Toyato.csv')

data.head()
--------------------------------------------
from sklearn import preprocessing

# Creating labelEncoder
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
data['Mfg_Month']=le.fit_transform(data['Mfg_Month'])
data['Mfg_Year']=le.fit_transform(data['Mfg_Month'])
# Spliting data into Feature and
X=data[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'Departments', 'salary']]
y=data['left']

# Import train_test_split function
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # 70% training and 30% test
# Import MLPClassifer
from sklearn.neural_network import MLPClassifier

# Create model object
clf = MLPClassifier(hidden_layer_sizes=(6,5),
                    random_state=5,
                    verbose=True,
                    learning_rate_init=0.01)

# Fit data onto the model
clf.fit(X_train,y_train)
---------------------------------------------------
import matplotlib.pyplot as plt

plt.plot(clf.loss_curve_)
plt.xlabel("No. of itrerations")
plt.ylabel("Training Error")
plt.show()
-----------------------------------------------
# Make prediction on test dataset
ypred=clf.predict(X_test)

# Import accuracy score
from sklearn.metrics import accuracy_score

# Calcuate accuracy
print("Accuracy Score: ", accuracy_score(y_test,ypred))
    """
    print(xml)

def SOM():
    xml="""
import pandas as pd
iris_df=pd.read_csv('/content/Iris.csv')
iris_df
-----------------------------------
X = iris_df.drop('Species', axis=1)
import matplotlib.pyplot as plt

plt.scatter(X['SepalLengthCm'], X['SepalWidthCm'])
plt.xlabel('SepalLengthCm')
plt.ylabel('SepalWidthCm')
plt.show()
--------------------------------------
pip install minisom
-------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import silhouette_score

# Load the dataset
data = pd.read_csv('/content/Iris.csv')

# Preprocessing: remove target variable
X = data.iloc[:, :-1].values

# Feature Scaling
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Determine optimal number of clusters using elbow method
distortions = []
for i in range(1, 11):
    som = MiniSom(x = 10, y = 10, input_len = 5, sigma = 1.0, learning_rate = 0.5)
    som.random_weights_init(X)
    som.train_random(data = X, num_iteration = 100)
    labels = np.zeros(len(X))
    for j, x in enumerate(X):
        w = som.winner(x)
        labels[j] = w[0] * 10 + w[1]
    distortions.append(silhouette_score(X, labels, metric='euclidean'))

# Plot elbow curve
plt.plot(range(1, 11), distortions)
plt.title('Elbow Curve')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()
----------------------------------------------------
# Optimal number of clusters based on elbow method
n_clusters = 3

# Apply SOM clustering
som = MiniSom(x = 10, y = 10, input_len = 5, sigma = 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)

# Get cluster labels
labels = np.zeros(len(X))
for i, x in enumerate(X):
    w = som.winner(x)
    labels[i] = w[0] * 10 + w[1]

# Print and plot cluster centroids and labels
centroids = som.get_weights()
plt.figure(figsize=(10, 10))
for i, x in enumerate(X):
    w = som.winner(x)
    plt.plot(w[0], w[1], marker='o', color='black'.format(labels[i]), markersize=12)
plt.scatter(centroids[:,:,0], centroids[:,:,1], color='k', s=100, linewidths=3, zorder=10)
plt.title('SOM Clustering ({} clusters)'.format(n_clusters))
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()

# Repeat for different number of clusters
for n_clusters in range(2, 6):
    som = MiniSom(x = 10, y = 10, input_len = 5, sigma = 1.0, learning_rate = 0.5)
    som.random_weights_init(X)
    som.train_random(data = X, num_iteration = 100)
    labels = np.zeros(len(X))
    for i, x in enumerate(X):
        w = som.winner(x)
        labels[i] = w[0] * 10 + w[1]
    centroids = som.get_weights()
    silhouette_avg = silhouette_score(X, labels, metric='euclidean')
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    """

    print(xml)

def Fuzzy():
    xml="""
A = dict()
B = dict()
Y = dict()

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}

print('The First Fuzzy Set is :', A)
print('The Second Fuzzy Set is :', B)


for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]

    if A_value > B_value:
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value

print('Fuzzy Set Union is :', Y)

for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]

    if A_value < B_value:
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value
print('Fuzzy Set Intersection is :', Y)

print('The Fuzzy Set is :', A)


for A_key in A:
   Y[A_key]= 1-A[A_key]

print('Fuzzy Set Complement is :', Y)

    """
    print(xml)
def d_fuzzy():
    xml="""
#Define a Fuzzy Set and Display it
fuzzy_set = {5: 0.4, 10: 0.8, 13: 0.2, 11: 0.5}
print("Fuzzy Set: {", end = "")
for x,y in fuzzy_set.items():
    print(x, ":", y, end = " ")

print("}", end = "\n\n")
# Center of Sums Method (COS)
def center_of_sums_defuzzification(fuzzy_set):
    numerator = sum(x * fuzzy_set[x] for x in fuzzy_set)
    denominator = sum(fuzzy_set[x] for x in fuzzy_set)
    return numerator / denominator
crisp_value = center_of_sums_defuzzification(fuzzy_set)
print("Crisp Value (Center of Sums):", round(crisp_value, 2))
# Center of gravity (COG) / Centroid of Area (COA) Method
def center_of_gravity_defuzzification(fuzzy_set, step=1):
    numerator = sum(x * fuzzy_set[x] * step for x in fuzzy_set)
    denominator = sum(fuzzy_set[x] * step for x in fuzzy_set)
    return numerator / denominator
crisp_value = center_of_gravity_defuzzification(fuzzy_set, step=1)
print("Crisp Value (Center of Gravity):", round(crisp_value, 2))
# Center of Area / Bisector of Area Method (BOA)
def center_of_area_defuzzification(fuzzy_set, step=1):
    total_area = sum(fuzzy_set[x] * step for x in fuzzy_set)
    center_of_area = sum(x * fuzzy_set[x] * step for x in fuzzy_set) /total_area
    return center_of_area
crisp_value = center_of_area_defuzzification(fuzzy_set, step=1)
print("Crisp Value (Center of Area):", round(crisp_value, 2))
# Weighted Average Method
def weighted_average_defuzzification(fuzzy_set):
    numerator = sum(x * fuzzy_set[x] for x in fuzzy_set)
    denominator = sum(fuzzy_set[x] for x in fuzzy_set)
    return numerator / denominator
crisp_value = weighted_average_defuzzification(fuzzy_set)
print("Crisp Value (Weighted Average):", round(crisp_value, 2))
# First of Maxima Method (FOM)
def first_of_maxima_defuzzification(fuzzy_set):
    max_value = max(fuzzy_set.values())
    for x in fuzzy_set:
        if fuzzy_set[x] == max_value:
            return x
crisp_value = first_of_maxima_defuzzification(fuzzy_set)
print("Crisp Value (First of Maxima):", round(crisp_value, 2))
# Last of Maxima Method (FOM)
def last_of_maxima_defuzzification(fuzzy_set):
    max_value = max(fuzzy_set.values())
    for x in reversed(sorted(fuzzy_set.keys())):
        if fuzzy_set[x] == max_value:
            return x
crisp_value = last_of_maxima_defuzzification(fuzzy_set)
print("Crisp Value (Last of Maxima):", round(crisp_value, 2))
# Mean of Maxima Method (FOM)
def mean_of_maxima_defuzzification(fuzzy_set):
    max_values = [x for x, membership in fuzzy_set.items() if
membership == max(fuzzy_set.values())]
    return sum(max_values) / len(max_values)
crisp_value = mean_of_maxima_defuzzification(fuzzy_set)
print("Crisp Value (Mean of Maxima):", round(crisp_value, 2))
    """
    

    print(xml)
def mam():
    xml="""
    pip install -U scikit-fuzzy
    import numpy as np
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    # Step 2: Fuzzify the input variables
    temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
    heater_control = ctrl.Consequent(np.arange(0, 101, 1),
    'heater_control')
    # Define membership functions
    temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
    humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])
    heater_control['low'] = fuzz.trimf(heater_control.universe, [0, 0, 50])
    # Step 3: Define rules
    rule1 = ctrl.Rule(temperature['cold'] & humidity['high'],
    heater_control['low'])
    # Step 4: Create control system
    heater_ctrl = ctrl.ControlSystem([rule1])
    heater = ctrl.ControlSystemSimulation(heater_ctrl)
    # Step 5: Input values and perform inference
    heater.input['temperature'] = 30
    heater.input['humidity'] = 80
    heater.compute()
    # Step 6: Defuzzify and get the crisp output
    heater_output = heater.output['heater_control']
    print("Heater Control:", heater_output)
        """
    print()

def sugo():

    xml="""
pip install -U scikit-fuzzy
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Load dataset
data_url = 'dataset.csv' # Replace with your dataset link
data = pd.read_csv(data_url)
# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 61, 1), 'humidity')
output = ctrl.Consequent(np.arange(0, 26, 1), 'output',
defuzzify_method='centroid')
# Generate fuzzy membership functions
temperature.automf(3)
humidity.automf(3)
output['low'] = fuzz.trimf(output.universe, [0, 5, 10])
output['medium'] = fuzz.trimf(output.universe, [10, 15, 20])
output['high'] = fuzz.trimf(output.universe, [15, 20, 25])
# Define rules using Sugeno-type fuzzy inference
rule1 = ctrl.Rule(temperature['poor'] & humidity['poor'],
output['low'])
rule2 = ctrl.Rule(temperature['average'] & humidity['average'],
output['medium'])
rule3 = ctrl.Rule(temperature['good'] & humidity['good'],
output['high'])
# Create control system
output_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
output_simulation = ctrl.ControlSystemSimulation(output_ctrl)
# Simulation
test_temp = 28
test_humidity = 37
output_simulation.input['temperature'] = test_temp
output_simulation.input['humidity'] = test_humidity
output_simulation.compute()
print(f"For Temperature: {test_temp} and Humidity:{test_humidity}, the Output is:{output_simulation.output['output']}")
# Plot membership functions and results
temperature.view()
humidity.view()
output.view(sim=output_simulation)
plt.show()
        """
        

    print(xml)

def genetic():

    xml="""
import numpy as np

# Define the target function (fitness function)
def fitness_function(x):
    return np.sum(x)

# Define the chromosome representation
def initialize_population(population_size, chromosome_length):
    return np.random.randint(2, size=(population_size, chromosome_length))

# Define the selection operator (tournament selection)
def tournament_selection(population, fitness_values, tournament_size):
    selected_indices = np.random.choice(len(population), tournament_size, replace=False)
    tournament_fitness = fitness_values[selected_indices]
    return population[selected_indices[np.argmax(tournament_fitness)]]

# Define the crossover operator (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

# Define the mutation operator (bit flip mutation)
def mutate(child, mutation_rate):
    mutated_indices = np.where(np.random.rand(len(child)) < mutation_rate)
    child[mutated_indices] = 1 - child[mutated_indices]
    return child

# Define the genetic algorithm
def genetic_algorithm(population_size, chromosome_length, generations, tournament_size, crossover_rate, mutation_rate):
    population = initialize_population(population_size, chromosome_length)
    for generation in range(generations):
        fitness_values = np.array([fitness_function(ind) for ind in population])

        new_population = []
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, fitness_values, tournament_size)
            parent2 = tournament_selection(population, fitness_values, tournament_size)

            if np.random.rand() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy()

            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            new_population.append(child1)
            new_population.append(child2)

        population = np.array(new_population)

        best_individual = population[np.argmax(fitness_values)]
        best_fitness = fitness_function(best_individual)

        print(f"Generation {generation+1}/{generations} - Best Fitness: {best_fitness}")

    return best_individual

# Example usage
np.random.seed(42)
population_size = 50
chromosome_length = 10
generations = 100
tournament_size = 5
crossover_rate = 0.8
mutation_rate = 0.01

best_solution = genetic_algorithm(population_size, chromosome_length, generations, tournament_size, crossover_rate, mutation_rate)
print("Best Solution:", best_solution)
print("Best Fitness:", fitness_function(best_solution))

    """

    print(xml)

def pso():
    xml="""
import numpy as np

class Particle:
    def __init__(self, dim):
        self.position = np.random.rand(dim)
        self.velocity = np.random.rand(dim)
        self.best_position = self.position.copy()
        self.fitness = float('inf')

def objective_function(x):
    # Example: Sphere function
    return np.sum(x**2)

def update_velocity(particle, global_best_position, inertia_weight, cognitive_weight, social_weight):
    inertia_term = inertia_weight * particle.velocity
    cognitive_term = cognitive_weight * np.random.rand() * (particle.best_position - particle.position)
    social_term = social_weight * np.random.rand() * (global_best_position - particle.position)
    return inertia_term + cognitive_term + social_term

def particle_swarm_optimization(population_size, dim, iterations, inertia_weight, cognitive_weight, social_weight):
    particles = [Particle(dim) for _ in range(population_size)]
    global_best_position = None
    global_best_fitness = float('inf')

    for _ in range(iterations):
        for particle in particles:
            particle.fitness = objective_function(particle.position)

            if particle.fitness < objective_function(particle.best_position):
                particle.best_position = particle.position.copy()

            if particle.fitness < global_best_fitness:
                global_best_fitness = particle.fitness
                global_best_position = particle.position.copy()

        for particle in particles:
            particle.velocity = update_velocity(particle, global_best_position, inertia_weight, cognitive_weight, social_weight)
            particle.position += particle.velocity

    return global_best_position, global_best_fitness

# Example usage
np.random.seed(42)
population_size = 20
dim = 5
iterations = 100
inertia_weight = 0.5
cognitive_weight = 1.5
social_weight = 1.5

best_position, best_fitness = particle_swarm_optimization(population_size, dim, iterations, inertia_weight, cognitive_weight, social_weight)
print("Best Position:", best_position)
print("Best Fitness:", best_fitness)

        """
        

    print(xml)
def regression():
    xml="""
import pandas as pd

df = pd.read_csv("Salary_Data.csv")
df
-------------------------------------
from scipy import stats
df1 = df.copy(deep=True)
df1.drop(df1[stats.zscore(df1["Salary"]) > 3].index,axis=0,inplace=True)
print("before drop : ",df.shape)

print("after drop : ",df1.shape)
-----------------------------------------
X = df1.iloc[:,0]
Y = df1.iloc[:,1]
import numpy as np

x_mean = np.mean(X)
y_mean = np.mean(Y)

b1 = sum((X-x_mean) * (Y-y_mean)) / sum((X-x_mean)**2)
b0 = y_mean - b1 * x_mean

print("b0 :",b0)
print("b1 :",b1)
--------------------------------------------
y_pred = b0 + (b1 * X)
y_pred
------------------------------
SSE = sum((Y - y_pred)**2)
SSE
-------------------------------------------
RMSE = np.sqrt(sum((Y - y_pred)**2)/len(X))
RMSE
-----------------------------
SSR = sum((Y - y_pred)**2)
SST = sum((Y - y_mean)**2)
r_square = 1 - (SSR/SST)
r_square
----------------------------------------
import matplotlib.pyplot as plt
plt.scatter(X,Y, color = "red")
plt.plot(X, y_pred, color = "g")
plt.show()
-------------------------------------------
inputs = [int(i) for i in input("Enter the input values to predict output : ").split()]
print("Input\tOutput")
for i in inputs:
    output = b0 + (b1 * i)
    print(i,"\t",output)
------------------------------------
import pandas as pd

df2 = pd.read_csv("house_price1.csv")
df2
--------------------------------
from scipy import stats
df3 = df2.copy(deep=True)
df3.drop(df1[stats.zscore(df3["price"]) > 3].index,axis=0,inplace=True)
print("before drop : ",df2.shape)
print("after drop : ",df3.shape)
----------------------------------------
X1 = df3.iloc[:,0]
X2 = df3.iloc[:,1]
Y = df3.iloc[:,2]
---------------------------------------
import numpy as np


x1_mean = np.mean(X1)
x2_mean = np.mean(X2)
y_mean = np.mean(Y)
n = X1.count()
Ex1_2 = sum(X1**2) - (sum(X1)**2/n)
Ex2_2 = sum(X2**2) - (sum(X2)**2/n)
Ex1y = sum(X1*Y) - (sum(X1)*sum(Y)/n)
Ex2y = sum(X2*Y) - (sum(X2)*sum(Y)/n)
Ex1x2 = sum(X1*X2) - (sum(X1)*sum(X2)/n)


b1 = ((Ex2_2 * Ex1y) - (Ex1x2 * Ex2y))/((Ex1_2 * Ex2_2) - (Ex1x2**2))
b2 = ((Ex1_2 * Ex2y) - (Ex1x2 * Ex1y))/((Ex1_2 * Ex2_2) - (Ex1x2**2))
b0 = y_mean - (b1*x1_mean) - (b2*x2_mean)

print(b0)
print(b1)
print(b2)
-------------------------------------
y_pred = b0 + (b1 * X1) + (b2 * X2)
y_pred
SSE = sum((Y - y_pred)**2)
SSE

RMSE = np.sqrt(sum((Y - y_pred)**2)/len(X))
RMSE

SSR = sum((Y - y_pred)**2)

SST = sum((Y - y_mean)**2)

r_square = 1 - (SSR/SST)
r_square

import matplotlib.pyplot as plt
plt.scatter(X1,Y, color = "red")
plt.scatter(X2,Y, color = "blue")
plt.plot(X1, y_pred, color = "g")
plt.plot(X2, y_pred, color = "g")
plt.show()

input1 = [int(i) for i in input("Enter the input values 1 to predict output : ").split()]
input2 = [int(i) for i in input("Enter the input values 2 to predict output : ").split()]
print("Input\tOutput")
for i in range(len(input1)):
        output = b0 + (b1 * input1[i]) + (b2 * input2[i])
        print(i,"\t",output)
        """
        

    print(xml)