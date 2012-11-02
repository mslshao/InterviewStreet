#include <iostream>
#include <string>

using namespace std;

#define MAXN 100002
#define MAXINT 1000002

int n, temp;
long a[MAXN], c[MAXINT];

int main() {
    int T, i, j;
    cin >> T; // # of test cases
    while (T--)
	{
		long iter=0;
		cin >> n; // # of integers per line
		// Inserting integers into the array
		for (i=0; i<n; i++) cin >> a[i]; 
		for (i=0; i<n; i++)
		{
			//cout << "Current value scope is: " << a[i] << endl;
			j = i;
			while ((j > 0) && (a[j] < a[j-1]))
			{
				temp = a[j];
				a[j] = a[j-1];
				a[j-1] = temp;
				iter+=1;
				j-=1;
			}
		}
		//for (i=0; i<n; i++) cout << a[i] << " ";
		//cout << endl; 
		cout << iter << endl;
	}
    
    return 0;
}
