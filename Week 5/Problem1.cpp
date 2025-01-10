#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<string> str;
    while (true)
    {
        cout << "Press 1 to enter element\n";
        cout << "Press 2 to remove element\n";
        int pr;
        cin >> pr;
        if (pr == 1)
        {
            cout << "Enter elements: ";
            string ele;
            cin >> ele;
            str.push_back(ele);
            cout << "Size: " << str.size() << "\nCapacity: \n"
                 << str.capacity();
        }
        if (pr == 2)
        {
            if (str.size() == 0)
            {
                cout << "No element availble to pop \n";
            }
            str.pop_back();
            cout << "Size: " << str.size() << "\nCapacity: \n"
                 << str.capacity();
        }
    }
}