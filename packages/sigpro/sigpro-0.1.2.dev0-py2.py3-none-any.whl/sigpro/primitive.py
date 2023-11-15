from . import contributing
#from .contributing import *
import json
import inspect

def make_primitive(primitive, primitive_type, primitive_subtype, 
                    primitive_function = None, #primitive_args,
                    context_arguments=None, fixed_hyperparameters=None,
                    tunable_hyperparameters=None, primitive_inputs = None, primitive_outputs=None):
        """Create a primitive JSON.

        During the JSON creation the primitive function signature is validated to
        ensure that it matches the primitive type and subtype implicitly specified
        by the primitive name.

        Any additional function arguments are also validated to ensure that the
        function does actually expect them.

        Args:
            primitive (str):
                The name of the primitive, the python path including the name of the
                module and the name of the function.
            primitive_type (str):
                Type of primitive.
            primitive_subtype (str):
                Subtype of the primitive.
            primitive_function (function):
                Function applied by the primitive.
            context_arguments (list or None):
                A list with dictionaries containing the name and type of the context arguments.
            fixed_hyperparameters (dict or None):
                A dictionary containing as key the name of the hyperparameter and as
                value a dictionary containing the type and the default value that it
                should take.
            tunable_hyperparameters (dict or None):
                A dictionary containing as key the name of the hyperparameter and as
                value a dictionary containing the type and the default value and the
                range of values that it can take.
            primitive_inputs (list or None):
                A list with dictionaries containing the name and type of the input values. If
                ``None`` default values for those will be used.
            primitive_outputs (list or None):
                A list with dictionaries containing the name and type of the output values. If
                ``None`` default values for those will be used.

        Raises:
            ValueError:
                If the primitive specification arguments are not valid.

        Returns:
            str:
                Path of the generated JSON file.
    """
    context_arguments = context_arguments or []
    fixed_hyperparameters = fixed_hyperparameters or {}
    tunable_hyperparameters = tunable_hyperparameters or {}

    primitive_spec = contributing._get_primitive_spec(primitive_type, primitive_subtype)
    primitive_inputs = primitive_inputs  or primitive_spec['args']
    primitive_outputs = primitive_outputs or primitive_spec['output']

    if primitive_function == None:
        primitive_function = contributing._import_object(primitive)

    primitive_args = contributing._get_primitive_args(
        primitive_function,
        primitive_inputs,
        context_arguments,
        fixed_hyperparameters,
        tunable_hyperparameters
    )

    primitive_dict = {
        'name': primitive,
        'primitive': primitive,
        'classifiers': {
            'type': primitive_type,
            'subtype': primitive_subtype
        },
        'produce': {
            'args': primitive_args,
            'output': [
                {
                    'name': primitive_output['name'],
                    'type': primitive_output['type'],
                }
                for primitive_output in primitive_outputs
            ],
        },
        'hyperparameters': {
            'fixed': fixed_hyperparameters,
            'tunable': tunable_hyperparameters
        }
    }
    return primitive_dict



