#include "lists.h"

/**
 * insert_node - insert a node at the beginning of the list
 * @head: first node
 * @number: data about to be inserted
 * Return: address of new node or NULL if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	ptr->next = NULL;

	ptr->next = *head;
	*head = ptr;

	return (ptr);
}
