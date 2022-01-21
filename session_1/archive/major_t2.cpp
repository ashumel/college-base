#include <iostream>
using namespace std;
int main()
{
	setlocale(LC_ALL, "RUS");
	cout << "Введите сумму (больше 7) :\n";
	int sum, l;
	cin >> sum;
	l = sum;
	int ThreeKop = 3;
	int FiveKop = 5;
	int count1, count2;
	for (int i = 1; i <= 60; i++)
	{
		if (sum == FiveKop * i)
		{
			cout << sum << " = " << FiveKop << " * " << i << endl;
	
		}
	}
	tryAgain1:

	for (int i = 1; i <= 60; i++)
	{
		if (sum == ThreeKop * i)
		{
			cout << sum << " = " << ThreeKop << " * " << i << endl;
	
		}
		
	}
	tryAgain2:
	
	for (int i = 1; i <= 60; i++)
	{
		l -= 3;
		for (int j = 1; j <= 60; j++)
		{
			if (l == FiveKop * j)
			{
				cout << "Можно заплaтить: " << FiveKop << " * " << j << " + " << ThreeKop << " * " << i << endl;
			}
		}
	}
	return 0;
}