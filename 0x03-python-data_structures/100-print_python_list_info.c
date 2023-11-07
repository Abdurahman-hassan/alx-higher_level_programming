#include <Python.h>

/**
* print_python_list_info - prints some basic info about Python lists
* @p: pointer to PyObject
* Return: void
*/
void print_python_list_info(PyObject *p)
{
    /* Cast the PyObject to a PyListObject */
    PyListObject *list = (PyListObject *)p;

    /* Get the size of the list */
    Py_ssize_t size = PyList_Size(p);

    /* Get the allocated size of the list */
    Py_ssize_t allocated = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    /* Iterate over items of the list and print their types */
    for (Py_ssize_t i = 0; i < size; i++) {
        /* Get an item from the list */
        PyObject *item = PyList_GetItem(p, i);
        /* Get the item's type */
        PyTypeObject *type = Py_TYPE(item);
        /* Print the type of the item */
        printf("Element %zd: %s\n", i, type->tp_name);
    }
}
