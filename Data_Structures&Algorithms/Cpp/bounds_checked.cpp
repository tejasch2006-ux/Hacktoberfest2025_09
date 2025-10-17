// bounds_checked.cpp
#include <iostream>
#include <vector>
#include <stdexcept>

int main() {
    std::vector<int> v = {1,2,3,4,5};
    try {
        std::cout << "Accessing v.at(10)...\n";
        int x = v.at(10); // throws std::out_of_range
        std::cout << "Value: " << x << "\n";
    } catch (const std::out_of_range &e) {
        std::cerr << "Caught out_of_range exception: " << e.what() << "\n";
    }
    return 0;
}
