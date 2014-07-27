#include<iostream>
#include<algorithm>
#include<new>
using namespace std;
int main() {

int* a = NULL;   // Pointer to int, initialize to nothing.
int n;           // Size needed for array
cin >> n;        // Read in the size
a = new int[n];  // Allocate n ints and save ptr in a.
for (int i=0; i<n; i++) {
  cin>>a[i] ;    // Initialize all elements to zero.
}
cout<<"hello";
return 0;
}
