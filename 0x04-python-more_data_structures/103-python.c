#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyListObject *list = (PyListObject *)p;
    PyObject *item;
    const char *type_name;

    printf("[*] Python list info\n");

    /* Casting to list object and retrieving size and allocated properties */
    size = PyVarObject_HEAD_INIT(NULL, 0).ob_size;
    allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    /* Loop through each item of the list */
    for (i = 0; i < size; i++) {
        item = list->ob_item[i];
        type_name = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, type_name);
        /* If it's a bytes object, call the print_python_bytes function */
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *trying_str;
    unsigned char *bytes_str;

    printf("[.] bytes object info\n");

    /* Check if it is indeed a bytes object */
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Getting size of bytes object */
    size = ((PyVarObject *)p)->ob_size;

    printf("  size: %zd\n", size);

    /* Trying to print the string if it's valid UTF-8, otherwise it's not safe */
    trying_str = PyBytes_AsString(p);
    if (trying_str != NULL)
        printf("  trying string: %s\n", trying_str);

    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

    bytes_str = (unsigned char *)((PyBytesObject *)p)->ob_sval;
    for (i = 0; i < size && i < 10; i++) {
        printf(" %02x", bytes_str[i]);
    }
    printf("\n");
}
