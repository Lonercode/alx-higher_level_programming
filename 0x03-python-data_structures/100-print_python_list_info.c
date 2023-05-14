#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
int item;
long int size = PyList_Size(p);
PyListObject *objct = (PyListObject *)p;
printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", objct->allocated);
for (item = 0; item < size; item++)
	printf("Element %i: %s\n", item, Py_TYPE(objct->ob_item[item])->tp_name);
}
