#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Displays details of a Python byte object
 * @p: Python object to be examined
 *
 * This function outputs information about a Python byte object,
 * such as its length, first 10 bytes in hex, and its string form.
 * If the object isn't a valid byte object, an error is indicated.
 */
void print_python_bytes(PyObject *p)
{
	long int i, size;
	char *str;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", (size >= 10 ? 10 : size + 1));

	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size && i < 9)
			printf(" ");
	}

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * display_float_data - Displays details of a Python float object
 * @p: Python object to be examined
 *
 * This function outputs the value of a Python float object.
 * If the object isn't a valid float object, an error is indicated.
 */
void print_python_float(PyObject *p)
{
	double value;
	char *num_buf;

	setbuf(stdout, NULL);

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	num_buf = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0,
			Py_DTST_FINITE);

	printf("  value: %s\n", num_buf);
	setbuf(stdout, NULL);
	PyMem_Free(num_buf);
}

/**
 * display_list_data - Displays details of a Python list object
 * @p: Python object to be examined
 *
 * This function outputs information about a Python list object,
 * including its size, allocated space, and elements.
 * If an element is a byte or float object, it is further examined.
 */
void print_python_list(PyObject *p)
{
	long int i, size, allocated;
	PyObject *element;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, element->ob_type->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);

		if (PyFloat_Check(element))
			print_python_float(element);
	}
	setbuf(stdout, NULL);
}