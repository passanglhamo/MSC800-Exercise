from ucimlrepo import fetch_ucirepo

# Load the Iris dataset
iris = fetch_ucirepo(id=53)

# Get features and target
X = iris.data.features
y = iris.data.targets

# 1. Total number of records
total_records = len(X)
print("1. Total number of records:", total_records)

# 2. Total number of different flowers
total_flowers = y.iloc[:, 0].nunique()
print("2. Total number of different flowers:", total_flowers)

# 3. Names of all different flowers
flower_names = y.iloc[:, 0].unique()
print("3. Names of different flowers:")
for flower in flower_names:
    print(flower)