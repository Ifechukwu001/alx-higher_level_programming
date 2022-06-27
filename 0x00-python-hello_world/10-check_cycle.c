#include "lists.h"

/**
 * check_cycle - Checks if a list is circular.
 * @list: Pointer to the first element of the list.
 * Return: 0 if there is no cycle, 1 if there is.
 */
int check_cycle(listint_t *list)
{
	size_t bufsize = 2, i, elem = 0;
	listint_t **buffer = malloc(bufsize * sizeof(listint_t*));
	listint_t *current = list;

	if (buffer == NULL)
		return (-1);

	while (current)
	{
		for (i = 0; i < elem; i++)
		{
			if (current == buffer[i])
			{
				free(buffer);
				return  (1);
			}
		}
		if (elem == bufsize)
		{
			bufsize += 2;
			buffer = realloc(buffer, bufsize * sizeof(listint_t*));
		}
		buffer[elem] = current;
		elem++;
		current = current->next;
	}
	free(buffer);
	return (0);
}
