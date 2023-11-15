import os
import warnings
from datetime import datetime

from .. import sge 

from .utilities.lib import *
from .utilities.logger import Logger


class Fedora(sge.EngineSGE):

    def __init__(
            self,
            seed,
            model,
            error_metric,
            sge_parameters_path,
            grammar_path,
            logging_dir,
            penalty = None,
            warn = True,
            operators = {}
        ):  
        
        # SGE parameters path
        self.sge_parameters_path = sge_parameters_path
        super().__init__(self.sge_parameters_path)

        # Set the seed
        self.seed = seed

        # Set model
        self.model = model

        # Error Metric
        self.error_metric = error_metric

        # Define Grammar Path
        self.grammar_path = grammar_path

        # Define Logging Directory
        self.logging_dir = logging_dir

        # Define fitness penalty function
        self.penalty = penalty

        # Log warnings
        self.warn = warn

        def warning_handler(message, category, filename, lineno, file=None, line=None):
            if self.warn:
                self.warnings += 1
                with open(self.current_run + Logger.WARNING_FILE, 'a') as file:
                    time = datetime.now().strftime("%H:%M:%S")
                    file.write(f"[{self.warnings}] - {time}: " + warnings.formatwarning(message, category, filename, lineno))

        warnings.showwarning = warning_handler 

        for name, op in operators.items():
            globals()[name] = op


    # def evaluate(self, phenotype: str) -> tuple[float, dict]:
    def evaluate(self, phenotype):
        """ Structured Grammatical Evolution (SGE) Evaluate Function """

        # Applying the Individual Phenotype to the dataset
        engineered_train = engineer_dataset(phenotype, self.train_data, globals=globals())
        engineered_validation = engineer_dataset(phenotype, self.validation_data, globals=globals())
        
        # Fitness
        fitness = score(self.model, engineered_train, engineered_validation, self.error_metric)

        if self.penalty:
            fitness += self.penalty(self.model)

        # Info
        self.individuals_information.append({PHENOTYPE: phenotype, FITNESS: fitness})

        return fitness, None

    def evolution_progress(self, population):
        # phenotypes = [individual["phenotype"] for individual in population]
        return ""

    def save_best(self, current_run):
        best_validation_info = sorted(self.individuals_information, key=lambda x: x[FITNESS])[0]
        individual = {
            FEATURES: len(get_features(best_validation_info[PHENOTYPE])),
            PHENOTYPE: best_validation_info[PHENOTYPE]
        }
        Logger.save_json(individual, current_run + Logger.BEST_FILE)
        

    def fit(self, X, y):
        self.warnings = 0
        super().__init__(self.sge_parameters_path)
        
        # Split Data
        self.train_data, self.validation_data = split_data(X, y, self.seed)
        
        # Set experience path
        self.experience_dir = self.logging_dir + sge.params["EXPERIMENT_NAME"]

        # Setup SGE PARAMS                                 
        sge.params["RUN"] = sge.params["SEED"] = self.seed
        sge.params["GRAMMAR"] = self.grammar_path
        sge.params["EXPERIMENT_NAME"] = self.experience_dir + Logger.RUNS

        self.current_run = sge.params["EXPERIMENT_NAME"] + Logger.run(self.seed)

        if os.path.exists(self.current_run): 
            Logger.error_experiment_exists(Logger.run(self.seed))
            return self

        # Create Current Run Folder if not exists
        if not os.path.exists(self.current_run): 
            os.makedirs(self.current_run)
        
        # Set Model Seed
        self.model.random_state = self.seed
                
        # Run Structured Grammatical Evolution
        self.individuals_information = []
        self.evolutionary_algorithm()
        
        # Save the phenotype of the best validation individual
        self.save_best(self.current_run)

        # Log warnings
        Logger.warnings(self.warnings, self.warn)
            
        return self
    
    def transform(self, X):
        best = self.get_best(self.experience_dir, self.seed)
        return engineer_dataset(best[PHENOTYPE], format_data(X, None), globals=globals())[DATA]
    
    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.transform(X)
    
    @staticmethod
    def get_best(results_dir, seed):
        return pd.read_json(f"{results_dir}/{Logger.RUNS}{Logger.run(seed)}{Logger.BEST_FILE}", typ="series")