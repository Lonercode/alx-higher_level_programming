#include "lists.h"

/**
 * insert_node - Insertingh a number into a sorted singly-linked list.
 * @head: Head Pointer
 * @number: The number
 * Return: Null or Pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *another;
another = malloc(sizeof(listint_t));
if (another == NULL)
{
return (NULL);
}
another->n = number;
if (node == NULL || node->n >= number)
{
another->next = node;
*head = another;
return (another);
}
while (node && node->next && node->next->n < number)
{
node = node->next;
}
another->next = node->next;
node->next = another;

return (another);
}
