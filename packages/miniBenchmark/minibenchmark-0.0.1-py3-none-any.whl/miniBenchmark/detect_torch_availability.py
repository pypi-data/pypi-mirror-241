""" Detect if torch is in the environment, CUDA, GRAM and how CPU memory channel accessible
"""
import torch
def detect_torch():
    try:
        import torch
        
        torch_version = torch.__version__
        installed  =True
        gpu = True if torch.cuda.is_available() else False
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print('Using device:', device)

        device_property = torch.cuda.get_device_properties(0)
        #Additional Info when using cuda

    except:
        gpu = False
        installed = False

    torch_dict = {"installed" : installed,
                  "gpu" : gpu }

    if installed and gpu:
        torch_dict['primary_gpu_model'] = torch.cuda.get_device_name(0)
        torch_dict['major'] = device_property.major
        torch_dict['minor'] = device_property.minor
        torch_dict['total_memory'] = device_property.total_memory
        torch_dict['total_memory_GB'] = device_property.total_memory/1024/1024/1024
        torch_dict['multi_processor_count'] = device_property.multi_processor_count
# for 3090        major=8, minor=6, total_memory=24259MB, multi_processor_count=82


    
    return torch_dict


print(torch.cuda.get_device_name(0))
print(torch.cuda.get_device_properties(0))
print(detect_torch())
