#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
}

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	char *str = PyBytes_AsString(p);
	printf("[.] size: %zd\n", size);
}

void print_python_float(PyObject *p) {
	if (!PyFloat_Check(p)) {
		printf("[ERROR] Invalid Float Object\n");
		return;
	}
	double value = PyFloat_AsDouble(p);
	printf("[.] value: %f\n", value);
}

