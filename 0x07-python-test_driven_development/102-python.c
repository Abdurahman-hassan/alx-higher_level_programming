#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - print an information of Python string object.
 * @p: Pointer to the PyObject representing the Python string.
 * This function prints details about the given Python string object
 * including its type, length, and value.
 * If the given object is not a Python string object
 * it prints an error message.
 * Return: void
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	const char *value = NULL;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8(p);

	printf("  length: %lu\n", length);
	printf("  value: %s\n", value);
}