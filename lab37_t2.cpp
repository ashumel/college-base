#include <iostream>
using namespace std;
const int n = 9;  //* Обозначаем количество вершин
int i, j;
int GM[n][n] = { //* Инициализируем граф, в виде смежной матрицы
	{0, 2, 0, 1, 1, 0, 0, 0, 0},
	{2, 0, 1, 0, 1, 1, 0, 0, 0},
	{0, 1, 0, 0, 0, 2, 0, 0, 0},
	{1, 0, 0, 2, 1, 0, 0, 0, 0},
	{1, 1, 0, 1, 0, 0, 0, 0, 0},
	{0, 1, 2, 0, 0, 0, 0, 0, 1},
	{0, 0, 0, 1, 0, 0, 0, 1, 0},
	{0, 0, 0, 0, 0, 0, 1, 2, 3},
	{0, 0, 0, 0, 1, 1, 0, 3, 0}
};
//* Функция поиска в ширину
void BFS(bool* visited, int unit) {
	int* queue = new int[n]; //_____
	int count, head;
	for (i = 0; i < n; i++)
		queue[i] = 0;
	count = 0; head = 0;
	queue[count++] = unit;
	visited[unit] = true;
	while (head < count) { //_____
		unit = queue[head++];
		cout << unit + 1 << " ";
		for (i = 0; i < n; i++)
			if (GM[unit][i] && !visited[i]) {
				queue[count++] = i;
				visited[i] = true;
			}
	}
	delete[]queue; //_____
}
int main() {
	setlocale(LC_ALL, "Rus");
	int start;
	cout << "Стартовая вершина >> ";
	cin >> start;
	bool* visited = new bool[n]; //_____
	cout << "Матрица смежности графа: " << endl;
	for (i = 0; i < n; i++) {
		visited[i] = false;
		for (j = 0; j < n; j++)
			cout << " " << GM[i][j];
		cout << endl;
	}
	cout << "Порядок обхода: ";
	BFS(visited, start - 1); //_____
	delete[]visited; //_____
	system("pause");
	return 0;
}
