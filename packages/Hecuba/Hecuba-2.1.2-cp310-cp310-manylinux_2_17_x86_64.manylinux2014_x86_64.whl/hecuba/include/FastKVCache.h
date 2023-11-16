#ifndef FastKVCache_INCLUDED
#define FastKVCache_INCLUDED

#include <iostream>
#include <unordered_map>
#include <list>

/***
 * Simple implementation of a Cache with a simple replacement policy.
 * @tparam TKey Key indexing, must be hashable
 * @tparam TValue Value associated to the Key
 */
template<class TKey, class TValue>
class FastKVCache {

public:
    FastKVCache(size_t size = 1024) {
        this->max_cache_size = size;
        this->current_size = 0;
    }

    ~FastKVCache() {
        this->clear();
    }

    // Getters

    size_t size() const {
        return this->current_size;
    }

    const TValue &get(const TKey &key) const {
        //yolandab
        //std::cout<<"Trying to get from cache"<<std::endl;
        auto it = cache_items_map.find(key);

        if (it == cache_items_map.end()) {
            //yolandab
            //std::cout<<"NOT Found it"<<std::endl;
            throw std::out_of_range("No such key in the cache");
        } else {
            //yolandab
            //std::cout<<"Found it in cache"<<std::endl;
            return it->second;
        }
    }


    // Modifiers

    void add(const TKey &key, const TValue &value) {
        auto it = cache_items_map.find(key);

        // Not found
        if (it == cache_items_map.end()) {
            if (current_size + 1 > max_cache_size) {
                // FLUSH EVERYTHING
                this->clear();
            }
            current_size ++;

            //cache_items_map[key] = value;
            cache_items_map.insert(std::make_pair(key,value));
        } else {
            it->second = value;
        }
    }

    void remove(const TKey &key) {
        auto it = cache_items_map.find(key);
        if (it != cache_items_map.end()) {
            cache_items_map.erase(key);
            current_size --;
        }
    }

    void clear() {
        cache_items_map.clear();
        current_size = 0;
    }


private:
    // Prevent the copy of a Cache
    FastKVCache(const FastKVCache &aCache);

    FastKVCache &operator=(const FastKVCache &aCache);

    size_t max_cache_size;
    size_t current_size;

    // Map containing references to the list items for update / read / removal purposes
    std::unordered_map<TKey, TValue> cache_items_map;
};


#endif // FastKVCache_INCLUDED
