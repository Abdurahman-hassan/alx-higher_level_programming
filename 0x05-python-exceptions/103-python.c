#include <Python.h>
#include <stdio.h>

void display_byte_data(PyObject *obj);
void display_float_data(PyObject *obj);
void display_list_data(PyObject *obj);

/**
 * display_byte_data - Displays details of a Python byte object
 * @obj: Python object to be examined
 *
 * This function outputs information about a Python byte object,
 * such as its length, first 10 bytes in hex, and its string form.
 * If the object isn't a valid byte object, an error is indicated.
 */
void display_byte_data(PyObject *obj)
{
	long int idx, byte_length;
	char *byte_str;

	setbuf(stdout, NULL);

	printf("[.] byte object details\n");

	if (!PyBytes_Check(obj))
	{
		printf("  [ERROR] Not a byte object\n");
		setbuf(stdout, NULL);
		return;
	}

	byte_length = PyBytes_Size(obj);
	byte_str = PyBytes_AsString(obj);

	printf("  length: %ld\n", byte_length);
	printf("  string: %s\n", byte_str);

	printf("  first %ld bytes: ", (byte_length > 10 ? 10 : byte_length));

	for (idx = 0; idx < byte_length && idx < 10; idx++)
	{
		printf("%02x", byte_str[idx] & 0xFF);
		if (idx < byte_length - 1)
			printf(" ");
	}

	printf("\n");
}

/**
 * display_float_data - Displays details of a Python float object
 * @obj: Python object to be examined
 *
 * This function outputs the value of a Python float object.
 * If the object isn't a valid float object, an error is indicated.
 */
void display_float_data(PyObject *obj)
{
	double float_val;
	char *float_str;

	setbuf(stdout, NULL);

	printf("[.] float object details\n");

	if (!PyFloat_Check(obj))
	{
		printf("  [ERROR] Not a float object\n");
		setbuf(stdout, NULL);
		return;
	}

	float_val = PyFloat_AsDouble(obj);
	float_str = PyOS_double_to_string(float_val, 'r', 0, Py_DTSF_ADD_DOT_0,
			Py_DTST_FINITE);

	printf("  value: %s\n", float_str);
	PyMem_Free(float_str);
}

/**
 * display_list_data - Displays details of a Python list object
 * @obj: Python object to be examined
 *
 * This function outputs information about a Python list object,
 * including its size, allocated space, and elements.
 * If an element is a byte or float object, it is further examined.
 */
void display_list_data(PyObject *obj)
{
	long int idx, list_size, list_allocated;
	PyObject *item;

	setbuf(stdout, NULL);

	printf("[*] Python list details\n");

	if (!PyList_Check(obj))
	{
		printf("  [ERROR] Not a list object\n");
		setbuf(stdout, NULL);
		return;
	}

	list_size = PyList_GET_SIZE(obj);
	list_allocated = ((PyListObject *)obj)->allocated;

	printf("[*] List size: %ld\n", list_size);
	printf("[*] Allocated: %ld\n", list_allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		item = PyList_GetItem(obj, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			display_byte_data(item);

		if (PyFloat_Check(item))
			display_float_data(item);
	}
}