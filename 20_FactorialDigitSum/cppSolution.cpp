#include <iostream>
using namespace std;

int main()
{
    bignum x = 2;
    bignum y = x.pow(4096);
    std::cout << y.to_string(10) << std::endl;
}