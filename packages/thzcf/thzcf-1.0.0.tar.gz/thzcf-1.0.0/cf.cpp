#include <iostream>
using namespace std;

void cf()
{
    for(int i = 1;i < 10;i++){
		for (int j = i;j>=i && j < 10;j++){
			cout<<i<<"x"<<j<<"="<<i*j<<"\t";
		}
		cout<<"\n";
	}
	
}

