#include<iostream>
#include<vector>
using namespace std;
vector<int> ReverseElements(vector<int>num)
{
    vector<int> reverse;
    int n = num.size();
    int m = 0;
    for (int i = n; i>= 0; i--)
    {
        reverse[m]=num[i];
        m++;
    }
    // reverse.erase(reverse.begin());
    return reverse;
}

vector<int> SortElements(vector<int> num)
{
    int n = num.size(); 
    for(int i = 0; i<(n-1); i++)
    {   int min = i;
        for (int j = (i+1) ; j < n; j++)
        {
            if(num[j]<num[min])
            {
                min = j;
            }
        }
        swap(num[i], num[min]);
    } 
    return num;
}

vector<int> RemoveDuplicates(vector<int> num)
{
    int n = num.size();
    for(int i = 0; i < n; i++)
    {
        int check = num[i];
        for (int j = i + 1; j < n; j++)
        {
            if(num[j] == check){
                num.erase(num.begin() + j);
                n--;
                j--; 
            }
        }
    }
    return num;
}
int main()
{
    vector<int> num = {12,34,56,12,34,7,8,0,45,12,3,45,28,28,28};
    vector<int> reverse = ReverseElements(num);
    vector<int> sorted = SortElements(num);
    vector<int> removed = RemoveDuplicates(num);
    cout<<"The reverse of the elements are: ";
    for (int i = 0; i < reverse.size(); i++)
    {
        cout<<reverse[i]<<" ";
    }
    cout<<"\n";
    cout<<"The sorted elements are: ";
    for (int i = 0; i < sorted.size(); i++)
    {
        cout<<sorted[i]<<" ";
    }
    cout<<"\n";
    cout<<"The elements after removing duplicates are: ";
    for (int i = 0; i < removed.size(); i++)
    {
        cout<<removed[i]<<" ";
    }
}
