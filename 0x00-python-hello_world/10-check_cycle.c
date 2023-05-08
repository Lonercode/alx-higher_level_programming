#include "lists.h"

/**
 * check_cycle - checks that a singly linked list has a cycle
 * @list: singly linked list
 *
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
listint_t *x = list;
listint_t *y = list;

if (!list)
{
return (0);
}

while (x && y && y->next)
{
x = x->next;
y = y->next->next;
if (x == y)
{
return (1);
}
}
return (0);
}
