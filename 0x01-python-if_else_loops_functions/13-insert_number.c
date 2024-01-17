#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a double pointer to the linked list
 * @number: the data
 * Return: the address of the new node on success. Otherwise NULL
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *prev_node, *curr_node;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;

    if (head == NULL || *head == NULL || (*head)->n > number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    curr_node = *head;
    while (curr_node != NULL && curr_node->n < number)
    {
        prev_node = curr_node;
        curr_node = curr_node->next;
    }
    prev_node->next = new_node;
    new_node->next = curr_node;
    return (new_node);
}
