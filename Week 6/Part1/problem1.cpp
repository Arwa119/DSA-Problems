#include <iostream>
using namespace std;

//problem 1
class Node {
public:
    int data;
    Node* next;
    Node(int data) : data(data), next(nullptr) {}
};

class LinkedList {
public:
    LinkedList() : head(nullptr) {}
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

    bool isEmpty() { return head == nullptr; }

    Node* insertNode(int index, int x) {
        if (index < 0) return nullptr;
        Node* newNode = new Node(x);
        if (index == 0) {
            newNode->next = head;
            head = newNode;
            return newNode;
        }
        Node* current = head;
        for (int i = 0; i < index - 1 && current != nullptr; ++i) {
            current = current->next;
        }
        if (current == nullptr) {
            delete newNode;
            return nullptr;
        }
        newNode->next = current->next;
        current->next = newNode;
        return newNode;
    }

    Node* insertAtHead(int x) {
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        return newNode;
    }

    Node* insertAtEnd(int x) {
        Node* newNode = new Node(x);
        if (head == nullptr) {
            head = newNode;
            return newNode;
        }
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
        return newNode;
    }

    bool findNode(int x) {
        Node* current = head;
        while (current != nullptr) {
            if (current->data == x) {
                return true;
            }
            current = current->next;
        }
        return false;
    }

    bool deleteNode(int x) {
        bool deleted = false;
        while (head != nullptr && head->data == x) {
            Node* temp = head;
            head = head->next;
            delete temp;
            deleted = true;
        }
        Node* current = head;
        while (current != nullptr && current->next != nullptr) {
            if (current->next->data == x) {
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
                deleted = true;
            } else {
                current = current->next;
            }
        }
        return deleted;
    }

    bool deleteFromStart() {
        if (head == nullptr) return false;
        Node* temp = head;
        head = head->next;
        delete temp;
        return true;
    }

    bool deleteFromEnd() {
        if (head == nullptr) return false;
        if (head->next == nullptr) {
            delete head;
            head = nullptr;
            return true;
        }
        Node* current = head;
        while (current->next->next != nullptr) {
            current = current->next;
        }
        delete current->next;
        current->next = nullptr;
        return true;
    }

    void displayList() {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " -> ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }

    Node* reverseList() {
        Node* prev = nullptr;
        Node* current = head;
        Node* next = nullptr;
        while (current != nullptr) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
        return head;
    }

    Node* sortList(Node* list) {
        if (list == nullptr || list->next == nullptr) return list;
        Node* sorted = nullptr;
        while (list != nullptr) {
            Node* current = list;
            list = list->next;
            if (sorted == nullptr || sorted->data >= current->data) {
                current->next = sorted;
                sorted = current;
            } else {
                Node* temp = sorted;
                while (temp->next != nullptr && temp->next->data < current->data) {
                    temp = temp->next;
                }
                current->next = temp->next;
                temp->next = current;
            }
        }
        return sorted;
    }

    Node* removeDuplicates(Node* list) {
        if (list == nullptr) return list;
        Node* current = list;
        while (current->next != nullptr) {
            if (current->data == current->next->data) {
                Node* temp = current->next;
                current->next = current->next->next;
                delete temp;
            } else {
                current = current->next;
            }
        }
        return list;
    }

    Node* mergeLists(Node* list1, Node* list2) {
        if (list1 == nullptr) return list2;
        if (list2 == nullptr) return list1;
        if (list1->data < list2->data) {
            list1->next = mergeLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeLists(list1, list2->next);
            return list2;
        }
    }

    Node* intersectLists(Node* list1, Node* list2) {
        Node* result = nullptr;
        Node** lastPtrRef = &result;
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->data == list2->data) {
                Node* newNode = new Node(list1->data);
                *lastPtrRef = newNode;
                lastPtrRef = &(newNode->next);
                list1 = list1->next;
                list2 = list2->next;
            } else if (list1->data < list2->data) {
                list1 = list1->next;
            } else {
                list2 = list2->next;
            }
        }
        return result;
    }

private:
    Node* head;
};

