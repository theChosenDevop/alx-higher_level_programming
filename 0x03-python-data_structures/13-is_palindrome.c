#include "lists.h"

/**
 * is_palindrome - print integers of palindrome
 * @head: array of integers
 * Return: 0 if it is not palindrome or 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;

	if (*head != NULL || (*head)->next != NULL)
	{
		while (fast && fast->next)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
			slow = slow->next;

		second_half = slow;
		reverse_list(&second_half);

		slow = *head;
		while (second_half)
		{
			if (second_half->n != slow->n)
				return (0);
			second_half = second_half->next;
			slow = slow->next;
		}
		reverse_list(&second_half);
		prev_slow->next = second_half;
	}
	else
	{
		/* Handle the case of an empty list */
		return (1);
	}

	return (1);
}


/**
 * reverse_list - reverse a singly linked list
 * @head: array
 * Return: void
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL, *curr = *head;

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
