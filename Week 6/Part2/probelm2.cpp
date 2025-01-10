#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string>
#define MAX 1000
using namespace std;

class StackArray
{
    int top;
    int arr[MAX];

public:
    StackArray() { top = -1; }

    bool push(int x)
    {
        if (top >= (MAX - 1))
        {
            printf("Stack Overflow\n");
            return false;
        }
        else
        {
            arr[++top] = x;
            printf("%d pushed into stack\n", x);
            return true;
        }
    }

    int pop()
    {
        if (top < 0)
        {
            printf("Stack Underflow\n");
            return 0;
        }
        else
        {
            int x = arr[top--];
            return x;
        }
    }

    int peek()
    {
        if (top < 0)
        {
            printf("Stack is Empty\n");
            return 0;
        }
        else
        {
            int x = arr[top];
            return x;
        }
    }

    bool isEmpty()
    {
        return (top < 0);
    }

    string toString()
    {
        if (top < 0)
        {
            return "Stack is Empty";
        }
        stringstream ss;
        for (int i = 0; i <= top; i++)
        {
            ss << arr[i] << " ";
        }
        return ss.str();
    }
};

int main()
{
    StackArray stack;
    string input;

    while (true)
    {
        getline(cin, input);

        if (input == "!")
        {
            break;
        }
        else if (input == "?")
        {
            cout << stack.toString() << endl;
        }
        else if (input == "^")
        {
            if (!stack.isEmpty())
            {
                cout << stack.pop() << endl;
            }
            else
            {
                cout << "Stack is Empty" << endl;
            }
        }
        else if (input == "+" || input == "-" || input == "*" || input == "/" || input == "%")
        {
            if (stack.isEmpty())
            {
                cout << "Stack Underflow" << endl;
                continue;
            }
            int b = stack.pop();
            if (stack.isEmpty())
            {
                cout << "Stack Underflow" << endl;
                stack.push(b); 
                continue;
            }
            int a = stack.pop();
            int result;
            if (input == "+")
            {
                result = a + b;
            }
            else if (input == "-")
            {
                result = a - b;
            }
            else if (input == "*")
            {
                result = a * b;
            }
            else if (input == "/")
            {
                if (b == 0)
                {
                    cout << "Division by zero error" << endl;
                    stack.push(a); 
                    stack.push(b);
                    continue;
                }
                result = a / b;
            }
            else if (input == "%")
            {
                if (b == 0)
                {
                    cout << "Division by zero error" << endl;
                    stack.push(a); 
                    stack.push(b);
                    continue;
                }
                result = a % b;
            }
            stack.push(result);
        }
        else
        {
            try
            {
                int num = stoi(input);
                stack.push(num);
            }
            catch (invalid_argument &)
            {
                cout << "Invalid input" << endl;
            }
        }
    }

    return 0;
}
