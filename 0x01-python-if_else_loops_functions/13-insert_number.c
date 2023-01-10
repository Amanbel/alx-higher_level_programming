#include "lists.h"

/**
 * insert_node - insert a node at the beginning of the list
 * @head: first node
 * @number: data about to be inserted
 * Return: address of new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		new->next = ptr;
		*head = new;
		return (new);
	}

	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
