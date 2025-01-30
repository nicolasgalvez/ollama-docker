class BasicModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        # Load the model from the specified path
        # This is a placeholder for actual model loading logic
        self.model = "Loaded model from {}".format(self.model_path)

    def generate_prediction(self, input_data):
        # Generate a prediction based on the input data
        # This is a placeholder for actual prediction logic
        return "Prediction for '{}': {}".format(input_data, self.model) if self.model else "Model not loaded"