def get_my_previous_variable():
    my_previous_variable = 100
    return my_previous_variable

def two_plus_three():
    a = 2
    b = 3
    c = a+b
    print (f'The result of adding {a}+{b} is {c}')
    return c

def add_100(my_previous_variable):
    my_previous_variable = my_previous_variable + 100
    print (f'The result of adding 100 to my_previous_variable is {my_previous_variable}')
    return my_previous_variable

def multiply_by_two(c):
    d = c*2
    print (f'Two times {c} is {d}')
    return d

def analyze(x):
    x = [1, 2, 3]
    y = [100, 200, 300]
    z = [u+v for u,v in zip(x,y)]
    product = [u*v for u, v in zip(x,y)]

# -----------------------------------------------------
# pipeline
# -----------------------------------------------------
def index_pipeline (test=False, load=True, save=True, result_file_name="index_pipeline"):
    """Pipeline calling each one of the functions defined in this module."""
    
    # load result
    result_file_name += '.pk'
    path_variables = Path ("index") / result_file_name
    if load and path_variables.exists():
        result = joblib.load (path_variables)
        return result

    my_previous_variable = get_my_previous_variable ()
    c = two_plus_three ()
    my_previous_variable = add_100 (my_previous_variable)
    d = multiply_by_two (c)
    analyze (x)

    # save result
    result = Bunch (d=d,my_previous_variable=my_previous_variable,c=c)
    if save:    
        path_variables.parent.mkdir (parents=True, exist_ok=True)
        joblib.dump (result, path_variables)
    return result

