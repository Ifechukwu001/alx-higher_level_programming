#include <object.h>
#include <listobject.h>
#include <stdio.h>
/**
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, allocated, iter_no;
	PyObject* value;
	
	if (PYLIST_CHECK(p))
	{
		list_size = PyList_Size(p);
		allocated = Py_SIZE(p);

		printf("[*] Size of the Python List = %d\n", list_size);
		printf("[*] Allocated = %d\n", allocated);
		for  (iter_no = 0; iter_no < list_size; iter_no)
		{
			value = PyList_GetItem(p, iter_no);
			printf("Element %d: %s\n", iter_no, Py_TYPE(value));
		}
	}
}
