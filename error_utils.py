import logging


def raise_error(ErrorName: str, message: str, log_error: str = None) -> None:
    if log_error != None:
        CustomError = type(ErrorName, (Exception,), {})
        logging(log_error)
        raise CustomError(message)
    if not isinstance(ErrorName, str):
        raise ValueError(f'{ErrorName} is not a string!')
    CustomError = type(ErrorName, (Exception,), {})
    raise CustomError(message)

