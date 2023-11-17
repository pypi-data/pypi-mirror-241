#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "dtypes.h"


PyObject *
test(PyObject *self, PyObject *Py_UNUSED(ignored))
{
    printf("This is a test string!\n");
    Py_RETURN_NONE;
}
