#include <iostream>
using namespace std;

template <typename T>
class Vector {
private:
    T* elements;
    int currentSize;
    int currentCapacity;

    void grow() {
        currentCapacity *= 2;
        T* newElements = new T[currentCapacity];
        for (int i = 0; i < currentSize; i++) {
            newElements[i] = elements[i];
        }
        delete[] elements;
        elements = newElements;
    }

public:
    Vector() : currentSize(0), currentCapacity(1) {
        elements = new T[currentCapacity];
    }

    ~Vector() {
        delete[] elements;
    }

    void PushBack(T value) {
        if (currentSize == currentCapacity) {
            grow();
        }
        elements[currentSize++] = value;
    }

    T operator[](int index) const {
        if (index >= 0 && index < currentSize) {
            return elements[index];
        }
        throw out_of_range("Index out of range");
    }

    T& operator[](int index) {
        if (index >= 0 && index < currentSize) {
            return elements[index];
        }
        throw out_of_range("Index out of range");
    }

    friend ostream& operator<<(ostream& out, const Vector& other) {
        for (int i = 0; i < other.currentSize; i++) {
            out << other.elements[i] << " ";
        }
        return out;
    }
};

int main() {
    Vector<int> vec;
    int choice, value, index;

    while (true) {
        cout << "\nOptions:\n";
        cout << "1. Add element\n";
        cout << "2. Retrieve element by index\n";
        cout << "3. Display vector\n";
        cout << "4. Quit\n";
        cout << "Select an option: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter value to add: ";
            cin >> value;
            vec.PushBack(value);
        } else if (choice == 2) {
            cout << "Enter index: ";
            cin >> index;
            try {
                cout << "Element at index " << index << " is " << vec[index] << endl;
            } catch (const out_of_range& e) {
                cout << e.what() << endl;
            }
        } else if (choice == 3) {
            cout << "Vector: " << vec << endl;
        } else if (choice == 4) {
            return 0;
        } else {
            cout << "Invalid option. Please try again.\n";
        }
    }
}
