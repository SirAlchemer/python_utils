import traceback
from typing import Any

def log(file_name: str, var_data: dict[str, Any], extra_details: str = None) -> None:
    with open(file_name, 'a') as f:
        f.write(traceback.format_exc())
        f.write("\n--------------\n\n")
        for name, value in var_data.items():
            if type(value) == str:
                f.write(f'{name}="{value}"\n')
            else:
                f.write(f'{name}={value}\n')
        if extra_details:
            f.write(f'\n{extra_details}\n~~~~~~~~~~~~~~~~~~\n\n')
        else:
            f.write('\n~~~~~~~~~~~~~~~~~~\n\n')
