#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: The head of the dlistint_t list.
 *
 * Return: The number of nodes in the list.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t nodes = 0;

	while (h)
	{
		nodes++;  /* Increment the number of nodes */
		printf("%d\n", h->n);  /* Print the value of the current node */
		h = h->next;  /* Move to the next node */
	}

	return (nodes);
}
