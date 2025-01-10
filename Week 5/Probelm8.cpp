#include <iostream>
using namespace std;

template <typename T>
class ArrayList {
private:
    T* data;
    int currentSize;
    int currentCapacity;

    void grow() {
        currentCapacity = currentCapacity + currentCapacity / 2;
        T* newData = new T[currentCapacity];
        for (int i = 0; i < currentSize; i++) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }

public:
    ArrayList() : currentSize(0), currentCapacity(2) {
        data = new T[currentCapacity];
    }

    ~ArrayList() {
        delete[] data;
    }

    void PushBack(T value) {
        if (currentSize == currentCapacity) {
            grow();
        }
        data[currentSize++] = value;
    }

    T operator[](int index) const {
        if (index >= 0 && index < currentSize) {
            return data[index];
        }
        throw out_of_range("Index out of range");
    }

    T& operator[](int index) {
        if (index >= 0 && index < currentSize) {
            return data[index];
        }
        throw out_of_range("Index out of range");
    }

    friend ostream& operator<<(ostream& out, const ArrayList& other) {
        for (int i = 0; i < other.currentSize; i++) {
            out << other.data[i] << " ";
        }
        return out;
    }
};

int main() {
    ArrayList<int> arr;
    int choice, value, index;

    while (true) {
        cout << "\nOptions:\n";
        cout << "1. Add element to the end\n";
        cout << "2. Retrieve element by index\n";
        cout << "3. Display array\n";
        cout << "4. Exit\n";
        cout << "Select an option: ";
        cin >> choice;

        if (choice == 1) {
            cout << "Enter the value to add: ";
            cin >> value;
            arr.PushBack(value);
        } else if (choice == 2) {
            cout << "Enter the index: ";
            cin >> index;
            try {
                cout << "Element at index " << index << " is " << arr[index] << endl;
            } catch (const out_of_range& e) {
                cout << e.what() << endl;
            }
        } else if (choice == 3) {
            cout << "Array contents: " << arr << endl;
        } else if (choice == 4) {
            return 0;
        } else {
            cout << "Invalid option. Please try again.\n";
        }
    }
}
