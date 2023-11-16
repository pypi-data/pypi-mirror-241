try:
    from sage_lib.FileManager import FileManager
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing FileManager: {str(e)}\n")
    del sys

try:
    import DFTPartition
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing DFTPartition: {str(e)}\n")
    del sys

try:
    import random
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing random: {str(e)}\n")
    del sys

class FFEnsembleManager(FileManager):
    """
    Represents an individual force field model.
    This class can be extended to support various types of force fields,
    including those based on machine learning.
    """

    def __init__(self, parameters):
        """
        Initialize the force field model with given parameters.
        
        :param parameters: A dictionary or other structure containing the parameters for the model.
        """
        self.parameters = parameters
        self.trainning_data = DFTPartition()
        self.test_data = DFTPartition()
        self.data = DFTPartition()

    def add_xyz(self, partition, file_location:str=None):
        file_location = file_location if not file_location is None else file_location
        partition.read_configXYZ(file_location)

    def add_data(self, partition, source='xyz', file_location:str=None):
        if source == 'xyz':
            partition.read_configXYZ(file_location)

    def add_trainning_data(self, source='xyz', file_location:str=None):
        """
        """
        file_location = file_location if not file_location is None else file_location
        self.add_data(partition=self.trainning_data, source='xyz', file_location=file_location)
        return True

    def add_test_data(self, source='xyz', file_location:str=None):
        """
        """
        file_location = file_location if not file_location is None else file_location
        self.add_data(partition=self.test_data, source='xyz', file_location=file_location)
        return True

    def add_data(self, file_location:str=None):
        """
        """
        file_location = file_location if not file_location is None else file_location
        self.add_data(partition=self.data, source='xyz', file_location=file_location)
        return True

    def split_data(self, percentage):
        """
        Splits the data in self.data.containers into self.training_data.containers and 
        self.test_data.containers based on the specified percentage.

        :param percentage: The percentage of data to allocate to the training set.
        """
        # Ensure the provided percentage is within a valid range
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100.")

        # Calculate the number of elements to allocate to the training set
        total_data_length = len(self.data.containers)
        training_set_size = int(total_data_length * (percentage / 100))

        # Shuffle the data to ensure randomness
        shuffled_data = self.data.containers.copy()
        random.shuffle(shuffled_data)

        # Split the data into training and test sets
        new_training_data = shuffled_data[:training_set_size]
        new_test_data = shuffled_data[training_set_size:]

        # Retain existing data in training and test data lists
        self.training_data.containers.extend(new_training_data)
        self.test_data.containers.extend(new_test_data)
        
    def add_model(self, model):
        """
        Add a new force field model to the manager.

        :param model: An instance of ForceFieldModel to be added.
        """
        self.models.append(model)

    def train_all(self, training_data):
        """
        Train all force field models using the provided training data.

        :param training_data: Data to be used for training all models.
        """
        for model in self.models:
            model.train(training_data)

    def predict_all(self, data):
        """
        Apply all force field models to the given data and return the results.

        :param data: The data to apply the models to.
        :return: A list of results from applying each model.
        """
        results = []
        for model in self.models:
            results.append(model.apply(data))
        return results