class Primitive: 
		"""
		This class will support (via inheritance) the creation of custom user-defined primitive classes.
		It will automatically construct JSONs for several primitive types and allow for
    easier use in linear/tree/layer pipeline architectures.
		"""
    
        #init should probably only take in the primitive and primitive type/subtype, both of which can be called within the individual classes, so they wont ever be 
        #explicitly passed by the user. 
        
        #The user should explicitly supply the function (?), and have the option to 

        #hyperparameter specs can probably be fetched w. inspect.signature.

        #rermove the 'make_json' cond arg and just allow the user to call the func separately.

        #make_json should provide a bare-minimum w/ only primitive, primitive_type, subtype, primitive_outputs?? 





        #when calling an existing primitive, the user should just be able to use the XNAMEPrimitive class with the desired parameters. (init_params). 
        #for these, the json already exists
        #the pipeline itself could try and handle any further modification of those primitives as part of a pipeline (massaging inputs/outputs, etc).

        #SigPro should also assist the user in being able to create a custom primitive of a certain type and subtype. 
        #The user wants to be able to put in a primitive name, type, subtype and function and spit out eithe    r a json or 
        # a class w/ the same basic api as all of the preloaded prims.

        
        
        # We could then add context, fixed, and tunable hyperparameters. 
		# def __init__(self, primitive, primitive_type, primitive_subtype, 
        #             primitive_function = None,
        #             context_arguments=None, fixed_hyperparameters=None,
        #             tunable_hyperparameters=None, primitive_outputs=None,
        #             primitives_path='sigpro/primitives', primitives_subfolders=True, 
        #             init_params = {}, make_json = True):

		# 		"""
		# 		Initialize primitive object. 
		# 		User can specify whether to write a JSON file as well 
		# 		for the primitive class, using write_to_json, by passing in an argument.
		# 		"""
        #         self.primitive = primitive
        #         self.primitive_type = primitive_type
        #         self.primitive_subtype = primitive_subtype
        #         self.primitive_function = primitive_function
        #         self.context_arguments = context_arguments or []
        #         self.fixed_hyperparameters = fixed_hyperparameters or {}
        #         self.tunable_hyperparamers = tunable_hyperparameters or {}
        #         self.primitive_outputs = primitive_outputs or contributing._get_primitive_spec(primitive_type, primitive_subtype)['output']
        #         self.primitives_path = primitives_path
        #         self.primitives_subfolders = primitives_subfolders


		# 		self.primitive_json = make_primitive(primitive, primitive_type, primitive_subtype, primitive_function,
        #             context_arguments, fixed_hyperparameters,
        #             tunable_hyperparameters, primitive_outputs,
        #             primitives_path, primitives_subfolders) #old make-primitive process
		# 		if make_json:
		# 			write_to_json(self.primitive_json, primitives_path)
		# 		pass
		# 		self.hyperparameter_values = init_params #record the init_param values as well.

    def __init__(self, primitive, primitive_type, primitive_subtype, 
                primitive_function, init_params = {}):

            """
            Initialize primitive object. 
            User can specify whether to write a JSON file as well 
            for the primitive class, using write_to_json, by passing in an argument.
            """
            self.primitive = primitive
            self.primitive_type = primitive_type
            self.primitive_subtype = primitive_subtype
            self.tunable_hyperparameters = {}
            self.fixed_hyperparameters = {}
            self.context_arguments = []
            primitive_spec = contributing._get_primitive_spec(primitive_type, primitive_subtype)
            self.primitive_inputs = primitive_spec['args']
            self.primitive_outputs = primitive_spec['output']

            contributing._check_primitive_type_and_subtype(primitive_type, primitive_subtype)


            self.primitive_function = primitive_function

            # self.primitive_args = _get_primitive_args(
            #     self.primitive_function,
            #     self.primitive_inputs,
            #     self.context_arguments,
            #     self.fixed_hyperparameters,
            #     self.tunable_hyperparameters
            # )



            #self.primitive_args = contributing._get_primitive_args(self.primitive_function, self.primitive_inputs, self.context_arguments, self.fixed_hyperparameters, self.tunable_hyperparameters)

            #function_args = inspect.getfullargspec(primitive_function).args.copy() #do smth with function args

            self.hyperparameter_values = init_params #record the init_param values as well.

            for param in init_params: #validate that param is a hyperparameter
                if param not in self.tunable_hyperparameters and param not in self.fixed_hyperparameters:
                    if param in COMMON_PARAMS:
                        self.fixed_hyperparameters[param] = 
                pass

            #self._validate_primitive_spec() #validate the primitive creation.

            #self.primitive_json = None
            #self._update_primitive_json()


    def make_primitive_json(self): #return primitive json.
        self._validate_primitive_spec()
        return make_primitive(self.primitive, self.primitive_type, self.primitive_subtype, self.primitive_function , self.context_arguments, self.fixed_hyperparameters, self.tunable_hyperparameters, self.primitive_outputs)
        pass


    def write_primitive_json(self, primitives_path = 'sigpro/primitives', primitives_subfolders=True):

        """
        primitives_path (str):
            Path to the root of the primitives folder, in which the primitives JSON will be stored.
            Defaults to `sigpro/primitives`.
        primitives_subfolders (bool):
            Whether to store the primitive JSON in a subfolder tree (``True``) or to use a flat
            primitive name (``False``). Defaults to ``True``.
        """
        pj = self.make_primitive_json()
        contributing._write_primitive(pj, self.primitive, primitives_path, primitives_subfolders)


        pass

    def set_context_arguments(self, context_arguments):
        self.context_arguments = context_arguments
        pass
    def set_tunable_hyperparameters(self, tunable_hyperparameters):
        self.tunable_hyperparameters = tunable_hyperparameters
        pass
    def set_fixed_hyperparameters(self, fixed_hyperparameters):
        self.fixed_hyperparameters = fixed_hyperparameters
        pass 

    def add_context_arguments(self, context_arguments):
        for arg in context_argments:
            if arg not in self.context_arguments:
                context_arguments.append(arg)
    def add_fixed_hyperparameter(self, hyperparams):
        for hyperparam in hyperparams:
            self.fixed_hyperparameters[hyperparam] = hyperparams[hyperparam]
    def add_tunable_hyperparameter(self, hyperparams):
        for hyperparam in hyperparams:
            self.tunable_hyperparameters[hyperparam] = hyperparams[hyperparam]
    
    def remove_context_arguments(self, context_arguments):
        for arg in context_argments:
            if arg in self.context_arguments:
                context_arguments.remove(arg)
    def remove_fixed_hyperparameter(self, hyperparams):
        for hyperparam in hyperparams:
            del self.fixed_hyperparameters[hyperparam]
    def remove_tunable_hyperparameter(self, hyperparams):
        for hyperparam in hyperparams:
            del self.tunable_hyperparameters[hyperparam]


    def set_primitive_inputs(self, primitive_inputs): #does the user really need to specify this?
        self.primitive_inputs = primitive_inputs
        pass             
    def set_primitive_outputs(self, primitive_outputs): #does the user really need to specify this?
        self.primitive_outputs = primitive_outputs
        pass 


    #these methods would specifically alter the primitive function/json to accept keywords.
    def rename_inputs(self, input_names): #potentially needed for layer pipelines?
            pass
    def rename_outputs(self, input_names): #potentially needed for layer pipelines?
            pass



    def _validate_primitive_spec(self): #check if the primitive is actually up-to-spec for debugging use/use in pipelines; throws appropriate errors.
        
        self.primitive_args = _get_primitive_args(
            self.primitive_function,
            self.primitive_inputs,
            self.context_arguments,
            self.fixed_hyperparameters,
            self.tunable_hyperparameters
        )
        pass
    
    
    def get_hyperparam_dict(self, name = None):
            """
            Return the dictionary of parameters (for use in larger pipelines such as Linear, etc)
            """
            if name == None:
                name = self.primitive
            return { 'name': name, 'primitive': self.primitive, 'init_params': self.hyperparameter_values}




