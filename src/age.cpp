#include <iosteam>

int   main( )
{
    std::size_t age{         };

    std::cout  <<  "Enter your age: ";
       std::cin >>    age;

    std::cout <<  "You have lived for " << age * 12 << " months.\n";
    return 0;
}
