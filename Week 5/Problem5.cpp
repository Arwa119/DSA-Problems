#include <iostream>
#include <vector>

using namespace std;

void displayMatrix(const vector<vector<int>>& mat) {
    for (int i = 0; i < mat.size(); i++) {
        for (int j = 0; j < mat[i].size(); j++) {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

void addRow(vector<vector<int>>& mat, vector<int>& row) {
    mat.push_back(row);
}

void addCol(vector<vector<int>>& mat, vector<int>& col) {
    for (int i = 0; i < mat.size(); i++) {
        mat[i].push_back(col[i]);
    }
}

vector<vector<int>> transposeMatrix(vector<vector<int>>& mat) {
    vector<vector<int>> transposed;
    int rows = mat.size();
    int cols = mat[0].size();
    for (int i = 0; i < cols; i++) {
        vector<int> row;
        for (int j = 0; j < rows; j++) {
            row.push_back(0);
        }
        transposed.push_back(row);
    }

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            transposed[j][i] = mat[i][j];
        }
    }
    return transposed;
}

int main() {
    vector<vector<int>> mat = {{2, 4}, {0, 6}};

    cout << "Initial Matrix:" << endl;
    displayMatrix(mat);

    vector<int> newRow = {7, 10};
    addRow(mat, newRow);
    cout << "\nMatrix after adding a new row:" << endl;
    displayMatrix(mat);

    vector<int> newCol = {11, 4, 9}; 
    addCol(mat, newCol);
    cout << "\nMatrix after adding a new column:" << endl;
    displayMatrix(mat);

    vector<vector<int>> transposedMat = transposeMatrix(mat);
    cout << "\nTransposed Matrix:" << endl;
    displayMatrix(transposedMat);

    return 0;
}
