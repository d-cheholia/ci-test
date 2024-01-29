#include <iostream>
#include <chrono>
#include <format>

int main( )
{
    auto    now = std::chrono::system_clock::now();
    auto now_time_t = std::chrono::system_clock::to_time_t(now);
       auto tm = *std::localtime(&now_time_t);

    std::cout << "Current time: " << std::format("{:%Y-%m-%d %H:%M:%S}\n", tm);

    return 0;
}