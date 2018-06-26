#include <bits/stdc++.h>
using namespace std;
 
// Funkcia iaka pochita serednie geometruchne i verne float nomer
float geometricMean(int arr[])
{
    // deklaruiemo zminnu suma i
    // stavumo ii rivnu  1. (ne null bo ne mojna umnojato na null)
    float summa = 1;
    int counter = 0;
    int n = sizeof(arr) / sizeof(arr[0]);
 
    // rexuiemo sumu vsix elementiv v masuvi
     for (int i = 1; i < n; i++)
    {
        if ( arr[i] % 3 != 0)
        summa = summa * arr[i];
        counter = counter + 1;
        
    }
 
    // serednie geometruchne
    float gm = pow(summa, (float)1 / counter);
    return gm;
}

// Driver function
int main()
{
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
    cout << geometricMean(arr);
    return 0;
}
