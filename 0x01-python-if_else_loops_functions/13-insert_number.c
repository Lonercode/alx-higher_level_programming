#include "lists.h"

/**
 * insert_node - Inserting a number into a sorted singly-linked list.
 * @head: Head Pointer
 * @number: Number
 * Return: Pointer or Null
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *n;
n = malloc(sizeof(listint_t));
if (n == NULL)
{
return (NULL);
}
n->ne = number;
if (node == NULL || node->ne >= number)
	{
		n->next = node;
		*head = n;
		return (n);
	}

	while (node && node->next && node->next->ne < number)
		node = node->next;

	n->next = node->next;
	node->next = n;

	return (n);
}
