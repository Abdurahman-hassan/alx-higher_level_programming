#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UNICODE *unicode = PyUnicode_AsUnicode(p);
    const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";

    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %zd\n", length);
    printf("  value: %ls\n", unicode);
}
