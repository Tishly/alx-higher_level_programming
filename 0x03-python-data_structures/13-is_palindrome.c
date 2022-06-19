#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	if (temp->next == 0)
		return (1);
	else
		return (0);
}
