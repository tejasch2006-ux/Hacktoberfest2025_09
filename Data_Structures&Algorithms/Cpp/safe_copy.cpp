// safe_copy.cpp
#include <iostream>
#include <string>
#include <vector>
#include <cstring>

int main() {
    std::string input;
    std::cout << "Enter a string (max 100 chars): ";
    std::getline(std::cin, input);

    const std::size_t BUFFER_SIZE = 100;
    char buffer[BUFFER_SIZE + 1]; // +1 for null terminator

    if (input.size() > BUFFER_SIZE) {
        std::cerr << "Error: input too long (" << input.size() << " > " << BUFFER_SIZE << ").\n";
        return 1;
    }

    // safe copy
    std::memcpy(buffer, input.data(), input.size());
    buffer[input.size()] = '\0';

    std::cout << "Copied safely: " << buffer << "\n";
    return 0;
}
