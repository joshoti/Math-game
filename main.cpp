#include <iostream>
#include <ctime>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

vector<int> questionGenerator(int operatorsSize)
{
	/*
	Random Generator
		Random = (rand() % stop) + start

	Example Use
		(rand() % 3) + 1  // Random integer between 1-3
		2

		rand() % 3  // Random integer between 0-2
		2
	*/
	srand(time(0));
	int leftHand = rand() % 101; // Random integer between 0-100
	int operation = rand() % operatorsSize; // Random integer between 0 - operatorArr.size
	int rightHand, answer, picker;
	vector<int> rightHandSet;
	switch (operation)
	{
	case 0: // addition
		rightHand = rand() % 101; // Random integer between 0-100
		answer = leftHand + rightHand;
		break;
	case 1: // subtraction
		rightHand = rand() % 101; // Random integer between 0-100
		answer = leftHand - rightHand;
		break;
	case 2: // multiplication
		rightHand = rand() % 11; // Random integer between 0-10
		answer = leftHand * rightHand;
		break;
	case 3: // floor division
		rightHand = rand() % 101; // Random integer between 0-100
		answer = leftHand / rightHand;
		break;
	case 4: // modulo
		picker = rand() % 4; // Random integer between 0-3
		rightHandSet = { 2,3,5,10 };
		rightHand = rightHandSet[picker];
		answer = leftHand % rightHand;
		break;
	case 5: // pow
		leftHand = rand() % 21; // Random integer between 0-20
		rightHand = rand() % 3; // Random integer between 0-2
		answer = pow(leftHand, rightHand);
		break;
	}
	return { leftHand, operation, rightHand, answer };
}
int main()
{	
	int play = 1;
	while (play){
		int correctCount = 0;
		for (int i = 1; i < 11; i++) {
			vector<string> operators = { " + ", " - ", " * ", " // ", " % ", " ** " };
			vector<int> question = questionGenerator(operators.size());	// { leftHand, Operator, rightHand, Answer }
			cout << "Question " << i << " / 10" << endl;
			cout << "\t\t" << question[0] << operators[question[1]] << question[2] << endl;
			cout << "Your Answer:    ";
			int userInput;
			cin >> userInput;
			if (userInput == question[3]) {
				correctCount++;
				cout << "Correct!" << endl;
			}
			else
				cout << "\nIncorrect!\nCorrect answer is: " << question[3] << endl;
			cout << endl;
		}
		cout << "You answered " << correctCount << " questions correctly!\n";
		if (8 <= correctCount)
			cout << "Excellent Performance!" << endl;
		else if (6 <= correctCount)
			cout << "Above Average Performance!" << endl;
		else if (4 <= correctCount)
			cout << "Average Performance!" << endl;
		else if (correctCount < 4)
			cout << "You Can Do Better Kido!" << endl;
		
		while (true){
			cout << "Would you like to retry?  ( 1/0 ) [ 1=yes / 0=no ]" << endl;
			cin >> play;
			if (play == 1 || play == 0)
				break;
		}
	}
}
