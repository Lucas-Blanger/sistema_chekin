class AlgumaCoisa:
    def __enter__(self):
        print('Estou Entrando')
        
    def __exit__(self, exec_type, exec_val, exec_tb):
        print('Estou saindo')
        
with AlgumaCoisa() as ola:
    print('Estou no meio')