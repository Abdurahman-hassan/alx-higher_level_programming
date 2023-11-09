#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/* Forward declaration of print_python_bytes */
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	const char *type_name;

	printf("[*] Python list info\n");
	/* Directly accessing the ob_size field of the object's var part */
	printf("[*] Size of the Python List = %zd\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size; i++) {
		item = list->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i, type_name);
		if (PyBytes_Check(item)) {
			print_python_bytes(item);
		}
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytesObject *bytes = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	printf("  size: %zd\n", PyBytes_GET_SIZE(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %zd bytes:", PyBytes_GET_SIZE(p) < 10 ? PyBytes_GET_SIZE(p) + 1 : 10);

	for (Py_ssize_t i = 0; i < PyBytes_GET_SIZE(p) && i < 10; i++) {
		printf(" %02x", bytes->ob_sval[i] & 0xff);
	}
	printf("\n");
}

