#include <Python.h>
#include <stdio.h>

void display_python_bytes(PyObject *obj);
void display_python_float(PyObject *obj);
void display_python_list(PyObject *obj);

/**
 * display_python_bytes - Displays details of a Python bytes object
 * @obj: Pointer to the Python object to inspect
 *
 * Outputs size, a snippet of the bytes, and attempts to print it as a string.
 * Reports error if not a bytes object.
 */
void display_python_bytes(PyObject *obj)
{
	long int index, byte_count;
	char *byte_sequence;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(obj)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_count = PyBytes_Size(obj);
	byte_sequence = PyBytes_AsString(obj);

	printf("  size: %ld\n", byte_count);
	printf("  trying string: %s\n", byte_sequence);
	printf("  first %ld bytes: ", (byte_count > 10 ? 10 : byte_count + 1));

	for (index = 0; index < byte_count && index < 10; index++) {
		printf("%02x", (unsigned char)byte_sequence[index]);
		if (index < 9) printf(" ");
	}
	printf("\n");
}

/**
 * display_python_float - Displays details of a Python float object
 * @obj: Pointer to the Python object to inspect
 *
 * Outputs the value of the float object.
 * Reports error if not a float object.
 */
void display_python_float(PyObject *obj)
{
	double float_value;
	char *formatted_value;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(obj)) {
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_value = PyFloat_AsDouble(obj);
	formatted_value = PyOS_double_to_string(float_value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf("  value: %s\n", formatted_value);
	PyMem_Free(formatted_value);
}

/**
 * display_python_list - Displays details of a Python list object
 * @obj: Pointer to the Python list object
 *
 * Outputs the size, allocated space, and elements of the list.
 * For bytes and float elements, uses dedicated functions.
 */
void display_python_list(PyObject *obj)
{
	long int index, list_size, alloc_size;
	PyObject *item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(obj)) {
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_size = PyList_Size(obj);
	alloc_size = ((PyListObject *)obj)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", alloc_size);

	for (index = 0; index < list_size; index++) {
		item = PyList_GetItem(obj, index);
		printf("Element %ld: %s\n", index, item->ob_type->tp_name);
		if (PyBytes_Check(item)) display_python_bytes(item);
		if (PyFloat_Check(item)) display_python_float(item);
	}
}