class TransformationPrimitive(TransformationPrimitive):

    def __init__(self, primitive, primitive_subtype,  primitive_function, init_params = {}):
        super().__init__(primitive, 'transformation',primitive_subtype, primitive_function, init_params)

    pass

class AmplitudeTransformation(TransformationPrimitive):

    def __init__(self, primitive, primitive_function, init_params = {}):
        super().__init__(primitive, 'amplitude', primitive_function, init_params)

    pass


class FrequencyTransformation(TransformationPrimitive):

    def __init__(self, primitive, primitive_function, init_params = {}):
        super().__init__(primitive,  'frequency', primitive_function, init_params)

    pass

class FrequencyTimeTransformation(TransformationPrimitive):

    def __init__(self, primitive,  primitive_function, init_params = {}):
        super().__init__(primitive, 'frequency_time', primitive_function, init_params)

    pass

class FrequencyBand(FrequencyTransformation):

    def __init__(self, low, high):
        super().__init__("sigpro.transformations.frequency.band.frequency_band", sigpro.transformations.frequency.band.frequency_band, {'low': low, 'high': high})
        primitive_spec = contributing._get_primitive_spec('aggregation', 'frequency')
        self.set_primitive_inputs(primitive_spec['args'])
        self.set_primitive_outputs([{'name': 'amplitude_values', 'type': "numpy.ndarray" }, {'name': 'frequency_values', 'type': "numpy.ndarray" }])
        self.set_fixed_hyperparameters({'low': {'type': 'int'}, 'high': {'type': 'int'}})

