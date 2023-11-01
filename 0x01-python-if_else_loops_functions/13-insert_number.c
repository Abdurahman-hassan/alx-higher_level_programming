#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to head of list
 * @number: value to insert in new node
 * Return: address of new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current = *head;
    listint_t *prev = NULL;

    /* Create new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;

    /* If list is empty, or new number is smaller than the head */
    if (*head == NULL || current->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Traverse the list */
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    /* Insert new node */
    prev->next = new_node;
    new_node->next = current;

    return (new_node);
}