#include "lists.h"

/**
 * is_palindrome - checks whether singly linked list is a palindrome
 * @head: pointer to head node of linked list
 * Return: 0 if not palindrome or 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp_head = *head;
	int x = 0;
	int array[10000];
	int index;
	int y;

	if (tmp_head == NULL || tmp_head->next == NULL)
		return (1);
	while (tmp_head != NULL)
	{
		array[x] = tmp_head->n;
		tmp_head = tmp_head->next;
		x++;
	}
	for (index = 0, y = x - 1; index < y; index++, y--)
	{
		if (array[index] != array[y])
			return (0);
	}
	return (1);

}
