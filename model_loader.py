from dataclasses import dataclass
import os,pickle

@dataclass
class ModelLoadingConfig:
    trained_model_path_config = os.path.join('notebooks','xgb.pkl')
    preprocessor_path_config = os.path.join('notebooks','preprocessor.pkl')


class Model:
    def __init__(self) -> None:
        self.model_configure = ModelLoadingConfig()
    
    def preprocessing(self,d):
        preprocessing = pickle.load(open(self.model_configure.preprocessor_path_config,'rb'))

        return preprocessing.transform(d)
    
    def Predict(self,inputs):
        try:
            model = pickle.load(open(self.model_configure.trained_model_path_config,'rb'))
            return model.predict(inputs)
        except Exception as e:
            raise e 
        

# if __name__ == '__main__':
#     model = Model()
#     d = {'hello':1}
#     model.preprocessing(**d)
#     print('loaded')