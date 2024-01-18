#include "lists.h"

/**
 * check_cycle - check a linked list if it is a circle
 * @list: pointer to the linked list
 * Return: 0 if the is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *tmp = list->next;

    while (tmp != NULL && tmp != list)
    {
        tmp = tmp->next;
    }
    if (tmp == NULL)
        return (0);
    return (1);
}
