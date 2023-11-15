try:
    from sage_lib.ForceFieldManager import ForceFieldManager
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing ForceFieldManager: {str(e)}\n")
    del sys

class GAPTrainer(ForceFieldManager):
    """
    Clase para entrenar un modelo GAP (Gaussian Approximation Potential).
    """

    def __init__(self, name="GAP_model", file_location="."):
        """
        Inicializa la clase GAPTrainer con valores predeterminados o proporcionados.
        """
        super().__init__(name, file_location)
        self.parameters = {
            "e0": {"H": 3.21, "O": 4.6},
            "energy_parameter_name": "energy",
            "force_parameter_name": "forces",
            "do_copy_at_file": "F",
            "sparse_separate_file": "T",
            "gp_file": "GAP.xml",
            "at_file": "train.xyz",
            "default_sigma": [0.008, 0.04, 0, 0],
            "gap": {
                "distance_2b": {
                    "cutoff": 4.0,
                    "covariance_type": "ard_se",
                    "delta": 0.5,
                    "theta_uniform": 1.0,
                    "sparse_method": "uniform",
                    "add_species": "T",
                    "n_sparse": 10
                }
            }
        }

    def set_parameters(self, **kwargs):
        """
        Establece o actualiza los parámetros para el entrenamiento del modelo GAP.
        """
        for key, value in kwargs.items():
            if key in self.parameters:
                self.parameters[key] = value
            else:
                raise KeyError(f"Parameter {key} not recognized.")

    def get_parameter_description(self):
        """
        Devuelve una descripción de los parámetros.
        """
        descriptions = {
            "e0": "Energías de los átomos aislados.",
            # Añadir descripciones para el resto de los parámetros aquí
        }
        return "\n".join(f"{key}: {desc}" for key, desc in descriptions.items())

    def train(self):
        """
        Entrena el modelo GAP utilizando los parámetros establecidos.
        """
        command = self._build_command()
        print(f"Executing: {command}")
        # Aquí se ejecutaría el comando en un entorno real
        # os.system(command)

    def _build_command(self):
        """
        Construye el comando de bash para el entrenamiento GAP.
        """
        command = ["gap_fit"]
        for key, value in self.parameters.items():
            if isinstance(value, dict):
                subcommand = self._build_subcommand(key, value)
                command.append(subcommand)
            else:
                command.append(f"{key}={value}")
        return " ".join(command)

    def _build_subcommand(self, key, value_dict):
        """
        Construye un subcomando para parámetros complejos.
        """
        parts = [f"{key}="]
        for subkey, subvalue in value_dict.items():
            if isinstance(subvalue, dict):
                parts.append(self._build_subcommand(subkey, subvalue))
            else:
                parts.append(f"{subkey}={subvalue}")
        return ":".join(parts)



class FF_GAP(ForceFieldManager):
    """
    Represents an individual force field model.
    This class can be extended to support various types of force fields,
    including those based on machine learning.
    """

    def __init__(self, parameters):
        """
        Initialize the force field model with given parameters. if not use default values.
        
        :param parameters: A dictionary or other structure containing the parameters for the model.
        """
        super().__init__(name=name, file_location=file_location)
        # add new parameters 

    def train(self, ....):
        """
        Train the GAP model using the provided atomic configuration file.

        :param at_file: XYZ file with teaching configurations.
        :param gp_file: Output XML file for the GAP model.
        :param teach_kwargs: Additional parameters for the GAP teaching process.
        """
        command = 

        # Execute the command


'''
 gap_fit 

 energy_parameter_name=E_dftbplus_d4 
 force_parameter_name=F_dftbplus_d4 
 do_copy_at_file=F 
 sparse_separate_file=T 
 gp_file=GAP.xml 
 at_file=train.xyz 
 default_sigma={0.008 0.04 0 0} 

 gap_fit 
 energy_parameter_name=energy 
 force_parameter_name=forces 
 do_copy_at_file=F 
 sparse_separate_file=T 
 gp_file=GAP.xml 
 at_file=train.xyz 
 default_sigma={0.008 0.04 0 0} 
 gap={distance_2b cutoff=4.0 covariance_type=ard_se delta=0.5 theta_uniform=1.0 sparse_method=uniform add_species=T n_sparse=10}

gap_fit 
energy_parameter_name=energy 
force_parameter_name=forces 
do_copy_at_file=F 
sparse_separate_file=T 
gp_file=GAP_3b.xml 
at_file=train.xyz 
default_sigma={0.008 0.04 0 0} 
gap={distance_2b cutoff=4.0 covariance_type=ard_se delta=0.5 theta_uniform=1.0 sparse_method=uniform add_species=T n_sparse=10 : 
        angle_3b cutoff=3.5 covariance_type=ard_se delta=0.5 theta_fac=0.5 add_species=T n_sparse=30 sparse_method=uniform}



quip E=T F=T atoms_filename=train.xyz param_filename=GAP.xml | grep AT | sed 's/AT//' > quip_train.xyz

'''