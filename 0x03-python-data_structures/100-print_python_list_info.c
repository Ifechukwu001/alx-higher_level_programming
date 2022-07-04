#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
/**
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, allocated, iter_no;
	const char *value;
	
	if (PyList_Check(p))
	{
		list_size = PyList_Size(p);
		allocated = Py_SIZE(p);

		printf("[*] Size of the Python List = %d\n", (int)list_size);
		printf("[*] Allocated = %d\n", (int)allocated);
		for  (iter_no = 0; iter_no < list_size; iter_no++)
		{
			value = (Py_TYPE(PyList_GetItem(p, iter_no)))->tp_name;
			printf("Element %d: %s\n", (int)iter_no, value);
		}
	}
}
