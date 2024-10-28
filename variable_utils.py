def sort_variables(lst):
    """
    Sorts a list of variables in ascending order.
    """
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
    """
    Creates a specified number of variables with a given name prefix and sets their values.
    """
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


def delete_variables(amount, var_nme):
    """
    Deletes a specified number of variables with a given name prefix.
    """
    for i in range(amount):
        var_name = f"{var_nme}_{i+1}"
        if var_name in globals():
            del globals()[var_name]


def get_variable_names(amount, var_nme):
    """
    Returns a list of variable names with a given prefix.
    """
    var_names = []
    for i in range(amount):
        var_name = f"{var_nme}_{i+1}"
        var_names.append(var_name)
    return var_names


def get_variable_values(amount, var_nme):
    """
    Returns a list of variable values with a given prefix.
    """
    var_values = []
    for i in range(amount):
        var_name = f"{var_nme}_{i+1}"
        if var_name in globals():
            var_values.append(globals()[var_name])
    return var_values


def set_variable_values(amount, var_nme, values):
    """
    Sets the values of a specified number of variables with a given name prefix.
    """
    if len(values) < amount:
        raise ValueError("List of values is too short")
    for i in range(amount):
        var_name = f"{var_nme}_{i+1}"
        globals()[var_name] = values[i]


def swap_variable_values(var_nme1, var_nme2):
    """
    Swaps the values of two variables.
    """
    if var_nme1 in globals() and var_nme2 in globals():
        temp = globals()[var_nme1]
        globals()[var_nme1] = globals()[var_nme2]
        globals()[var_nme2] = temp


def copy_variable_value(src_var_nme, dst_var_nme):
    """
    Copies the value of one variable to another.
    """
    if src_var_nme in globals():
        globals()[dst_var_nme] = globals()[src_var_nme]