class ComparativeTransformation(TransformationPrimitive):
    pass


class AggregationPrimitive(Primitive):
    def __init__(self, primitive, primitive_subtype,  primitive_function, init_params = {}):
        super().__init__(primitive, 'aggregation',primitive_subtype, primitive_function, init_params)

    pass


class AmplitudeAggregation(AggregationPrimitive):

    def __init__(self, primitive, primitive_function, init_params = {}):
        super().__init__(primitive, 'amplitude', primitive_function, init_params)

    pass


class FrequencyAggregation(AggregationPrimitive):

    def __init__(self, primitive, primitive_function, init_params = {}):
        super().__init__(primitive,  'frequency', primitive_function, init_params)

    pass

class FrequencyTimeAggregation(AggregationPrimitive):

    def __init__(self, primitive,  primitive_function, init_params = {}):
        super().__init__(primitive, 'frequency_time', primitive_function, init_params)

    pass


class ComparativeAggregation(TransformationPrimitive):
    pass

def primitive_from_json(json_path, init_params): #Create the proper primitive object given an input json and hyperparameters.

    pass




class LinearPipeline(Primitive): #We inherit primitive optimistically in hopes of nested pipelines.

		"""
		Analogue of sigpro.SigPro object in current use, takes in same arguments.
		Only distinction is that we accept primitive objects, rather than dict inputs.
		"""


        @staticmethod
        def _build_linear_pipeline(transformations, aggregations, values_column_name='values',
                 keep_columns=False, input_is_dataframe=True):  #Placeholder. Should contain bulk of work.

            return LinearPipeline(transformations, aggregations, values_column_name,
                 keep_columns, input_is_dataframe)   

		def __init__(self, transformations, aggregations, values_column_name='values',
                 keep_columns=False, input_is_dataframe=True): #Note. User does not need to set input values
                
                self.transformations = transformations
                self.aggregations = aggregations
                # self.values_column_name = 'values'
                # self.keep_columns = False
                # self.input_is_dataframe = 
                self.values_column_name = values_column_name
                self.keep_columns = keep_columns
                self.input_is_dataframe = input_is_dataframe

				for transformation_ in transformations:
                    transformation_._validate_primitive_spec()
                    transformation = transformation_.get_hyperparam_dict()

                    #continue OG method
                    pass
                
                for aggregation_ in aggregations:
                    aggregation_._validate_primitive_spec()
                    aggregation = aggregation_.get_hyperparam_dict()

                    #continue OG method

                    pass


        def set_values_column_name(values_column_name):
            self.values_column_name = values_column_name

        def set_keep_columns(self, keep_columns):
            self.keep_columns = keep_columns

        def accept_dataframe_input(self, input_is_dataframe):
            self.input_is_dataframe = input_is_dataframe



		def process_signal(self, data, ...):
				pass

		#getters and setters 


"""
Layer pipelines: interleave primitives with 'column renamer primitives' that take existing ft columns,
and set/add duplicates w/ the appropriate column names. 
"""