#include <stdio.h>
#include "lists.h"

/*
 * check_cycle - checks cycle in linked list
 * @list: linked list
 * Return: 0 if no cycle 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *Sptr = list;
	listint_t *Fptr = list;

	while (Sptr != NULL && Fptr != NULL && Fptr->next != NULL)
	{
		Sptr = Sptr->next;
		Fptr = Fptr->next;

		if (Sptr == Fptr)
		{
			return (1);
		}
	}
	return (0);
}
