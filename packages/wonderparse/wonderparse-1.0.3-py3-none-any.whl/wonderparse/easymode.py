import wonderparse.execution as _execution
import wonderparse.parser as _parser
import wonderparse.process_namespace as _process_namespace


def simple_run(*, 
    args, 
    program_object,
    endgame='print',
    exception_repr=False,
    **kwargs,
):
    endgame = _endgame(endgame)
    parser = _parser.by_object(program_object, **kwargs)
    ns = parser.parse_args(args)
    funcInput = _process_namespace.by_object(program_object, namespace=ns)
    if len(vars(ns)):
        raise ValueError(f"Some arguments in the namespace were not processed: {ns}")
    try:
        result = _execution.by_object(program_object, funcInput=funcInput)
    except Exception as exc:
        if 'prog' in kwargs.keys():
            msgA = f"Running {kwargs['prog']} failed:"
        else:
            msgA = "Error:"
        if exception_repr:
            msgB = exc.__repr__()
        else:
            msgB = str(exc)
        msg = msgA + " " + msgB
        raise SystemExit(msg)
    return endgame(result)
    
def iterprint(values):
    for value in values:
        print(value)

def _endgame(value):
    if type(value) is not str:
        return value
    if value == 'print':
        return print
    if value == 'iterprint':
        return iterprint
    if value == 'return':
        return _return
    raise ValueError(f"{value.__repr__()} is not a legal value for endgame.")

def _return(value):
    return value

