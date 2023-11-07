#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Validates whether a linked list is symmetrical.
 *
 * @head: Double pointer to the start of the list.
 *
 * Return: 1 if the list mirrors itself, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *end;
	int count = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	end = *head;

	while (end->next)
	{
		count++;
		end = end->next;
	}

	if (count == 1 && (*head)->n == end->n)
		return (1);

	return (evaluate_palindrome(*head, end));
}

/**
 * evaluate_palindrome - Helper function to determine if a list reads the same backwards.
 *
 * @start: Pointer to the beginning node of the list.
 * @end: Pointer to the end node of the list.
 *
 * Return: 1 if the segment is symmetrical, 0 if it is not.
 */
int evaluate_palindrome(listint_t *start, listint_t *end)
{
	if (!start || (start == end && start->n == end->n) || !end)
		return (1);

	if (start->n != end->n)
		return (0);

	// Move towards the middle of the list, comparing nodes from both ends
	return (evaluate_palindrome(start->next, end - 2));
}
