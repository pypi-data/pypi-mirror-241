from typing import (
    get_type_hints,
    get_origin,
    get_args,
    Union,
    Any,
    Callable,
    Optional,
)
import inspect


def check_types(warnings: bool = True):
    """
    A decorator that checks the types of the arguments passed to a function.
    It raises a TypeError if the type of an argument is not compatible with the type hint.

    Parameters:
    -----------
    warnings : bool, optional
        Whether to print warnings when a type cannot be checked, by default True
    """

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            ### get type hints and variable names
            hints = get_type_hints(func)
            var_names = list(inspect.signature(func).parameters.keys())

            ### check args
            for arg_idx, arg in enumerate(args):
                arg_name = var_names[arg_idx]
                if arg_name in hints.keys():
                    check_type_hint(
                        var_name=arg_name,
                        var=arg,
                        type_hint=hints[arg_name],
                        func=func,
                        warnings=warnings,
                    )

            ### check kwargs
            for kwarg_name, kwarg in kwargs.items():
                check_type_hint(
                    var_name=kwarg_name,
                    var=kwarg,
                    type_hint=hints[kwarg_name],
                    func=func,
                    warnings=warnings,
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def check_class_base_rec(var_name, func, type_hint, args, base):
    ### check if args of type hint is equal to base, if yes, return None
    if not args == base:
        ### if not equal go deeper with base
        if base == None:
            ### if base already None, raise TypeError
            raise TypeError(
                f"Parameter {var_name} of function {func} should be a class of {get_args(type_hint)[0]}"
            )
        else:
            ### go deeper and check base of base of base
            return check_class_base_rec(var_name, func, type_hint, args, base.__base__)
    else:
        return None


def check_type_hint(
    var_name: str,
    var: Any,
    type_hint: type,
    func: Callable,
    warnings: bool,
    current_var: Optional[Any] = None,
    current_type_hint: Optional[type] = None,
) -> None:
    """
    Check if the type of the variable is compatible with the type hint

    Parameters
    ----------
    var_name : str
        Name of the variable
    var : Any
        Variable to check
    type_hint : type
        Type hint of the variable
    func : function
        Function that is checked
    current_var : Any, optional
        Current variable to check, used for recursive calls, by default None
    current_type_hint : type, optional
        Current type hint of the variable, used for recursive calls, by default None
    """

    ### set current_var and current_type_hint to var and type_hint if they are None
    if current_var is None:
        current_var = var
    if current_type_hint is None:
        current_type_hint = type_hint

    # print(
    #     f"var_name: {var_name}, var: {current_var}, var_type: {type(current_var)}, current_type_hint: {current_type_hint}, origin: {get_origin(current_type_hint)}, args: {get_args(current_type_hint)}"
    # )

    ### depending on origin of type hint doe different things
    ### if origin is type
    ### check if args of type hint is equal to var
    ### if not, check if equal to base of var recursively
    ### if never true, raise TypeError
    if get_origin(current_type_hint) is type:
        ### Type expects a class, first check if var is a class
        if not inspect.isclass(current_var):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be a class of {get_args(type_hint)[0]}"
            )
        ### check if args of type hint is equal to var, if yes, return None
        if get_args(current_type_hint)[0] == current_var:
            return None
        else:
            ### if not equal, check if base class is equal to args of type hint
            return check_class_base_rec(
                var_name,
                func,
                type_hint,
                args=get_args(current_type_hint)[0],
                base=current_var.__base__,
            )

    ### if origin is dict
    ### check if type is dict
    ### check if type of all keys and vals are correct
    ### do this by calling function check_type_hint recursively
    if get_origin(current_type_hint) is dict:
        ### check if type is dict
        if not isinstance(current_var, dict):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        ### passed dict check, now check if type of keys and vals are correct
        type_key = get_args(current_type_hint)[0]
        type_val = get_args(current_type_hint)[1]
        for key, val in current_var.items():
            check_type_hint(
                var_name=key,
                var=var,
                type_hint=type_hint,
                func=func,
                warnings=warnings,
                current_var=key,
                current_type_hint=type_key,
            )
            check_type_hint(
                var_name=key,
                var=var,
                type_hint=type_hint,
                func=func,
                warnings=warnings,
                current_var=val,
                current_type_hint=type_val,
            )
        ### variable passed all checks, return None
        return None

    ### if origin is list
    ### check if type is list
    ### check if type of all elements is correct
    ### do this by calling function check_type_hint recursively
    elif get_origin(current_type_hint) is list:
        ### check if type is list
        if not isinstance(current_var, list):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        ### passed list check, now check if type of all elements is correct
        type_element = get_args(current_type_hint)[0]
        for element in current_var:
            check_type_hint(
                var_name=var_name,
                var=var,
                type_hint=type_hint,
                func=func,
                warnings=warnings,
                current_var=element,
                current_type_hint=type_element,
            )
        ### variable passed all checks, return None
        return None

    ### if origin is Union
    ### check if variable is one of the types in the union
    ### do this by calling function check_type_hint recursively
    elif get_origin(current_type_hint) is Union or get_origin(
        current_type_hint
    ) is type(str | int):
        ### check if variable is any of the types in the union
        for type_ in get_args(current_type_hint):
            ### need a try except here because we want to check all types in the union and not stop at the first one that fails
            try:
                check_type_hint(
                    var_name=var_name,
                    var=var,
                    type_hint=type_hint,
                    func=func,
                    warnings=warnings,
                    current_var=current_var,
                    current_type_hint=type_,
                )
                ### variable passed one check, return None
                return None
            except:
                pass
        ### variable did not pass any checks, raise TypeError
        raise TypeError(
            f"Parameter {var_name} of function {func} should be {type_hint}"
        )

    ### if origin is None, its a simple type and we can check it directly using isinstance
    elif get_origin(current_type_hint) is None:
        ### check if variable is an instance of the type hint, if not raise TypeError
        if not isinstance(current_var, current_type_hint):
            raise TypeError(
                f"Parameter {var_name} of function {func} should be {type_hint}"
            )
        else:
            return None

    ### if variable passed all checks without errors or returning, print that the type cannot be checked
    if warnings:
        print(
            f"WARNING check_type_hint: Variable {var_name} with type {type(var)} of function {func} could not be checked."
        )
    return None
