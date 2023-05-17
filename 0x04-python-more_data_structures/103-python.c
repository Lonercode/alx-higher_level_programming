#include <Python.h>
#include <bytesobject.h>
#include <listobject.h>
#include <object.h>

void print_python_bytes(PyObject *p)
{
long int size;
int l;
char *t_str = NULL;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

PyBytes_AsStringAndSize(p, &t_str, &size);
printf("  size: %li\n", size);
printf("  trying string: %s\n", t_str);
if (size < 10)
	printf("  first %li bytes:", size + 1);
else
	printf("  first 10 bytes:");
for (l = 0; l <= size && l < 10; l++)
	printf(" %02hhx", t_str[l]);
printf("\n");
}


void print_python_list(PyObject *p)
{
int l;
long int size = PyList_Size(p);
PyListObject *list = (PyListObject *)p;
const char *el;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", list->allocated);
for (l = 0; l < size; l++)
{
el = (list->ob_item[l])->ob_type->tp_name;
printf("Element %i: %s\n", l, el);
if (!strcmp(el, "bytes"))
	print_python_bytes(list->ob_item[l]);
}
}
