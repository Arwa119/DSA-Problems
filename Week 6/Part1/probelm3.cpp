#include <iostream>

class Node
{
public:
    int data;
    Node *next;
    Node *prev;
    Node(int data) : data(data), next(nullptr), prev(nullptr) {}
};

class DoublyLinkedList
{
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}
    ~DoublyLinkedList();

    bool isEmpty() { return head == nullptr; }
    Node *insertNode(int index, int x);
    Node *insertAtHead(int x);
    Node *insertAtEnd(int x);
    bool findNode(int x);
    bool deleteNode(int x);
    bool deleteFromStart();
    bool deleteFromEnd();
    void displayList();
    Node *reverseList();
    Node *sortList(Node *list);
    Node *removeDuplicates(Node *list);
    Node *mergeLists(Node *list1, Node *list2);
    Node *intersectLists(Node *list1, Node *list2);

private:
    Node *head;
    Node *tail;
};

// Destructor to clean up memory
DoublyLinkedList::~DoublyLinkedList()
{
    Node *current = head;
    while (current != nullptr)
    {
        Node *next = current->next;
        delete current;
        current = next;
    }
}

Node *DoublyLinkedList::insertNode(int index, int x)
{
    if (index < 0)
        return nullptr;

    Node *newNode = new Node(x);

    if (index == 0)
    {
        newNode->next = head;
        if (head != nullptr)
            head->prev = newNode;
        head = newNode;
        if (tail == nullptr)
            tail = newNode;
        return newNode;
    }

    Node *current = head;
    for (int i = 0; i < index - 1 && current != nullptr; ++i)
    {
        current = current->next;
    }

    if (current == nullptr)
    {
        delete newNode;
        return nullptr;
    }

    newNode->next = current->next;
    newNode->prev = current;
    if (current->next != nullptr)
        current->next->prev = newNode;
    current->next = newNode;
    if (newNode->next == nullptr)
        tail = newNode;

    return newNode;
}

Node *DoublyLinkedList::insertAtHead(int x)
{
    Node *newNode = new Node(x);
    newNode->next = head;
    if (head != nullptr)
        head->prev = newNode;
    head = newNode;
    if (tail == nullptr)
        tail = newNode;
    return newNode;
}

Node *DoublyLinkedList::insertAtEnd(int x)
{
    Node *newNode = new Node(x);
    if (tail == nullptr)
    {
        head = tail = newNode;
        return newNode;
    }
    tail->next = newNode;
    newNode->prev = tail;
    tail = newNode;
    return newNode;
}

bool DoublyLinkedList::findNode(int x)
{
    Node *current = head;
    while (current != nullptr)
    {
        if (current->data == x)
        {
            return true;
        }
        current = current->next;
    }
    return false;
}

bool DoublyLinkedList::deleteNode(int x)
{
    bool deleted = false;
    Node *current = head;

    while (current != nullptr)
    {
        if (current->data == x)
        {
            if (current->prev != nullptr)
                current->prev->next = current->next;
            if (current->next != nullptr)
                current->next->prev = current->prev;
            if (current == head)
                head = current->next;
            if (current == tail)
                tail = current->prev;
            Node *temp = current;
            current = current->next;
            delete temp;
            deleted = true;
        }
        else
        {
            current = current->next;
        }
    }

    return deleted;
}

bool DoublyLinkedList::deleteFromStart()
{
    if (head == nullptr)
        return false;
    Node *temp = head;
    head = head->next;
    if (head != nullptr)
        head->prev = nullptr;
    else
        tail = nullptr;
    delete temp;
    return true;
}

bool DoublyLinkedList::deleteFromEnd()
{
    if (tail == nullptr)
        return false;
    Node *temp = tail;
    tail = tail->prev;
    if (tail != nullptr)
        tail->next = nullptr;
    else
        head = nullptr;
    delete temp;
    return true;
}

void DoublyLinkedList::displayList()
{
    Node *current = head;
    while (current != nullptr)
    {
        std::cout << current->data << " <-> ";
        current = current->next;
    }
    std::cout << "nullptr" << std::endl;
}

Node *DoublyLinkedList::reverseList()
{
    Node *current = head;
    Node *temp = nullptr;

    while (current != nullptr)
    {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev;
    }

    if (temp != nullptr)
        head = temp->prev;

    return head;
}

Node *DoublyLinkedList::sortList(Node *list)
{
    if (list == nullptr || list->next == nullptr)
        return list;

    Node *sorted = nullptr;

    while (list != nullptr)
    {
        Node *current = list;
        list = list->next;

        if (sorted == nullptr || sorted->data >= current->data)
        {
            current->next = sorted;
            if (sorted != nullptr)
                sorted->prev = current;
            sorted = current;
        }
        else
        {
            Node *temp = sorted;
            while (temp->next != nullptr && temp->next->data < current->data)
            {
                temp = temp->next;
            }
            current->next = temp->next;
            if (temp->next != nullptr)
                temp->next->prev = current;
            temp->next = current;
            current->prev = temp;
        }
    }

    return sorted;
}

Node *DoublyLinkedList::removeDuplicates(Node *list)
{
    if (list == nullptr)
        return list;

    Node *current = list;

    while (current->next != nullptr)
    {
        if (current->data == current->next->data)
        {
            Node *temp = current->next;
            current->next = current->next->next;
            if (current->next != nullptr)
                current->next->prev = current;
            delete temp;
        }
        else
        {
            current = current->next;
        }
    }

    return list;
}

Node *DoublyLinkedList::mergeLists(Node *list1, Node *list2)
{
    if (list1->data < list2->data)
    {
        list1->next = mergeLists(list1->next, list2);
        list1->next->prev = list1;
        list1->prev = nullptr;
        return list1;
    }
    else
    {
        list2->next = mergeLists(list1, list2->next);
        list2->next->prev = list2;
        list2->prev = nullptr;
        return list2;
    }
}

Node *DoublyLinkedList::intersectLists(Node *list1, Node *list2)
{
    Node *result = nullptr;
    Node **lastPtrRef = &result;

    while (list1 != nullptr && list2 != nullptr)
    {
        if (list1->data == list2->data)
        {
            Node *newNode = new Node(list1->data);
            *lastPtrRef = newNode;
            lastPtrRef = &(newNode->next);
            list1 = list1->next;
            list2 = list2->next;
        }
        else if (list1->data < list2->data)
        {
            list1 = list1->next;
        }
        else
        {
            list2 = list2->next;
        }
    }

    return result;
}
