#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list; /* Set slow pointer to the head of the list */
	fast = list->next; /* Set fast pointer to the next node */

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast) /*If slow and fast pointers meet, there is a cycle */
			return (1);

		slow = slow->next; /* Move slow pointer one step forward */
		fast = fast->next->next; /* Move fast pointer two steps forward */
	}
	return (0); /* If loop completes, there is no cycle */
}
