#include "lists.h"

/**
 * is_palindrome - print integers of palindrome
 * @head: array of integers
 * Return: 0 if it is not palindrome or 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	listint_t *rev;
	listint_t *mid;
	size_t count = 0, i;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		count++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < ((count / 2) - 1); i++)
		temp = temp->next;

	if ((count % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_list(&temp);
	mid = rev;

	temp = *head;
	while (temp && rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_list(&mid);

	return (1);
}
/**
 * reverse_list - reverse a singly linked list
 * @head: array
 * Return: void
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev, *next, *curr = *head;

	while (curr)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*head = prev;
	return (*head);
}
