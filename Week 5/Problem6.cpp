#include <iostream>
using namespace std;

template <typename T>
class AutoGrowingArray {
private:
    T* data;
    int currentSize;
    int currentCapacity;

    void grow() {
        currentCapacity++;
        T* newData = new T[currentCapacity];
        for (int i = 0; i < currentSize; i++) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
    }

public:
    AutoGrowingArray() : currentSize(0), currentCapacity(1) {
        data = new T[currentCapacity];
    }

    ~AutoGrowingArray() {
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

    friend ostream& operator<<(ostream& out, const AutoGrowingArray& other) {
        for (int i = 0; i < other.currentSize; i++) {
            out << other.data[i] << " ";
        }
        return out;
    }
};

int main() {
    AutoGrowingArray<int> arr;
    int choice, value, index;

    while (true) {
        cout << "\nOptions:\n";
        cout << "1. Add element\n";
        cout << "2. Retrieve element by index\n";
        cout << "3. Display array\n";
        cout << "4. Quit\n";
        cout << "Select an option: ";
        cin >> choice;
        if(choice == 1) {
            cout << "Enter value to add: ";
            cin >> value;
            arr.PushBack(value);
        }
        if(choice == 2) {
            cout << "Enter index: ";
            cin >> index;
            try {
                cout << "Element at index " << index << " is " << arr[index] << endl;
            } catch (const out_of_range& e) {
                cout << e.what() << endl;
            }
        }
        if(choice == 3) {
            cout << "Array contents: " << arr << endl;
        }
        if(choice == 4) {
            return 0;
        }
        if(choice < 1 || choice > 4) {
            cout << "Invalid option. Please try again.\n";
        }
    }
}
