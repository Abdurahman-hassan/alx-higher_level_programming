#include <Python.h>
#include <listobject.h>
#include <bytesobject.h>

/* Function to display information about byte objects in Python */
void display_python_bytes(PyObject *py_object)
{
	long bytes_size;
	char *bytes_content = NULL;

	printf("[.] bytes object info\n");

	/* Validate that the object is a bytes object */
	if (!PyBytes_Check(py_object))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Retrieve string and its length from the bytes object */
	PyBytes_AsStringAndSize(py_object, &bytes_content, &bytes_size);

	printf("  size: %ld\n", bytes_size);
	printf("  trying string: %s\n", bytes_content);

	/* Print up to 10 bytes of the bytes object */
	printf("  first %ld bytes:", (bytes_size < 10) ? bytes_size + 1 : 10);
	for (int index = 0; index <= bytes_size && index < 10; ++index)
	{
		printf(" %02hhx", bytes_content[index]);
	}
	printf("\n");
}

/* Function to display information about list objects in Python */
void display_python_list(PyObject *py_object)
{
	PyListObject *py_list = (PyListObject *)py_object;
	long list_size = PyList_Size(py_object);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", py_list->allocated);

	/* Iterate over the list and print details about each element */
	for (int index = 0; index < list_size; ++index)
	{
		PyObject *item = PyList_GET_ITEM(py_list, index);
		const char *item_type = item->ob_type->tp_name;

		printf("Element %d: %s\n", index, item_type);

		/* If the list element is a bytes object, display its info */
		if (PyBytes_Check(item))
		{
			display_python_bytes(item);
		}
	}
}

