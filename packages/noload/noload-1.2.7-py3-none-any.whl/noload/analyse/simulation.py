# SPDX-FileCopyrightText: 2020 G2Elab / MAGE
#
# SPDX-License-Identifier: Apache-2.0

from noload.optimization.iterationHandler import Iterations
from typing import Callable, Dict, List, Any

'''computes model with the inputs dictionnary, and give the value of output 
variables'''


def computeOnce(model: Callable[..., Dict], inputs: Dict[str, Any],
                outputs: List[str]):
    """
    Computes the outputs of the model according to the values of the given
    input variables.
    :param model: model
    :param inputs: names and values of input variables (dictionary)
    :param outputs: names of output variables (list)
    :return: values of the outputs (list)
    """
    res = model(**inputs)
    dico = {k: v for k, v in res.__iter__()}  # conversion en dictionnaire
    out=[]
    for vars in outputs:
        try:
            if vars not in list(dico.keys()):
                raise KeyError(vars) #si la variable du cahier des charges
        except KeyError: # n'appartient pas aux sorties du modèle
            print('Warning :',vars,'is not in model')
            pass
        else:
            out.append(dico[vars])
    # sauvegarde et tracé des résultats uniquement si appel à la fonction et
    # non au gradient
    return out


# TODO : Harmoniser les résultats avec ceux d'une optimisation pour le tracé
#  des itérations
'''computes model with the inputs dictionnary and a variable input varying in 
a range, and give the value of output variables'''


def computeParametric(model: Callable[..., Dict], variable: str,
                      range: List[float], inputs: Dict[str, Any],
                      outputs: List[str]):
    """
    Computes the outputs of the model corresponding to the values of the given
    input variables, except one varying in a range of values.
    :param model: model
    :param variable: the input that varies
    :param range: range of values in which the input varies
    :param inputs: names and values of constant input variables (dictionary)
    :param outputs: names of output variables (list)
    :return: values of the outputs (list)
    """
    iter = Iterations(None,
        [variable], outputs)  # permet de sauvegarder les résultats au fur et
    # à mesure (optionnel)
    for x in range:
        if inputs != []:
            res = model(**{variable: x}, **inputs)
        else:
            res = model(*x)  # in case of model with only 1 argument
        dico = {k: v for k, v in res.__iter__()}  # conversion en dictionnaire
        out=[]
        for vars in outputs:
            try:
                if vars not in list(dico.keys()):
                    raise KeyError(vars) #si la variable du cahier des charges
            except KeyError: # n'appartient pas aux sorties du modèle
                print('Warning :',vars,'is not in model')
                pass
            else:
                out.append(dico[vars])
        # sauvegarde et tracé des résultats uniquement si appel à la fonction
        # et non au gradient
        iter.updateData([x], out)
    return iter

import autograd.numpy as np
from autograd import jacobian
from noload.optimization.Tools import StructList

def computeJacobian(model: Callable[..., Dict], inputs: Dict[str, Any],
                      outputs: List[str]):
    """
    Displays gradients of outputs corresponding to the values of
    the given inputs.
    :param model: model
    :param inputs: names and values of constant input variables (dictionary)
    :param outputs: names of output variables (list)
    :return: gradients of the outputs (list)
    """
    inputs_keys=list(inputs.keys())
    inputs_values=np.array(list(inputs.values()))
    def eval_model(inputs_values):
        global shape
        xList=dict(zip(inputs_keys,inputs_values))
        res = model(**xList)
        dico = {k: v for k, v in res.__iter__()}  # conversion en dictionnaire
        out=[]
        for vars in outputs:
            try:
                if vars not in list(dico.keys()):
                    raise KeyError(vars) #si la variable du cahier des charges
            except KeyError: # n'appartient pas aux sorties du modèle
                print('Warning :',vars,'is not in model')
                pass
            else:
                out.append(dico[vars])
        Out=StructList(out)
        shape=Out.shape
        return np.array(Out.flatten())
    dout=jacobian(eval_model)(inputs_values)
    Dout = StructList(dout, 'flattened', shape)
    return Dout.unflatten()