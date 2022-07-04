#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current, *end;
	int i, elem_no = 0;

	current = *head;
	while (current)
	{
		elem_no++;
		current = current->next;
	}

	current = *head;
	end = NULL;
	while (current != end)
	{
		end = current;
		for (i = 1; i != elem_no; i++)
			end = end->next;
		if (current->n == end->n)
		{
			current = current->next;
			elem_no -= 2;
		}
		else
			return (0);
	}
	return (1);
}
