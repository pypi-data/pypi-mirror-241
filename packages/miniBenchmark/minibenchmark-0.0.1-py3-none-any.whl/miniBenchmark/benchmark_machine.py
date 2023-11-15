"""sample_task
"""


from .generate_data_tasks import *
from .upscale_task import upscale_task
from .invert_matrix import task_matrix_inversion

def matrix_inversion_cpu(hpo):
    return upscale_task(task_matrix_inversion, hpo)



from .FFT_power_spectral import task_fft, task_fft_2d


def fft_cpu(hpo):
    return upscale_task(task_fft, hpo)

def fft_2d_cpu(hpo):
    return upscale_task(task_fft,hpo)

from .PDE_BVP import task_wave_pde_2d

def wave_pde_cpu(hpo):
    return upscale_task(task_wave_pde_2d ,hpo)

from .tab_dae import task_tab_dae

def tab_dae_tf(hpo):
    return upscale_task(task_tab_dae,hpo)

from .Forests import task_if_all, task_rf_all


def task_if_all_sk(hpo):
    return upscale_task(task_if_all,hpo)


def task_rf_all_sk(hpo):
    return upscale_task(task_rf_all,hpo)


from time import time

t0=time()

tasks = {"matrix_inversion_cpu" : (matrix_inversion_cpu,[2**10, 2**12, 2**14]),
         "fft_cpu" : (fft_cpu, [2**24, 2**26, 2**28]),
         "fft_2d_cpu":(fft_2d_cpu, [2**20, 2**22, 2**24]),
         "wave_pde_cpu": (wave_pde_cpu,[2**20, 2**22, 2**24]),
         "tab_dae_tf": (tab_dae_tf, [10,]),
         "rf_sk" : (task_rf_all_sk, [2**18, 2**20,2**22]),
         "if_sk" : (task_if_all_sk, [2**18, 2**20,2**22]),
         }


def run_tasks(tasks):
    results = {}
    for k, v in tasks.items():
        results[k]=v[0](v[1])
    return results

#results = run_tasks(tasks)
#print(results)
#print(time()-t0)
