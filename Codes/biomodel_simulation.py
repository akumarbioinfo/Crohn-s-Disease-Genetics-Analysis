import tellurium as te # type: ignore
import matplotlib.pyplot as plt

# Step 1: Load the BioModel
model_id = 'BIOMD0000000536'  # model ID
model_url = f'https://www.ebi.ac.uk/biomodels/model/download/{model_id}?filename={model_id}_url.xml'

# Load the SBML model
r = te.loadSBMLModel(model_url)

# Simulate the model for a given time period
result = r.simulate(0, 100, 1000)  # Simulate from time 0 to 100 with 1000 points

# Get the species IDs from the model
species_ids = r.getFloatingSpeciesIds()

# Print the species IDs to identify them
print("Species IDs:")
with open("figures/biomodel_species_ids.txt", "w") as f: # Save species IDs to a text file
    for i, species_id in enumerate(species_ids):
        print(f"{i}: {species_id}")
        f.write(f"{i}: {species_id}\n")

# Analyze and Plot Results for All Species
# I'll add a modification here to save plots to the 'figures' directory
for i, species_id in enumerate(species_ids):
    # Extract the time and concentration data for the species of interest
    time = result[:, 0]
    # Adjust index for result as first column is time, others are species
    concentration = result[:, i + 1]

    # Plot the concentration of the species over time
    plt.figure(figsize=(10, 6))
    plt.plot(time, concentration, label=species_id)
    plt.xlabel('Time')
    plt.ylabel('Concentration')
    plt.title(f'Simulation of {species_id} over Time')
    plt.legend()
    plt.grid(True) # Added grid for better readability
    plt.savefig(f"figures/biomodel_simulation_{species_id}.png") # Saving to figures folder
    plt.close() # Close plot to prevent too many open figures