#include "lists.h"

/**
 * reverse_listint - Reverses the second half of the list
 * @head: Pointer to the head of the list
 * Return: Pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head;
    listint_t *second_half, *prev_slow = *head;
    listint_t *midnode = NULL;  // To handle odd size list
    int result = 1;  // Assume list is palindrome

    if (*head != NULL && (*head)->next != NULL)
    {
        // Find the middle of the list (slow will point to it)
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        // For odd sized lists, skip the middle element
        if (fast != NULL)
        {
            midnode = slow;
            slow = slow->next;
        }

        // Reverse the second half of the list
        second_half = reverse_listint(&slow);
        prev_slow->next = NULL; // Terminate first half

        // Check if the list is palindrome
        result = compare_lists(*head, second_half);

        // Reconstruct the original list (reverse the second half back)
        reverse_listint(&second_half);

        // If there was a mid node (odd size list), add it back
        if (midnode != NULL)
        {
            prev_slow->next = midnode;
            midnode->next = second_half;
        }
        else  // else just join the two halves
        {
            prev_slow->next = second_half;
        }
    }

    return result;
}

/**
 * compare_lists - Compares two lists to check if they are the same
 * @head1: Pointer to the head of the first list
 * @head2: Pointer to the head of the second list
 * Return: 1 if the lists are the same, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
    listint_t *temp1 = head1;
    listint_t *temp2 = head2;

    while (temp1 && temp2)
    {
        if (temp1->n == temp2->n)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else
            return 0;
    }

    // If both lists are traversed and no mismatches are found
    if (temp1 == NULL && temp2 == NULL)
        return 1;

    return 0; // If one of the lists has not ended, they are not the same
}