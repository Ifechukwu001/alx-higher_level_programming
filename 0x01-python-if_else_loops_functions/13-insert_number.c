#include "lists.h"

/**
 * insert_node - inserts a new node at an index of a sorted list.
 * @head: Pointer to the HEAD of the list.
 * @number: Data to be inserted.
 * Return: Pointer to the new node or NULL if unsuccessful.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_item, *next_item, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (0);

	new->n = number;

	current_item = *head;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		while (current_item)
		{
			if (current_item->next)
			{
				next_item = current_item->next;
				if ((*head)->n > new->n)
				{
					new->next = *head;
					*head = new;
					break;
				}
				else if ((current_item->n <= new->n)
					 && (new->n <= next_item->n))
				{
					new->next = next_item;
					current_item->next = new;
					break;
				}
				current_item = current_item->next;
				continue;
			}
			current_item->next = new;
			new->next = NULL;
			current_item = current_item->next;
		}
	}
	return (new);
}
