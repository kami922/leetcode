#include <unordered_set>
#include <vector>
#include <random>

class RandomizedSet {
public:
    RandomizedSet() {
        srand(time(NULL)); // Seed the random number generator
    }

    bool insert(int val) {
        return s.insert(val).second;
    }

    bool remove(int val) {
        return s.erase(val) > 0;
    }

    int getRandom() {
        int size = s.size();
        if (size == 0) {
            return -1; // Or handle the case as needed
        }
        int index = rand() % size;
        auto it = std::next(s.begin(), index);
        return *it;
    }

private:
    std::unordered_set<int> s;
};
/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */