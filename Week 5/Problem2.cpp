#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> num;
    for (int i = 0; i < 100; i++)
    {
        num.push_back(i);
        cout << "Size: " << num.size() << "\nCapacity: " << num.capacity() << endl;
    }
}

// the capacity doubled each time the limit is exceeded
