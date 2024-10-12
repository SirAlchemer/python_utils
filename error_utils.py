

def raise_error(ErrorName: str, message: str):
    if isinstance(ErrorName, str):
        CustomError = type(ErrorName, (Exception,), {})
        raise CustomError(message)

