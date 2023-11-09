---

# Doubly Linked Lists

This repository contains C programs that implement various functionalities of doubly linked lists. Each program is accompanied by a main file for testing.

## List of Programs

1. **Print list**
   - Description: This program prints all the elements of a  `dlistint_t`  list.
   - Prototype:  `size_t print_dlistint(const dlistint_t *h)` 
   - Return: the number of nodes
   - Format: see example

2. **List length**
   - Description: This program returns the number of elements in a linked  `dlistint_t`  list.
   - Prototype:  `size_t dlistint_len(const dlistint_t *h)` 

3. **Add node**
   - Description: This program adds a new node at the beginning of a  `dlistint_t`  list.
   - Prototype:  `dlistint_t *add_dnodeint(dlistint_t **head, const int n)` 
   - Return: the address of the new element, or NULL if it failed

4. **Add node at the end**
   - Description: This program adds a new node at the end of a  `dlistint_t`  list.
   - Prototype:  `dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)` 
   - Return: the address of the new element, or NULL if it failed

5. **Free list**
   - Description: This program frees a  `dlistint_t`  list.
   - Prototype:  `void free_dlistint(dlistint_t *head)` 

6. **Get node at index**
   - Description: This program returns the nth node of a  `dlistint_t`  linked list.
   - Prototype:  `dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)` 
   - Return: the address of the node, or NULL if it does not exist

7. **Sum list**
   - Description: This program returns the sum of all the data (n) of a  `dlistint_t`  linked list.
   - Prototype:  `int sum_dlistint(dlistint_t *head)` 
   - Return: the sum of the data, or 0 if the list is empty

8. **Insert at index**
   - Description: This program inserts a new node at a given position in a  `dlistint_t`  list.
   - Prototype:  `dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)` 
   - Return: the address of the new node, or NULL if it failed

9. **Delete at index**
   - Description: This program deletes the node at a given index in a  `dlistint_t`  list.
   - Prototype:  `int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)` 
   - Return: 1 if successful, -1 if failed

## Repository Details

- GitHub repository: [alx-low_level_programming](https://github.com/paschalugwu/alx-higher_level_programming)
- Directory: 0x17-doubly_linked_lists

---