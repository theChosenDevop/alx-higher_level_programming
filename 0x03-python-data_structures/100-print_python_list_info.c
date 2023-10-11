#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info: prints python list information
 * @p: Python Object list
 */
void print_python_list_info(PyObject *p)
{
	int obj_size, i, obj_alloc;
	PyObject *obj;

	obj_size = Py_SIZE(p);
	obj_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", obj_size);
	printf("[*] Allocated = %d\n", obj_alloc);

	for (i = 0; i < obj_size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
