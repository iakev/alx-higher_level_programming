#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to a pointer of the start of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	int cycle = 0, i = 0, j;
	listint_t *arr[100];

	current = list;
	while(current != NULL)
	{
		arr[i++] = current;
		current = current->next;
		for(j = 0; j < i; j++)
		{
			if (current == arr[j])
			{
				cycle = 1;
				break;
			}
		}
		if (cycle == 1)
			break;
	}
	return (cycle);
}
