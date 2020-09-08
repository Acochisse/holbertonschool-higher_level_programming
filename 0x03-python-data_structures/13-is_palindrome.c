#include "lists.h"

/**
 * is_palindrome - checks if the data in linked list is palindrome
 * @head: pointer to the list to be checked
 *
 * return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)

{
	listint_t *temp;
	stack <int> s;
	int i;

	temp = *head;
	while (temp != NULL)
	{
		s.push(temp);
		temp = temp->next;
	}
	while (head != NULL)
	{
		i = s.top();
		s.pop;
		if(head->n != i)
			return (0);
	}
       	head = head->next;
	return (1);
