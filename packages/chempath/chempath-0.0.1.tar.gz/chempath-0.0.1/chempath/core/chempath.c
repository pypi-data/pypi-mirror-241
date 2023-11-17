#include "dtypes.h"


static PyMethodDef methods_module[] = {
    {"test", test, METH_VARARGS, "Test function."},
    {NULL},
};

static PyModuleDef module__chempath = {
    PyModuleDef_HEAD_INIT,
    .m_name    = "_chempath",
    .m_doc     = "C implementation of chempath.",
    .m_size    = -1,
    .m_methods = methods_module,
};

PyMODINIT_FUNC PyInit__chempath(void)
{
    PyObject *m;
    m = PyModule_Create(&module__chempath);

    if (!m)
        return NULL;

    return m;
}
