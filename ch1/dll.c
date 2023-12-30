#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
	int k;
	struct Node* next;
	struct Node* prev;
};

struct Node* head = NULL;
struct Node* tail = NULL;
struct Node* t = NULL;
int i = 0;

void insert(int x, char* c){

	struct Node* ptr = (struct Node*)malloc(sizeof(struct Node));

	/* (ptr*).k = x */
	ptr->k = x;
	ptr->next = NULL;
	ptr->prev = NULL;

	if(head == NULL){
		head = ptr;
		tail = head;
	}

	else{
		if(strcmp(c, "L") == 0){
			t = ptr;
			t->next = head;
			head->prev = t;
			head = t;
		}
		else{
			tail->next = ptr;
			ptr->prev = tail;
			tail = ptr;
		}
	}
	i++;
}

struct Node* find(int x){

	struct Node* curr_node = head;

	while(curr_node != NULL){
		if(curr_node->k == x) break;
		curr_node = curr_node->next;
	}

	if(curr_node == NULL) printf("[%d] NOT FOUND!\n",x);

	else printf("[%d] FOUND!\n",x);

	return curr_node;
}

void delete(int x){
	struct Node* y = find(x);
	if(y == NULL) return;

	if(y == head){
		head = y->next;
		y->next = NULL;
	}
	if(y == tail){
		tail = y->prev;
		tail->next = NULL;
	}
	if(y != NULL) printf("del -> %d\n",y->k);
	free(y);
	i--;
}

int main(){
	insert(6, "R");
	insert(69, "R");
	insert(111, "L");
	insert(4, "R");
	delete(111);
	//delete(42);
	//delete(4);
	delete(6);
	//delete(69);

	struct Node* curr_node = head;

	if(curr_node != NULL){
		printf("val of head: %d\n",head->k);
		printf("val of tail: %d\n",tail->k);

		while(curr_node != NULL){
			printf("%d : %p | ",curr_node->k, &curr_node->next);
			curr_node = curr_node->next;
		}
		printf("\n");
	}
	return 0;
}
