

def sort_variables(lst):
    amount = len(lst)
    for i in range(amount):
        var_name = f"var_{i + 1}"
        globals()[var_name] = [lst[i]]

    for i in range(amount):
        var_name = f"var_{i + 1}"
        is_lowest = True
        for j in range(amount):
            if i != j:
                other_var_name = f"var_{j + 1}"
                if globals()[var_name][0] > globals()[other_var_name][0]:
                    is_lowest = False
                    break

    # sort the variables
    sorted_vars = []
    for i in range(amount):
        var_name = f"var_{i + 1}"
        sorted_vars.append(globals()[var_name][0])
    sorted_vars.sort()
    for i in range(amount):
        var_name = f"var_{i + 1}"
        globals()[var_name] = [sorted_vars[i]]
    return sorted_vars


def create_variables(amount, set_all_to, var_nme, lst=None):
    if lst is not None:
        if len(lst) < amount:
            raise ValueError("List is too short")
        for i in range(amount):
            var_name = f"{var_nme}_{i+1}"
            globals()[var_name] = lst[i]
    else:
        for i in range(amount):
            var_name = f"{var_nme}_{i+1}"
            globals()[var_name] = set_all_to
