#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints bytes formation
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	char *string = PyBytes_AS_STRING(bytes);
	Py_ssize_t size = PyBytes_GET_SIZE(bytes);
	Py_ssize_t limit = size >= 10 ? 10 : size + 1;
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", limit);
	for (i = 0; i < limit; i++)
	{
		unsigned char byte = string[i];

		printf(" %02x", byte);
	}
	printf("\n");
}

/**
 * print_python_list - prints bytes formation
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = Py_SIZE(p);
	Py_ssize_t i;

	printf("[.] Python list info\n");
	printf("[.]  Size of the Python List = %zd\n", size);
	printf("[.] Allocated = %zd\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *obj = list->ob_item[i];

		printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
