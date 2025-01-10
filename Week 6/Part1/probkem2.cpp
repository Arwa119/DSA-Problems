// Stack with array
#include <iostream>
#include <cstdio>
#define MAX 1000
using namespace std;

class StackArray {
    int top;
    int arr[MAX];

public:
    StackArray() { top = -1; }
    bool push(int x) {
        if (top >= (MAX - 1)) {
            printf("Stack Overflow\n");
            return false;
        } else {
            arr[++top] = x;
            printf("%d pushed into stack\n", x);
            return true;
        }
    }
    int pop() {
        if (top < 0) {
            printf("Stack Underflow\n");
            return 0;
        } else {
            int x = arr[top--];
            return x;
        }
    }
    int peek() {
        if (top < 0) {
            printf("Stack is Empty\n");
            return 0;
        } else {
            int x = arr[top];
            return x;
        }
    }
    bool isEmpty() {
        return (top < 0);
    }
};

// Stack with linked list

class Node {
public:
    int data;
    Node* next;
    Node(int data) : data(data), next(nullptr) {}
};

class StackLinkedList {
    Node* top;

public:
    StackLinkedList() { top = nullptr; }
    void push(int x) {
        Node* newNode = new Node(x);
        newNode->next = top;
        top = newNode;
        printf("%d pushed into stack\n", x);
    }
    int pop() {
        if (isEmpty()) {
            printf("Stack Underflow\n");
            return 0;
        } else {
            Node* temp = top;
            top = top->next;
            int popped = temp->data;
            delete temp;
            return popped;
        }
    }
    int peek() {
        if (isEmpty()) {
            printf("Stack is Empty\n");
            return 0;
        } else {
            return top->data;
        }
    }
    bool isEmpty() {
        return top == nullptr;
    }
};

// Queue with array

class QueueArray {
    int front, rear, size;
    int arr[MAX];

public:
    QueueArray() { front = size = 0; rear = MAX - 1; }
    bool enqueue(int x) {
        if (isFull()) {
            printf("Queue Overflow\n");
            return false;
        } else {
            rear = (rear + 1) % MAX;
            arr[rear] = x;
            size = size + 1;
            printf("%d enqueued to queue\n", x);
            return true;
        }
    }
    int dequeue() {
        if (isEmpty()) {
            printf("Queue Underflow\n");
            return 0;
        } else {
            int x = arr[front];
            front = (front + 1) % MAX;
            size = size - 1;
            return x;
        }
    }
    int peek() {
        if (isEmpty()) {
            printf("Queue is Empty\n");
            return 0;
        } else {
            return arr[front];
        }
    }
    bool isFull() {
        return (size == MAX);
    }
    bool isEmpty() {
        return (size == 0);
    }
};

// Queue with linked list

class QueueLinkedList {
    Node* front;
    Node* rear;

public:
    QueueLinkedList() { front = rear = nullptr; }
    void enqueue(int x) {
        Node* newNode = new Node(x);
        if (rear == nullptr) {
            front = rear = newNode;
            printf("%d enqueued to queue\n", x);
            return;
        }
        rear->next = newNode;
        rear = newNode;
        printf("%d enqueued to queue\n", x);
    }
    int dequeue() {
        if (isEmpty()) {
            printf("Queue Underflow\n");
            return 0;
        }
        Node* temp = front;
        front = front->next;
        if (front == nullptr) {
            rear = nullptr;
        }
        int dequeued = temp->data;
        delete temp;
        return dequeued;
    }
    int peek() {
        if (isEmpty()) {
            printf("Queue is Empty\n");
            return 0;
        } else {
            return front->data;
        }
    }
    bool isEmpty() {
        return front == nullptr;
    }
};
