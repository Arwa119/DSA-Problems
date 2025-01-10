#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> num = {12, 13, 14, 15, 13, 2, 3, 24, 23, 4, 1, 3};
    int find;
    int n = num.size();
    cout << "Enter the number of element: \n";
    cin >> find;
    for (int i = 0; i <= n; i++)
    {
        if (find == num[i])
        {
            cout << "Element found at index: " << i;
        }
        else
        {
            cout << "Element not found";
        }
    }
}