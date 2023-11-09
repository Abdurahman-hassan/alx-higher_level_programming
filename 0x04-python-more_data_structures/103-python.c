#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/*
 * print_python_bytes - Prints information about Python bytes objects.
 * @p: PyObject pointer to a Python bytes object.
 *
 * This function checks if the given PyObject is a bytes object and,
 * if so, prints its size, the string it contains, and the first ten bytes
 * of its contents in hexadecimal format. If the object is not a valid
 * bytes object, it outputs an error message.
 */
void print_python_bytes(PyObject *p)
{
	long int byte_size; /* Size of the bytes object. */
	int index;          /* Loop index for iterating over bytes. */
	char *byte_content; /* Pointer to bytes object content. */

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) /* Check if PyObject is a bytes object. */
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Retrieves content and size of bytes object. */
	PyBytes_AsStringAndSize(p, &byte_content, &byte_size);

	printf("  size: %li\n", byte_size);
	printf("  trying string: %s\n", byte_content);
	printf("  first %li bytes:", byte_size < 10 ? byte_size + 1 : 10);

	/* Print up to the first 10 bytes of the bytes object. */
	for (index = 0; index <= byte_size && index < 10; index++)
		printf(" %02hhx", byte_content[index]);
	printf("\n");
}

/*
 * print_python_list - Prints information about Python list objects.
 * @p: PyObject pointer to a Python list object.
 *
 * This function outputs the size of the list, the allocated memory for it,
 * and details of each element contained within the list, including their type.
 * If an element is a bytes object, it calls print_python_bytes to print
 * further information about the bytes object.
 */
void print_python_list(PyObject *p)
{
	long int list_size = PyList_Size(p); /* Number of items in the list. */
	PyListObject *list_obj = (PyListObject *)p; /* Cast to PyListObject. */
	const char *element_type; /* Type name of the list element. */

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", list_obj->allocated);

	/* Iterate over each element in the list and print its type. */
	for (int i = 0; i < list_size; i++)
	{
		element_type = Py_TYPE(list_obj->ob_item[i])->tp_name;
		printf("Element %i: %s\n", i, element_type);

		/* If element is a bytes object, call print_python_bytes. */
		if (PyBytes_Check(list_obj->ob_item[i]))
			print_python_bytes(list_obj->ob_item[i]);
	}
}

