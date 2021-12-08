#include <iostream>
#include <string>

using namespace std;

const int n = 4;

class Developer {
protected:
	string fullName;
	int age;
	string position;
	string* technologies;
public:
	Developer(string fullName, int age, string position) {
		this->fullName = fullName;
		this->age = age;
		this->position = position;
		this->technologies = NULL;
	}
	virtual void code() = 0;

	void learnNewTechnology(string* technologies) {
		this->technologies = technologies;
	}
};

class JuniorDeveloper : public Developer {
    public:
    void code override (string fullName, int age, string position) : Developer(fullName, age, "Junior") {
        cout << "Junior разработчик по имени " << this->fullName << " пишет код...";  
    }
}

class MiddleDeveloper : public Developer {
    public:
    void code override (string fullName, int age, string position) : Developer(fullName, age, "Middle") {
        cout << "Middle разработчик со стажем   " << this->age << "года пишет код...";
} } 

int main() {
	setlocale(LC_ALL, "rus");

	JuniorDeveloper junior("Настя", 18);
	junior.code();

	MiddleDeveloper middle("Влад", 24, 3.5);
	middle.code();

	SeniorDeveloper senior("Игорь", 30, "iTechArt");
	string* technologies = new string[n];
	for (int i = 0; i < n; i++) {
		cout << "Введите " << i + 1 << " технологию: ";
		cin >> technologies[i];
	}
	senior.learnNewTechnology(technologies);
	senior.code();

	system("pause");
	return 0;
}
