from src.model.despesa_model import Despesa

usuario = Despesa().incluir("Transporte", 1)
print(usuario)