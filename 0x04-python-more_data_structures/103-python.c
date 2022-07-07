#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t list_size, allocated;
	PyListObject *list;
	int i;
	const char *type;

	if (PyList_Check(p))
	{
		list = (PyListObject *)p;
		printf("[*] Python list info\n");

		list_size = PyList_Size(p);
		printf("[*] Size of the Python List = %d\n", (int)list_size);

		allocated = list->allocated;
		printf("[*] Allocated = %d\n", (int)allocated);

		for (i = 0; i < (int)list_size; i++)
		{
			type = list->ob_item[i]->ob_type->tp_name;
			printf("Element %d: %s\n", i, type);
		}

		
	}
}


void print_python_bytes(PyObject *p)
{
	Py_ssize_t byte_size, limit;
	char *test_str;
	PyBytesObject *obj;
	int i;

	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");

		byte_size = PyBytes_Size(p);
		printf("  size: %d\n", (int)byte_size);

		test_str = PyBytes_AsString(p);
		printf("  trying string: %s\n", test_str);

		if (byte_size >= 10)
			limit = 10;
		else
			limit = byte_size + 1;
		
		printf("  first %lu bytes:", limit);
		for (i = 0; i < limit; i++)
		{
			obj = (PyBytesObject *)p;
			if (obj->ob_sval[i] >= 0)
				printf(" %02x", obj->ob_sval[i]);
			else
				printf(" %02x", 256 + obj->ob_sval[i]);
		}
		putchar('\n');
	}
}
