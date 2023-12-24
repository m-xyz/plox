#include <stdio.h>
#include <stdlib.h>

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
		if(c == "L"){
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


/* TODO */
void delete(int x){
	struct Node* y = find(x);
	if(y != NULL) printf("%d\n",y->k);
}

int main(){
	insert(6, "R");
	insert(69, "R");
	insert(111, "L");
	insert(4,"R");
	//find(111);
	//find(4);
	//find(42);
	delete(111);
	delete(42);

	struct Node* curr_node = head;

	while(curr_node != NULL){
		printf("%d : %p | ",curr_node->k, &curr_node->next);
		curr_node = curr_node->next;
	}
	printf("\n");

	return 0;
}
