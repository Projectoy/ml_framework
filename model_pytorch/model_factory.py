from enum import Enum, auto

class ModelFactory:

    def create_model(self, model_type_str, configuration):
        model_type = self.get_model_cls_from_str(model_type_str)
        if model_type == EnumModel.BERT:
            return self.create_bert_model(configuration)
        elif model_type == EnumModel.ROBERTA:
            return self.create_roberta_model(configuration)
        elif model_type == EnumModel.TRANSFORMER:
            return self.create_transformer_model(configuration)
        elif model_type == EnumModel.ENC_DEC:
            return self.create_enc_dec_model(configuration)
        else:
            raise Exception("no model type!{}".format(model_type_str))

    def create_bert_model(self, configuration):
        pass

    def create_roberta_model(self, configuration):
        pass

    def create_transformer_model(self, configuration):
        pass

    def create_enc_dec_model(self,configuration):
        pass

    def get_model_cls_from_str(self, model_type_str):
        if model_type_str == "bert":
            return EnumModel.BERT
        elif model_type_str == "roberta":
            return EnumModel.ROBERTA
        elif model_type_str == "transformer":
            return EnumModel.TRANSFORMER
        elif model_type_str == "enc_dec":
            return EnumModel.ENC_DEC
        else:
            return None

class EnumModel(Enum):
    BERT = auto()
    ROBERTA = auto()
    TRANSFORMER = auto()
    ENC_DEC = auto()