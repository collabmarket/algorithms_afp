import io
import argparse
from datetime import datetime
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Permite modificar solo nb_base y replicar cambios en nbs
nb_base = 'A-E_Cuprum.ipynb'
nbs = ['A-E_Habitat.ipynb', 'A-E_Modelo.ipynb', 'A-E_Cuprum.ipynb']
# Falta agregar: Capital, Planvital, Provida

# Funcion procesa nb
def nbexec(nb_base, nb):
    base_name = nb_base.split('_')[1].split('.')[0].upper()
    afp_name = nb.split('_')[1].split('.')[0].upper()
    # Lee nb_base origen
    with io.open(nb_base, 'rt') as f:
        aux = nbformat.read(f, as_version=4)
    # Reemplaza afp_name
    u = aux['cells'][2]['source'].replace(base_name, afp_name)
    aux['cells'][2]['source'] = u
    # Opciones
    ep = ExecutePreprocessor(timeout=600)
    # Procesa aux (Revisar si preprocess modifica aux)
    ep.preprocess(aux, {})
    # Escribe nb destino
    with io.open(nb, 'wt') as f:
        nbformat.write(aux, f)
    print "[INFO]--" + datetime.now().strftime('%Y-%M-%d %H:%M:%S') + "--" + "nbexec" + "--" + nb

def processall():
    # Procesa nb base
    nbexec(nb_base,  nb_base)
    # Procesa lista nbs
    for nb in nbs:
        nbexec(nb_base, nb)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy changes from A-E_Cuprum.ipynb")
    parser.add_argument('nb', nargs='?')
    args = parser.parse_args()
    if args.nb:
        nbexec(nb_base, args.nb)
    else:
        processall()
