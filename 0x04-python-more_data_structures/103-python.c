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
		printf("[*] Size of the Python List = %d\n", list_size);

		allocated = list->allocated;
		printf("[*] Allocated = %d", allocated);

		for (i = 0; list->ob_item[i] != NULL; i++)
		{
			type = list->ob_item[i]->ob_type->tp_name;
			printf("Element %d: %s\n", i, type);
		}

		
	}
}


void print_python_bytes(PyObject *p)
{
	
}
