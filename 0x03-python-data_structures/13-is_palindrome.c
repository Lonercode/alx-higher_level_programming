#include "lists.h"

/**
 * reverse_listint - reverse a linked list
 * @head: head pointer
 * Return: pointer
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current_one = *head;
	listint_t *next = NULL;
	while (current_one)
	{
		next = current_one->next;
		current_one->next = previous;
		previous = current_one;
		current_one = next;
	}
	*head = previous;
}

/**
 * is_palindrome - Is the linked list a palindrome?
 * @head: pointer
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *d = NULL;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			d = s->next;
			break;
		}
		if (!f->next)
		{
			d = s->next->next;
			break;
		}
		s = s->next;
	}

	reverse_listint(&d);

	while (d && t)
	{
		if (t->n == d->n)
		{
			d = d->next;
			t = t->next;
		}
		else
			return (0);
	}
	if (!d)
		return (1);

	return (0);
}
